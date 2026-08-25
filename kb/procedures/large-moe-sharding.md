---
id: LLM-KB-PROCEDURES-LARGE-MOE-SHARDING
title: "Large MoE multi-GPU sharding and memory offload runbook"
category: procedures
tags: [procedures, moe, sharding, multi_gpu, deepseek_v3, tensor_parallel]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, windows
  shell: bash
  tools: [llama.cpp, sglang, unsloth]
error_signatures:
  - "CUDA out of memory during expert routing"
  - "PCIe bandwidth bottleneck on all-to-all reduce"
---

# Large MoE Multi-GPU Sharding & Memory Offload

Runbook for deploying extreme-scale Mixture-of-Experts models (DeepSeek V3 671B,
DeepSeek V4 Pro, Mixtral 8x22B) across multi-GPU workstations and CPU/NVMe offload hosts.

## 1. Multi-GPU Tensor Sharding (8x RTX 3090/4090)

When sharding 671B MoE across 8x 24GB GPUs (192GB Total VRAM):
- Target Quantization: `UD-Q2_K_XS` (206 GB total file footprint).
- Command:
  ```bash
  llama-server     --model models/DeepSeek-V3-UD-Q2_K_XS     --tensor-split 24,24,24,24,24,24,24,24     --n-gpu-layers 58     --ctx-size 16384     --flash-attn
  ```
- Performance: ~12-15 tokens/sec with PCIe Gen4 interconnect.

## 2. Enterprise Cluster Deployment (4x / 8x A100/H100 80GB)

For enterprise nodes with NVLink / NVSwitch:
- Target Quantization: `Q3_K_M` (297.28 GB) or `FP8` (671 GB).
- Use Tensor Parallelism (TP=8) or Pipeline Parallelism (PP=4, TP=2) to balance latency and throughput.

## 3. CPU/NVMe Memory-Mapped Execution

On single-GPU workstations with 256GB DDR5 RAM:
- Command:
  ```bash
  llama-server     --model models/DeepSeek-V3-UD-Q2_K_XS     --n-gpu-layers 8     --ctx-size 8192     --mmap     --threads 16
  ```
- Latency: ~1.8-2.5 tokens/sec.
