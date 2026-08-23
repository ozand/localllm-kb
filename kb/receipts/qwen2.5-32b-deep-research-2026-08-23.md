# Qwen2.5 32B Instruct — Deep Practical Local Research Receipt

- Date: 2026-08-23
- Model: Qwen2.5 32B Instruct
- Scope: Dense 32.5B parameter baseline, Bartowski GGUF quants, single vs dual 3090 scaling, 98K context comparison with Qwen3

## 1. Architecture Identity
- **Architecture**: Dense Transformer (`qwen2.5`).
- **Layers & Heads**: 64 layers, 40 attention heads, 8 KV heads (`head_dimension: null` without speculative inference).
- **Context Window**: 32,768 config native, 131,072 extended via YARN/RoPE.

## 2. Quantization Matrix
- Original safetensors: 65.53 GB
- GGUF quants (Bartowski):
  * F16: 65.54 GB (2 parts)
  * Q8_0: 34.82 GB
  * Q6_K: 26.89 GB
  * Q5_K_M: 23.26 GB
  * Q4_K_M: 19.85 GB
  * Q4_K_S: 18.78 GB (exact standard artifact available)
  * IQ4_XS: 17.69 GB
  * Q3_K_M: 15.94 GB
  * Q2_K: 12.31 GB

## 3. Hardware Deployments & 98K Memory Limit
- **Single RTX 3090 / 3090 Ti 24GB**:
  * Q4_K_S weights = 18.78 GB
  * Up to 16k context: ~20.9 GB (fits with ~3.1 GB buffer).
  * 32k context with Q8 KV = 23.0 GB (very tight, near OOM).
  * 98,304 tokens with Q8 KV = 12.88 GB cache -> **31.66 GB total VRAM (OOM on 24GB)**.
  * 98,304 tokens with Q4 KV = 6.44 GB cache -> **25.22 GB total VRAM (OOM on 24GB)**.
  * Yields **~24.5 tok/s** generation.
- **Dual RTX 3090 (2x24GB = 48GB)**:
  * Allows running Q5_K_M or Q6_K with full 131k context at **~44 tok/s**.

## 4. Evidence Classification
- Weights and GGUF files: `reported_official` / Hugging Face tree API.
- Hardware measurements: `reported_community_reproducible` (llama.cpp community logs).
- 98K KV scaling: `estimated` based on exact architecture parameters (8 KV heads, 64 layers).
