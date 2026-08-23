# Qwen3 Coder 30B A3B Instruct — Deep Practical Local Research Receipt

- Date: 2026-08-23
- Model: Qwen3 Coder 30B A3B Instruct
- Scope: Dedicated coding agent deployment, MoE total vs active parameters, native 262k context scaling

## 1. Coder Architecture & Thinking Distinction
- **Specialization**: Strict coding agent optimization (`non-thinking-only`).
- **Parameters**: 30.5B total / 3.3B active (8 of 128 experts).
- **Native Context Window**: 262,144 tokens.

## 2. Quantization Matrix
- Original safetensors: 61.07 GB
- GGUF verified quants:
  * Q8_0: 32.48 GB
  * Q6_K: 25.09 GB
  * Q5_K_M: 21.73 GB
  * Q4_K_M: 18.56 GB
  * Q4_K_S: 17.46 GB (exact standard artifact available)
  * IQ4_XS: 16.38 GB
  * Q3_K_M: 14.71 GB
  * Q2_K: 11.26 GB

## 3. Hardware Deployments & 98K Context Fit
- **Single RTX 3090 / 3090 Ti 24GB**:
  * Q4_K_S weights (17.46 GB) + 98,304 token Q8 KV cache (4.83 GB) = **22.29 GB VRAM**
  * **FITS on 1x 24GB GPU** with ~1.7 GB safety buffer.
  * Yields **~58 tok/s** streaming generation, ideal for real-time IDE agents.
- **Dual RTX 3090 48GB**:
  * Allows running Q8_0 quant (32.48 GB) with full 262K context (~82 tok/s).

## 4. Evidence Classification
- Weights and GGUF files: `reported_official` / Hugging Face tree API.
- Hardware measurements: `reported_community_reproducible` (llama.cpp / Cline community logs).
- 98K KV scaling: `estimated` based on exact architecture parameters (4 KV heads, 48 layers).
