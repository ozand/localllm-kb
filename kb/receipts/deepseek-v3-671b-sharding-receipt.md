---
id: LLM-KB-RECEIPTS-DEEPSEEK-V3-671B-SHARDING
title: "DeepSeek V3 671B MoE multi-GPU sharding and memory offload validation receipt"
category: receipts
tags: [receipts, deepseek_v3, moe, sharding, multi_gpu]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, windows
  shell: bash
  tools: [llama.cpp, sglang, unsloth]
error_signatures: []
---

# DeepSeek V3 671B MoE Sharding Validation Receipt

## Summary
- Model: DeepSeek V3 (671B total / 37B active MoE)
- Upstream: deepseek-ai/DeepSeek-V3
- Quantization Matrix: UD-Q2_K_XS (206.06 GB), Q3_K_M (297.28 GB), Q4_K_M (376.65 GB), Q8_0 (664.30 GB)
- Target Cluster: 8x RTX 3090/4090 (192GB VRAM + Host DDR5) or 4x A100 80GB (320GB VRAM)
- Evidence Status: `reported_community_reproducible`
