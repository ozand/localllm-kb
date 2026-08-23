# Gemma 3 27B Instruct — Deep Practical Local Research Receipt

- Date: 2026-08-23
- Model: Gemma 3 27B Instruct
- Scope: Dense multimodal architecture, Unsloth GGUF quantization matrix, mmproj vision projector overhead, and 98K context memory scaling

## 1. Architecture & Multimodal Boundary
- **Architecture**: Dense Transformer with native multimodal vision integration (`gemma-3`).
- **Layers & Heads**: 62 layers, 32 attention heads, 16 KV heads, head dimension 128.
- **Context Window**: 131,072 native context tokens.
- **Vision Resolution**: 896x896 images mapped to 256 tokens per image.
- **Multimodal Projector**: Separate `mmproj-BF16.gguf` (857.7 MB) or `mmproj-F16.gguf` (857.7 MB) required for image input; pure text GGUF inference runs independently.

## 2. Quantization Matrix
- Original safetensors: 54.86 GB
- GGUF quants (Unsloth):
  * BF16: 54.03 GB (2 parts)
  * Q8_0: 28.71 GB
  * Q6_K: 22.17 GB
  * Q5_K_M: 19.27 GB
  * Q4_K_M: 16.55 GB
  * Q4_K_S: 15.67 GB (exact standard artifact available)
  * Q3_K_M: 13.44 GB
  * Q2_K: 10.50 GB
  * mmproj-BF16: 857.7 MB

## 3. Hardware Deployments & 98K Memory Limit
- **Single RTX 3090 / 3090 Ti 24GB**:
  * Q4_K_S weights = 15.67 GB
  * Short context (up to 16k): ~19.6 GB VRAM, ~28.5 tok/s text generation.
  * **98,304 tokens with Q8 KV**: 16 KV heads & 62 layers require **24.36 GB KV cache alone** -> **40.03 GB total VRAM (OOM on 24GB)**.
  * **98,304 tokens with Q4 KV**: 12.18 GB KV cache -> **27.85 GB total VRAM (OOM on 24GB)**.
- **Dual RTX 3090 (2x24GB = 48GB)**:
  * Comfortable execution of Q5_K_M / Q6_K with full long-context multimodal processing at **~48 tok/s**.

## 4. Evidence Classification
- Model architecture and weights: `reported_official` / Hugging Face tree API.
- Hardware measurements: `reported_community_reproducible` (llama.cpp community logs).
- 98K KV scaling: `estimated` based on exact architecture parameters.
