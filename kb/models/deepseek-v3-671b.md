---
id: LLM-KB-MODELS-DEEPSEEK-V3-671B
title: "DeepSeek V3 671B MoE model architecture and local deployment record"
category: models
tags: [models, deepseek_v3, moe, mla, multi_gpu, tensor_parallel]
status: active
created: 2026-08-25
updated: 2026-08-29
environment:
  os: linux, windows
  shell: bash
  tools: [llama.cpp, sglang, unsloth]
error_signatures: []
---

# DeepSeek V3 (671B MoE)

DeepSeek V3 is described in the existing model record as a 671-billion parameter sparse Mixture-of-Experts (MoE) model with 37 billion active parameters per token, utilizing Multi-Head Latent Attention (MLA) and DeepSeekMoE architecture with auxiliary-loss-free load balancing.

Model identity and architecture figures are documented/report-based; deployment figures below are bounded observations from the [DeepSeek V3 sharding receipt](../receipts/deepseek-v3-671b-sharding-receipt.md) and originating [Issue #77](https://github.com/ozand/localllm-kb/issues/77). They are not universal fit or performance guarantees.

## Architecture

- **Total parameters:** 671.0 billion; **active parameters:** 37.0 billion. These are model-architecture figures, not resident-weight or throughput figures.
- **Layers:** 61.
- **Routed experts:** 256, with top-8 active per token.
- **Shared experts:** 1, reported as always active.
- **Attention:** Multi-Head Latent Attention (MLA) with 128 heads and 512 latent dimension.
- **Native context window:** 131,072 tokens as reported; runtime support, usable context, KV-cache type, and client limits are `unknown` here.

## Deployment Paradigms

1. **Reported 8x RTX 3090/4090 scenario (192GB nominal VRAM):**
   - Quantization: `UD-Q2_K_XS` (reported 206.06 GB file footprint); the exact artifact filename, revision, checksum, runtime allocation, and host-memory behavior are `unknown` here.
   - Partial CPU/RAM offload of a reported 14–16 GB on host DDR5 is setup-specific, not a universal requirement.
   - **Expected speed:** reported ~12–15 tokens/sec. Runtime/version, exact GPU, interconnect, context/KV settings, workload, concurrency, layer placement, and measurement method are `unknown`; treat this as bounded evidence, not a benchmark baseline.
2. **Reported 4x A100/H100 80GB scenario (320GB nominal VRAM):**
   - Quantization: `Q3_K_M` (reported 297.28 GB file footprint). The statement that it fits entirely in VRAM depends on artifact metadata, runtime overhead, KV cache, and allocation; those conditions are `unknown` here.
   - **Expected speed:** reported ~25–32 tokens/sec. Runtime/version, exact accelerator, interconnect, context, workload, concurrency, and measurement method are `unknown`.
3. **Reported consumer CPU/NVMe layer-offload scenario (1x 24GB GPU + 256GB RAM):**
   - Quantization: `UD-Q2_K_XS` via llama.cpp `--mmap` with 8 GPU-offloaded layers; exact artifact, runtime/version, storage, CPU, context, workload, and placement are `unknown`.
   - **Expected speed:** reported ~2.1 tokens/sec. This is a bounded observation, not a general CPU/NVMe expectation.

**Evidence status:** `reported_community_reproducible` for the linked receipt's bounded deployment record, with incomplete claim-level conditions on this page. File footprint, nominal VRAM, usable runtime memory, and generated-token speed must not be conflated.
