---
id: LLM-KB-PROC-DYNAMIC-QUANTS
title: "Unsloth dynamic quantization methodology and verification"
category: procedures
tags: [quantization, dynamic_quants, unsloth, gguf, perplexity]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, windows
  shell: bash
  tools: [unsloth, llama.cpp]
error_signatures:
  - "UD quant artifact treated as standard GGUF"
  - "Perplexity explosion on uniform 3-bit"
---

# Dynamic Quantization Methodology

## 1. Concept and Differentiation

Standard GGUF quantizations (`Q4_K_S`, `Q4_K_M`, `Q5_K_M`, `Q8_0`) apply uniform quantization
rules across layers with fixed k-quant assignments.

Unsloth Dynamic Quantization (`UD-*`, `Dynamic 2.0`) uses importance-driven layer sensitivity
analysis:
1. **Calibration Corpus**: Evaluates 300K to 1.5M high-quality tokens to compute layer-wise
   gradient and activation norms.
2. **Selective Bit Allocation**: Assigns higher precision (e.g. 5-bit/6-bit/8-bit) to the most
   sensitive layers (such as first/last transformer blocks, down-projections, and self-attention heads)
   and lower precision (3-bit/4-bit) to redundant MLP/MoE expert weights.
3. **Artifact Identification**: Dynamic quantizations are denoted with `UD-` prefix
   (e.g., `UD-Q4_K_S`, `UD-Q4_K_M`, `UD-Q2_K_XL`).

## 2. Decision Matrix: Standard GGUF vs Dynamic Quants

- **When to choose Standard GGUF (Bartowski/Upstream)**:
  - Strict compliance testing against reference upstream quants.
  - Verification of pure baseline performance.
- **When to choose Dynamic Quants (Unsloth UD-*)**:
  - Memory-constrained local deployments where a standard Q4 exceeds VRAM (e.g., Qwen3.8 27B, Nemotron 3.5, DeepSeek R1).
  - Maximizing reasoning and conversational MMLU score per gigabyte of VRAM.

## Related Records

- [Unsloth Runtime](../runtimes/unsloth.md)
- [Qwen3.8 27B](../models/qwen3.8-27b.md)
- [NVIDIA Nemotron 3.5](../models/nemotron-3.5-lightning.md)
- [Model Artifact Lifecycle](model-artifact-lifecycle.md)
