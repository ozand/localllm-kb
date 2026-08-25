import pytest
from kb_bootstrap.vram_calc import (
    calculate_weight_bytes,
    calculate_kv_cache_bytes,
    classify_placement,
    evaluate_model_vram,
)


def test_calculate_weight_bytes():
    # 32B model in Q4_K_S (4.35 bits / weight)
    bytes_val = calculate_weight_bytes(32.5e9, "Q4_K_S")
    gib_val = bytes_val / (1024**3)
    assert 16.0 < gib_val < 18.0


def test_calculate_kv_cache_bytes_dense():
    # Qwen3 32B: 64 layers, 8 KV heads, 128 head_dim, 98304 tokens, Q8 KV
    kv_bytes = calculate_kv_cache_bytes(
        num_layers=64,
        num_kv_heads=8,
        head_dim=128,
        context_length=98304,
        kv_quant="q8_0",
    )
    kv_gib = kv_bytes / (1024**3)
    # Expected ~12.88 GiB
    assert 12.0 < kv_gib < 14.0


def test_calculate_kv_cache_bytes_moe():
    # Qwen3 30B A3B: 48 layers, 4 KV heads, 128 head_dim, 98304 tokens, Q8 KV
    kv_bytes = calculate_kv_cache_bytes(
        num_layers=48,
        num_kv_heads=4,
        head_dim=128,
        context_length=98304,
        kv_quant="q8_0",
    )
    kv_gib = kv_bytes / (1024**3)
    # Expected ~4.83 GiB
    assert 4.5 < kv_gib < 5.2


def test_classify_placement():
    assert classify_placement(22.0, 23.5) == "full_vram_fit"
    assert classify_placement(30.0, 23.5) == "partial_cpu_offload"
    assert classify_placement(45.0, 23.5) == "out_of_memory"


def test_evaluate_model_vram_qwen3_30b_fits_24gb():
    res = evaluate_model_vram(
        total_params=30.5e9,
        active_params=3.3e9,
        num_layers=48,
        num_kv_heads=4,
        head_dim=128,
        quant="Q4_K_S",
        kv_quant="q8_0",
        context_points=[98304],
        architecture_type="moe",
    )
    ctx_98k = res["context_evaluation"][0]
    assert ctx_98k["fits_24gb"] is True
    assert ctx_98k["placements"]["24GB"] == "full_vram_fit"
    assert ctx_98k["peak_vram_gib"] < 23.5


def test_evaluate_model_vram_qwen3_32b_oom_24gb():
    res = evaluate_model_vram(
        total_params=32.5e9,
        active_params=32.5e9,
        num_layers=64,
        num_kv_heads=8,
        head_dim=128,
        quant="Q4_K_S",
        kv_quant="q8_0",
        context_points=[98304],
        architecture_type="dense",
    )
    ctx_98k = res["context_evaluation"][0]
    assert ctx_98k["fits_24gb"] is False
    assert ctx_98k["placements"]["24GB"] == "partial_cpu_offload" or ctx_98k["placements"]["24GB"] == "out_of_memory"
    assert ctx_98k["peak_vram_gib"] > 24.0
