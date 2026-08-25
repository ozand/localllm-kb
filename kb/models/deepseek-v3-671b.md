---
id: LLM-KB-MODELS-DEEPSEEK-V3-671B
title: "DeepSeek V3 671B MoE model architecture and local deployment record"
category: models
tags: [models, deepseek_v3, moe, mla, multi_gpu, tensor_parallel]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, windows
  shell: bash
  tools: [llama.cpp, sglang, unsloth]
error_signatures: []
---

# DeepSeek V3 (671B MoE)

DeepSeek V3 is a 671-billion parameter sparse Mixture-of-Experts (MoE) model with
37 billion active parameters per token, utilizing Multi-Head Latent Attention (MLA)
and DeepSeekMoE architecture with auxiliary-loss-free load balancing.

## Architecture

- **Total Parameters**: 671.0 Billion
- **Active Parameters**: 37.0 Billion
- **Layers**: 61
- **Routed Experts**: 256 (Top-8 active per token)
- **Shared Experts**: 1 (always active)
- **Attention**: Multi-Head Latent Attention (MLA) with 128 heads and 512 latent dimension
- **Native Context Window**: 131,072 tokens

## Deployment Paradigms

1. **8x RTX 3090/4090 (192GB VRAM)**:
   - Quantization: `UD-Q2_K_XS` (206.06 GB) requires partial CPU/RAM offload (14-16 GB on host DDR5).
   - Expected Speed: ~12-15 tokens/sec.
2. **4x A100 / H100 80GB (320GB VRAM)**:
   - Quantization: `Q3_K_M` (297.28 GB) fits entirely in VRAM.
   - Expected Speed: ~25-32 tokens/sec.
3. **Consumer CPU/NVMe Layer Offload (1x 24GB GPU + 256GB RAM)**:
   - Quantization: `UD-Q2_K_XS` via llama.cpp `--mmap` and 8 GPU offloaded layers.
   - Expected Speed: ~2.1 tokens/sec.
