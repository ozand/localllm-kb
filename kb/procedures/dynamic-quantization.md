---
id: LLM-KB-PROC-DYNAMIC-QUANTS
title: "Unsloth dynamic quantization methodology and verification"
category: procedures
tags: [quantization, dynamic_quants, unsloth, gguf, perplexity]
status: active
created: 2026-08-25
updated: 2026-08-29
environment:
  os: linux, windows
  shell: bash
  tools: [unsloth, llama.cpp]
error_signatures:
  - "UD quant artifact treated as standard GGUF"
  - "Perplexity explosion on uniform 3-bit"
---

# Dynamic Quantization Methodology

The procedure below describes the distinction and selection rationale for Unsloth Dynamic Quantization. Evidence status for numeric and quality/performance statements is `reported_community_partial` or `unknown` unless a cited artifact-specific receipt supplies matching conditions. It is not a universal quantization recipe or quality guarantee.

## 1. Concept and Differentiation

Standard GGUF quantizations (`Q4_K_S`, `Q4_K_M`, `Q5_K_M`, `Q8_0`) apply uniform quantization
rules across layers with fixed k-quant assignments.

Unsloth Dynamic Quantization (`UD-*`, `Dynamic 2.0`) uses importance-driven layer sensitivity
analysis:
1. **Calibration corpus:** The existing guidance reports a range of `300K–1.5M` tokens for computing layer-wise gradient and activation norms. Corpus composition, calibration method, model/artifact revision, quantization implementation, runtime, and validation metric are `unknown` here; this is not a universal token requirement.
2. **Selective bit allocation:** The documented concept assigns higher precision (examples: 5-bit/6-bit/8-bit) to more sensitive layers and lower precision (examples: 3-bit/4-bit) to less sensitive weights. Exact layer selection, thresholds, model architecture, and resulting quality are artifact- and implementation-specific and remain `unknown` unless recorded by a matching receipt.
3. **Artifact Identification**: Dynamic quantizations are denoted with `UD-` prefix
   (e.g., `UD-Q4_K_S`, `UD-Q4_K_M`, `UD-Q2_K_XL`).

## 2. Decision Matrix: Standard GGUF vs Dynamic Quants

- **When to choose Standard GGUF (Bartowski/Upstream)**:
  - Strict compliance testing against reference upstream quants.
  - Verification of pure baseline performance.
- **When to consider Dynamic Quants (Unsloth UD-*):**
  - Memory-constrained local deployments where a particular standard artifact does not fit the available runtime memory. The cited model examples are not fit guarantees; exact artifact size, runtime overhead, KV-cache settings, hardware, context, and workload are `unknown` unless measured.
  - Comparing quality or capability per unit of memory may be useful, but the earlier “maximizing reasoning and conversational MMLU score per gigabyte” wording is not a verified universal result. Baseline artifact, evaluation set, metric, runtime, and measurement method are `unknown`.

**Evidence status:** `reported_community_partial` / documented terminology. File footprint, runtime memory, quality metrics, and performance must be recorded separately; no compression ratio, VRAM saving, perplexity, MMLU score, or speedup is asserted by this procedure.

## Related Records

- [Unsloth Runtime](../runtimes/unsloth.md)
- [Qwen3.8 27B](../models/qwen3.8-27b.md)
- [NVIDIA Nemotron 3.5](../models/nemotron-3.5-lightning.md)
- [Model Artifact Lifecycle](model-artifact-lifecycle.md)
