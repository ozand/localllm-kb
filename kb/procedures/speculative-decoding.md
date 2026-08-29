---
id: LLM-KB-PROC-SPECULATIVE-DECODING
title: "Speculative Decoding and Draft-Model Acceleration"
category: procedures
tags: [speculative_decoding, mtp, dflash, draft_models, latency_optimization]
status: active
created: 2026-08-25
updated: 2026-08-29
environment:
  os: linux, windows
  shell: bash, powershell
  tools: [llama.cpp, unsloth, sglang]
error_signatures:
  - "draft model token mismatch"
  - "speculative decoding slower than base generation"
---

# Speculative Decoding and Multi-Token Prediction (MTP) Runbook

## Overview

Speculative decoding leverages a smaller draft model or native multi-token prediction
(MTP) heads to propose $K$ candidate tokens per step, which the primary model
verifies in a single batched forward pass.

## 1. Native MTP Acceleration (Qwen3.8 / DeepSeek)

- Native MTP heads embedded in model weights predict next tokens directly without
  loading an external secondary model.
- **Evidence status:** capability is documented in the linked runtime sources; the numeric speedup range below is not independently verified for a canonical model/artifact/runtime/hardware combination.
- **Performance claim:** the stated `1.5x–2.2x` range is retained only as an illustrative, community-reported range. Model, artifact, runtime version, GPU, context, workload, baseline, and measurement method are `unknown` here; do not use it as a sizing or throughput guarantee.
- **Llama.cpp Flags**:
  ```bash
  llama-server -m model-UD-Q4_K_S.gguf --draft-mtp 1 --spec-draft-p-min 0.8
  ```

## 2. External Draft Models (DFlash / Small-Large Pairings)

- **Pairing Rule**: Draft model and target model must share an identical vocabulary
  and tokenizer (e.g. Qwen2.5-0.5B draft for Qwen2.5-32B).
- **GPU Placement**:
  - Single GPU: Keep draft model in GPU VRAM (adds ~0.5GB–1.5GB overhead).
  - Multi-GPU: Place draft model on GPU 0 or dedicated co-processor to avoid PCIe
    synchronization bottlenecks. These placement notes are operational hypotheses, not measurements in this knowledge base; validate them for the specific runtime, interconnect, model, and workload before relying on them.

See the [DFlash, MTP, and DSpark claim-verification receipt](../receipts/speculative-decoding-claim-verification-receipt.md) for the public evidence review and its limitations.

## 3. Performance Profiling

| Strategy | Base Model | Draft Engine | Single 3090 Baseline | Speculative Speed | Speedup |
|---|---|---|---|---|---|
| **Native MTP** | Qwen3.8 27B | Internal MTP Head | 30.0 tok/s | 60.0 tok/s | **2.0x** |
| **DFlash 2** | Qwen3.8 27B | DFlash-2 Draft | 30.0 tok/s | 65.2 tok/s | **2.17x** |
| **Small Draft** | Qwen2.5 32B | Qwen2.5 0.5B | 24.5 tok/s | 41.2 tok/s | **1.68x** |

> **Evidence status for this table:** illustrative/community-reported values only. The table has no attached artifact identity, immutable revision, runtime version, exact RTX 3090 configuration, context, workload, sampling settings, or measurement method. Issue #100 independently corroborated the existence of speculative-decoding methods and benchmark tooling, but promoted zero numeric claims to measured or reproducible performance facts. Treat every number above as `reported_community_partial`, not as a benchmark baseline.
