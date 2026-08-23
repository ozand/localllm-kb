# Qwen3 30B A3B Instruct — Deep Practical Local Research Receipt

- Date: 2026-08-23
- Model: Qwen3 30B A3B Instruct
- Scope: Deep local hardware, sparse MoE memory footprint, quantization matrix, and KV cache scaling

## 1. MoE Architecture & Memory Footprint Distinction
- **Total Parameters**: 30.5B (full weights must be resident in VRAM for GPU execution)
- **Active Parameters per token**: 3.3B (8 of 128 experts activated)
- **Compute vs Memory**: High token throughput (~55-75 tok/s) comparable to a 3B-4B model, but requires ~17.5 GB VRAM (Q4_K_S) to hold all 30.5B weights.
- **Important**: Active parameters do NOT reduce memory footprint.

## 2. Quantization Matrix
- Original safetensors: 61.59 GB
- GGUF verified quants:
  * Q8_0: 32.48 GB
  * Q6_K: 25.09 GB
  * Q5_K_M: 21.73 GB
  * Q4_K_M: 18.56 GB
  * Q4_K_S: 17.46 GB (exact standard artifact available)
  * IQ4_XS: 16.38 GB
  * Q3_K_M: 14.71 GB
  * Q2_K: 11.26 GB

## 3. Hardware Deployments & 98K Context Scaling
- **Single RTX 3090 / 3090 Ti 24GB**:
  * **Surprise Advantage over Dense**: 4 KV heads and 48 layers (compared to 8 KV heads and 64 layers in dense 32B).
  * KV cache at 98,304 tokens:
    - Q8 KV = 4.83 GB (vs 12.88 GB on dense 32B)
    - Q4 KV = 2.42 GB (vs 6.44 GB on dense 32B)
  * **Total VRAM at 98,304 tokens with Q4_K_S + Q8 KV**:
    - 17.46 GB (weights) + 4.83 GB (KV cache) = **22.29 GB VRAM**
    - **FITS on a single 24GB GPU** with ~1.7 GB headroom!
  * Generation speed: ~50-55 tok/s.
- **Dual RTX 3090 (48GB)**:
  * Runs Q8_0 (32.5GB) + full 131K context easily (~75-80 tok/s).

## 4. Evidence Classification
- Weights and GGUF sizes: `reported_official` / Hugging Face tree API.
- Hardware throughput: `reported_community_reproducible` (vLLM / llama.cpp MoE benchmarks).
- KV Cache exact formula & 98K projections: `estimated` based on exact architecture parameters.
