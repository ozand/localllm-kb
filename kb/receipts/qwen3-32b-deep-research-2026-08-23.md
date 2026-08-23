# Qwen3 32B Instruct — Deep Practical Local Research Receipt

- Date: 2026-08-23
- Model: Qwen3 32B Instruct
- Scope: Deep local hardware, quantization, memory scaling, and runtime analysis

## 1. Quantization Matrix
- Official Weights (safetensors): 65.52 GB (dense 32.76B parameters)
- GGUF quants verified from Unsloth repository:
  * Q8_0: 34.82 GB
  * Q6_K: 26.88 GB
  * Q5_K_M: 23.21 GB
  * Q4_K_M: 19.76 GB
  * Q4_K_S: 18.77 GB (exact standard Q4_K_S artifact available)
  * Q3_K_M: 15.97 GB
  * Q2_K: 12.34 GB

## 2. Hardware Deployments & Practical Limits
- **Single RTX 3090 / 3090 Ti 24GB**:
  * Weights (Q4_K_S): 18.77 GB
  * Short context (4K-8K): ~20-21 GB VRAM -> Fits on single 24GB GPU (~22-25 tok/s generation).
  * Medium context (16K): ~23 GB VRAM -> Very tight fit, close to OOM.
  * 32K context with Q8 KV: 24.2 GB -> OOM on 24GB without offloading layers.
  * 32K context with Q4_0 KV: 22.4 GB -> Fits with ~1.5 GB headroom.
- **Dual RTX 3090 (48GB total)**:
  * Full GPU fit for Q6_K / Q8_0 with deep context (up to 131K YARN max).
  * Reported throughput: ~40-45 tok/s tensor parallel.
- **Single RTX 4090 24GB**:
  * Higher memory bandwidth (1008 GB/s) yields ~32-35 tok/s with AWQ/Q4_K_M in vLLM.
- **Apple Silicon (M3/M4 Max 64GB/128GB)**:
  * Unified memory easily fits Q4_K_M or Q8_0 with 64K-128K context (~28 tok/s).

## 3. Context & KV Cache Scaling (Target: 98,304 tokens)
- Architecture KV heads: 8 KV heads, head dim 128, 64 layers.
- KV Cache per token (Q8): 131,072 bytes (128 KB).
- At 98,304 tokens:
  * Q8 KV Cache = 12.88 GB
  * Q4 KV Cache = 6.44 GB
  * Total VRAM with Q4_K_S (Q8 KV) = 18.77 + 12.88 = 31.65 GB -> **OOM on single 24GB GPU**.
  * Total VRAM with Q4_K_S (Q4 KV) = 18.77 + 6.44 = 25.21 GB -> **OOM on single 24GB GPU**.
- **Conclusion**: Qwen3 32B dense at 98K context cannot run fully on a single 24GB GPU even with Q4 KV cache; requires minimum 32GB workstation GPU or dual 24GB setup.

## 4. Evidence Classification
- Weights and GGUF sizes: `reported_official` / Hugging Face tree API
- Hardware throughput and VRAM limits: `reported_community_reproducible` (Reddit, vLLM community benchmarks)
- KV Cache exact formula & 98K projections: `estimated` based on exact architecture parameters.
