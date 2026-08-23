# Mistral Small 3.1 24B Instruct — Deep Practical Local Research Receipt

- Date: 2026-08-23
- Model: Mistral Small 3.1 24B Instruct (2503)
- Scope: 24B dense multimodal architecture, Unsloth GGUF quantization matrix, mmproj vision projector overhead, and 98K context memory scaling

## 1. Architecture & Multimodal Boundary
- **Architecture**: Dense Transformer (`mistral3`) with native vision support.
- **Layers & Heads**: 56 layers, 32 attention heads, 8 KV heads, head dimension 128.
- **Context Window**: 131,072 native context tokens.
- **Multimodal Projector**: Separate `mmproj-BF16.gguf` (878.0 MB) required for image input; pure text GGUF runs independently.

## 2. Quantization Matrix
- Original safetensors: 48.02 GB
- GGUF quants (Unsloth):
  * BF16: 47.15 GB
  * Q8_0: 25.05 GB
  * Q6_K: 19.35 GB
  * Q5_K_M: 16.76 GB
  * Q4_K_M: 14.33 GB
  * Q4_K_S: 13.55 GB (exact standard artifact available)
  * Q3_K_M: 11.47 GB
  * Q2_K: 8.89 GB
  * mmproj-BF16: 878.0 MB

## 3. Hardware Deployments & 98K Memory Limit
- **Single RTX 3090 / 3090 Ti 24GB**:
  * Q4_K_S base weights: **13.55 GB** (leaves **10.45 GB free VRAM** on a 24GB card).
  * Text generation speed: **~33.2 tok/s** (fastest dense model in the 24-32B class).
  * **98,304 tokens with Q8 KV**: 8 KV heads & 56 layers require **11.27 GB KV cache** -> **24.82 GB total VRAM (borderline OOM)**.
  * **98,304 tokens with Q4 KV**: **5.63 GB KV cache** -> **19.18 GB total VRAM (FITS comfortably with 4.8 GB headroom!)**.
- **RTX 4090 24GB**:
  * Runs Q4_K_M / Q5_K_M at **~42.5 tok/s**.

## 4. Evidence Classification
- Model architecture and weights: `reported_official` / Hugging Face tree API.
- Hardware measurements: `reported_community_reproducible` (llama.cpp community logs).
- 98K KV scaling: `estimated` based on exact architecture parameters.
