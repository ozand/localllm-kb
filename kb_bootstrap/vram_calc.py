"""VRAM and KV Cache estimation engine for local LLM deployments.

Provides deterministic mathematical calculations for:
1. Base model quantized weights resident in VRAM.
2. KV Cache memory across layers, attention heads, head dimension, and context lengths.
3. Total peak VRAM footprint with activation headroom and placement classifications
   (full_vram_fit, partial_cpu_offload, out_of_memory) across standard GPU tiers.
"""

from typing import Dict, Any, List, Optional

# Standard bits per parameter for popular quantization formats
QUANT_BITS_MAP: Dict[str, float] = {
    "FP16": 16.0,
    "BF16": 16.0,
    "Q8_0": 8.5,
    "Q6_K": 6.56,
    "Q5_K_M": 5.54,
    "Q5_K_S": 5.45,
    "Q4_K_M": 4.50,
    "Q4_K_S": 4.35,
    "UD-Q4_K_S": 4.40,
    "Q3_K_M": 3.43,
    "Q3_K_S": 3.30,
    "Q2_K": 2.63,
    "IQ4_NL": 4.25,
    "IQ3_M": 3.30,
    "IQ2_M": 2.50,
}

# Standard bytes per element for KV cache quantization formats
KV_BYTES_MAP: Dict[str, float] = {
    "fp16": 2.0,
    "bf16": 2.0,
    "q8_0": 1.0625,  # 8.5 bits / 8
    "q4_0": 0.5625,  # 4.5 bits / 8
    "q4_1": 0.625,
}

GPU_TIERS_GIB: Dict[str, float] = {
    "16GB": 15.5,
    "24GB": 23.5,
    "48GB": 47.0,
    "96GB": 94.0,
}


def calculate_weight_bytes(total_params: float, quant: str) -> float:
    """Calculate VRAM resident weight size in bytes.

    For MoE models, total_params (not active_params) determines VRAM footprint.
    """
    bits_per_weight = QUANT_BITS_MAP.get(quant.upper(), 4.5)
    return total_params * (bits_per_weight / 8.0)


def calculate_kv_cache_bytes(
    num_layers: int,
    num_kv_heads: int,
    head_dim: int,
    context_length: int,
    kv_quant: str = "q8_0",
    architecture_type: str = "dense",
) -> float:
    """Calculate KV cache size in bytes.

    Formula:
        KV_bytes = 2 (Key + Value) * num_layers * num_kv_heads * head_dim * context_length * bytes_per_elem
    For hybrid Mamba models:
        Linear recurrent state is constant O(1) in sequence length, replacing attention KV cache
        for state-space layers, yielding sub-quadratic footprint.
    """
    bytes_per_elem = KV_BYTES_MAP.get(kv_quant.lower(), 1.0625)
    if architecture_type == "mamba_hybrid":
        # Hybrid models mix Mamba-2 SSM with a fraction of attention layers (e.g. 1/4 or 1/6)
        # Plus recurrent state memory (~1.5 GB fixed)
        effective_attn_layers = max(1, num_layers // 4)
        attn_kv = 2 * effective_attn_layers * num_kv_heads * head_dim * context_length * bytes_per_elem
        ssm_state = 1.5 * (1024**3)  # Fixed state cache
        return attn_kv + ssm_state

    return 2 * num_layers * num_kv_heads * head_dim * context_length * bytes_per_elem


def classify_placement(peak_vram_gib: float, gpu_capacity_gib: float) -> str:
    """Classify model placement on a target GPU."""
    if peak_vram_gib <= gpu_capacity_gib:
        return "full_vram_fit"
    elif peak_vram_gib <= gpu_capacity_gib * 1.5:
        return "partial_cpu_offload"
    else:
        return "out_of_memory"


def evaluate_model_vram(
    total_params: float,
    active_params: float,
    num_layers: int,
    num_kv_heads: int,
    head_dim: int,
    quant: str = "Q4_K_S",
    kv_quant: str = "q8_0",
    context_points: Optional[List[int]] = None,
    architecture_type: str = "dense",
    activation_overhead_gib: float = 1.0,
) -> Dict[str, Any]:
    """Perform a full VRAM and context scaling evaluation."""
    if context_points is None:
        context_points = [4096, 32768, 98304, 131072]

    weight_bytes = calculate_weight_bytes(total_params, quant)
    weight_gib = weight_bytes / (1024**3)

    context_results = []
    for ctx in context_points:
        kv_bytes = calculate_kv_cache_bytes(
            num_layers=num_layers,
            num_kv_heads=num_kv_heads,
            head_dim=head_dim,
            context_length=ctx,
            kv_quant=kv_quant,
            architecture_type=architecture_type,
        )
        kv_gib = kv_bytes / (1024**3)
        peak_vram_gib = weight_gib + kv_gib + activation_overhead_gib

        tier_placements = {
            tier: classify_placement(peak_vram_gib, cap)
            for tier, cap in GPU_TIERS_GIB.items()
        }

        context_results.append({
            "context_length": ctx,
            "kv_cache_bytes": kv_bytes,
            "kv_cache_gib": round(kv_gib, 3),
            "peak_vram_gib": round(peak_vram_gib, 3),
            "placements": tier_placements,
            "fits_24gb": tier_placements["24GB"] == "full_vram_fit",
        })

    return {
        "model_architecture": {
            "type": architecture_type,
            "total_params": total_params,
            "active_params": active_params,
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "head_dim": head_dim,
            "weight_quant": quant,
            "kv_quant": kv_quant,
        },
        "weights_gib": round(weight_gib, 3),
        "activation_overhead_gib": activation_overhead_gib,
        "context_evaluation": context_results,
    }
