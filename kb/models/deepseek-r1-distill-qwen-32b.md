---
id: M-DEEPSEEK-R1-DISTILL-QWEN-32B
title: "DeepSeek R1 Distill Qwen 32B Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "deepseek", "r1", "reasoning", "distill", "qwen", "32b", "dense", "gguf", "bartowski", "rtx3090ti"]
upstream_repo: "https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-32B-GGUF"
upstream_commit: "91d17d52a233b8fbca971842ba7cecfc8fe7ab41"
primary_artifact: "DeepSeek-R1-Distill-Qwen-32B-Q4_K_S.gguf"
provenance_status: "validated_metadata_bounded_runtime_evidence"
evidence_status: "reported_community_reproducible_and_estimated"
last_updated: "2026-08-29"
limitations: "Artifact metadata is reported upstream metadata; hardware throughput is reported community evidence; KV/VRAM matrices are estimates. Native versus extended context and architecture discrepancies are preserved explicitly."
---

# DeepSeek R1 Distill Qwen 32B Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

The base-model and GGUF identities below come from the existing import receipt. Artifact byte size and hash are reported upstream metadata, not a local recomputation. Architecture/context figures remain separated from runtime/client support and deployment estimates.

- **Model Identity**: DeepSeek R1 Distill Qwen 32B (`deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`)
- **Architecture**: Dense Transformer fine-tuned with DeepSeek R1 reasoning traces (32.5B parameters)
- **Base Precision**: BF16 / FP16
- **Layer and head count:** 64 layers and 8 KV heads are reported consistently; the existing records disagree on the attention-head count (`64` on this page versus `40` in the import/deep-research receipts), and head dimension is not locally verified. Preserve this discrepancy; do not infer a value.
- **Context limit:** the import/deep-research records distinguish `32,768` native configuration from `131,072` extended context via YaRN/RoPE. Runtime/client support and usable context remain `unknown` here.
- **Primary GGUF artifact:** `DeepSeek-R1-Distill-Qwen-32B-Q4_K_S.gguf`; reported upstream metadata is `18.78 GB / 18,784,409,760 bytes` at the cited GGUF revision. The page's previous `20,165,165,472`-byte value is not reconciled with that record; local verification is `unknown`.

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance

The following are bounded `reported_community_reproducible` observations from the linked deep-research receipt, not universal reference rates. Exact artifact, runtime/version, backend, hardware configuration, context, workload, concurrency, reasoning policy, output length, and measurement method are not fully recorded on this page and remain `unknown` where absent.

- **Single RTX 3090 / 3090 Ti (24GB):** reported ~23.8 tok/s raw token generation. The reported 2x–5x wall-clock completion overhead from reasoning tokens is workload- and policy-dependent, not a universal multiplier.
- **Dual RTX 3090 / 3090 Ti (2x24GB):** reported ~43.5 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB):** reported ~28.5 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (8 KV Heads, 64 Layers)

The matrix is an `estimated` architecture-based calculation, not a runtime allocation measurement. It assumes the listed quantization and KV-cache types; allocator overhead, runtime placement, prompt/reasoning tokens, backend behavior, and usable headroom are `unknown`. `FITS`, `TIGHT`, and `OOM` are estimates for the named nominal hardware, not guarantees across runtimes.

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~1.07 GB | ~0.54 GB | ~19.85 GB | ✅ **FITS** (4.15GB margin) | ✅ **FITS** |
| **32,768 (32k)** | ~4.29 GB | ~2.15 GB | ~23.07 GB | ⚠️ **TIGHT** (0.93GB margin) | ✅ **FITS** |
| **98,304 (98k)** | ~12.88 GB | ~6.44 GB | ~31.66 GB | ❌ **OOM on 24GB** | ✅ **FITS** |
| **131,072 (128k)** | ~17.18 GB | ~8.59 GB | ~35.96 GB | ❌ **OOM on 24GB** | ✅ **FITS** |

---

## 3. Reasoning Budget & Deployment Considerations

- **Thinking overhead:** The existing receipt reports 2,000–8,000 extra thinking tokens in some complex tasks. Exact count depends on model/runtime reasoning policy, task, prompt, output, and stop behavior; treat the range as `reported_community_partial`, not a universal budget.
- **Single 24GB constraint:** Keep generation context bounded when the selected artifact and KV-cache configuration require it. The matrix's OOM statuses are estimates, not direct runtime outcomes for every backend or allocation.

**Evidence status:** Architecture and artifact metadata are reported upstream metadata; throughput and reasoning observations are `reported_community_reproducible` only within the bounded receipt conditions; KV/VRAM matrix values are `estimated`. See the [DeepSeek R1 deep-research receipt](../receipts/deepseek-r1-distill-qwen-32b-deep-research-2026-08-23.md) and [DeepSeek R1 import receipt](../receipts/deepseek-r1-distill-qwen-32b-import-2026-08-23.md).
