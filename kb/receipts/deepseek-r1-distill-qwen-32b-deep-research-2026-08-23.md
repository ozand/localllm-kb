# DeepSeek R1 Distill Qwen 32B — Deep Practical Local Research Receipt

- Date: 2026-08-23
- Model: DeepSeek R1 Distill Qwen 32B
- Scope: Reasoning model based on Qwen2.5 32B backbone, Bartowski GGUF quants, thinking token latency, 98K context memory limit

## 1. Architecture & Reasoning Identity
- **Architecture**: Dense Transformer reasoning model (`deepseek-r1-distill-qwen` on `qwen2.5` base).
- **Layers & Heads**: 64 layers, 40 attention heads, 8 KV heads (`head_dimension: null` without speculative inference).
- **Context Window**: 32,768 config native, 131,072 extended via YARN/RoPE.
- **Reasoning Behavior**: Generates extensive `<think>...</think>` tokens before final response; raw token generation is ~24 tok/s, but wall-clock latency per question is 2x-5x higher than non-reasoning models.

## 2. Quantization Matrix
- Original safetensors: 65.53 GB
- GGUF quants (Bartowski):
  * BF16: 65.54 GB (2 parts)
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
  * Short context (up to 16k): ~20.9 GB VRAM, solid fit with ~23.8 tok/s generation.
  * 98,304 tokens with Q8 KV = 12.88 GB cache -> **31.66 GB total VRAM (OOM on 24GB)**.
  * 98,304 tokens with Q4 KV = 6.44 GB cache -> **25.22 GB total VRAM (OOM on 24GB)**.
- **Dual RTX 3090 (2x24GB = 48GB)**:
  * Allows running Q5_K_M / Q6_K with full long context reasoning chains at **~43.5 tok/s**.

## 4. Evidence Classification
- Weights and GGUF files: `reported_official` / Hugging Face tree API.
- Hardware measurements: `reported_community_reproducible` (llama.cpp community logs).
- 98K KV scaling: `estimated` based on exact architecture parameters.
