---
id: LLM-KB-PROCEDURES-LARGE-MOE-SHARDING
title: "Large MoE multi-GPU sharding and memory offload runbook"
category: procedures
tags: [procedures, moe, sharding, multi_gpu, deepseek_v3, tensor_parallel]
status: active
created: 2026-08-25
updated: 2026-08-29
environment:
  os: linux, windows
  shell: bash
  tools: [llama.cpp, sglang, unsloth]
error_signatures:
  - "CUDA out of memory during expert routing"
  - "PCIe bandwidth bottleneck on all-to-all reduce"
---

# Large MoE Multi-GPU Sharding & Memory Offload

Runbook for a possible deployment pattern for extreme-scale Mixture-of-Experts models. The cited evidence is model- and environment-specific; DeepSeek V3, DeepSeek V4 Pro, and Mixtral 8x22B are not interchangeable evidence subjects. See the [DeepSeek V3 sharding receipt](../receipts/deepseek-v3-671b-sharding-receipt.md) and originating [Issue #77](https://github.com/ozand/localllm-kb/issues/77).

## 1. Multi-GPU Tensor Sharding (8x RTX 3090/4090)

For the reported DeepSeek V3 scenario using 8x 24GB GPUs (192GB nominal VRAM):
- **Evidence status:** `reported_community_reproducible` for the linked receipt's bounded setup; not a universal fit or performance guarantee.
- Target quantization: `UD-Q2_K_XS` (reported 206 GB total file footprint; exact artifact revision, filename, checksum, and runtime allocation are `unknown` here).
- The 192GB VRAM total and 206GB file footprint are different quantities; successful placement requires runtime-specific offload/overhead handling and is not implied by arithmetic alone.
- Command:
  ```bash
  llama-server     --model models/DeepSeek-V3-UD-Q2_K_XS     --tensor-split 24,24,24,24,24,24,24,24     --n-gpu-layers 58     --ctx-size 16384     --flash-attn
  ```
- Performance: reported ~12–15 tokens/sec with PCIe Gen4 interconnect. Model revision, exact artifact, runtime/version, GPU model, context, workload, concurrency, layer placement, and measurement method are `unknown` in this procedure; treat the figure as bounded reported evidence, not a baseline.
## 2. Enterprise Cluster Deployment (4x / 8x A100/H100 80GB)

For enterprise nodes with NVLink / NVSwitch, the following are deployment examples rather than universal requirements:
- Target quantization examples: `Q3_K_M` (reported 297.28 GB) or `FP8` (reported 671 GB). Exact artifact, revision, metadata overhead, runtime, and usable memory are `unknown`.
- Tensor Parallelism (TP=8) or Pipeline Parallelism (PP=4, TP=2) may be used to balance latency and throughput. The suitable split, throughput, and latency are workload- and runtime-specific and remain `unknown` without a matched measurement.

## 3. CPU/NVMe Memory-Mapped Execution

For a reported single-GPU workstation with 256GB DDR5 RAM, CPU/NVMe memory-mapped execution is an offload example, not a guaranteed operating mode:
- **Evidence status:** `reported_community_partial`; CPU, storage, PCIe, model/artifact, runtime/version, context, workload, and measurement method are otherwise `unknown`.
- Command:
  ```bash
  llama-server     --model models/DeepSeek-V3-UD-Q2_K_XS     --n-gpu-layers 8     --ctx-size 8192     --mmap     --threads 16
  ```
- Latency: reported ~1.8–2.5 tokens/sec. This is a bounded observation, not a general CPU/NVMe performance expectation; the exact conditions are `unknown`.