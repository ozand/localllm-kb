# OpenAI gpt-oss-20b — Deep Practical Local Research Receipt

- Date: 2026-08-23
- Model: OpenAI gpt-oss-20b (MoE reasoning model)
- Scope: Native MXFP4 weights, MoE sparse activation (21B total / 3.6B active), low/medium/high reasoning effort distinction, and 98K context memory scaling

## 1. Architecture & MoE Parameters
- **Architecture**: Sparse Mixture-of-Experts (`gpt-oss`).
- **Parameters**: 21B total parameters, only **3.6B active parameters** per token.
- **Layers & Heads**: 40 layers, 32 attention heads, **4 KV heads**, head dimension 128, 32 total experts (4 active per token).
- **Native Precision**: Built natively with MXFP4 quantization.
- **Context Window**: 131,072 native context tokens.

## 2. Quantization Matrix
- Original safetensors (MXFP4): 27.52 GB
- GGUF quants (Unsloth):
  * F16: 13.79 GB
  * Q8_0: 12.11 GB
  * Q6_K: 12.04 GB
  * Q5_K_M: 11.72 GB
  * Q4_K_M: 11.62 GB
  * Q4_K_S: 11.62 GB (exact standard artifact available)
  * Q3_K_M: 11.51 GB
  * Q2_K: 11.47 GB

## 3. Hardware Deployments & 98K Memory Limit
- **Single RTX 3090 / 3090 Ti 24GB**:
  * Q4_K_S base weights: **11.62 GB** (leaves **12.38 GB free VRAM** on a 24GB card!).
  * Text generation speed: **~65.4 tok/s** (exceptionally high speed due to only 3.6B active parameters).
  * **Reasoning Effort Levels**:
    * `low`: fast single-pass or minimal reasoning (~65 TPS).
    * `medium`: balanced reasoning steps.
    * `high`: deep reasoning chains (2x-4x total tokens).
  * **98,304 tokens with Q8 KV**: 4 KV heads & 40 layers require only **4.02 GB KV cache** -> **15.64 GB total VRAM (FITS easily on single 24GB GPU with 8.36 GB headroom!)**.
- **RTX 4090 24GB**:
  * Runs Q4_K_S / Q5_K_M at **~82.0 tok/s**.

## 4. Evidence Classification
- Model architecture and weights: `reported_official` / Hugging Face tree API.
- Hardware measurements: `reported_community_reproducible` (llama.cpp community logs).
- 98K KV scaling: `estimated` based on exact architecture parameters.
