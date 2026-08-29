---
id: M-QWEN25-32B
title: "Qwen2.5 32B Instruct Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "qwen", "qwen2.5", "32b", "dense", "gguf", "bartowski", "rtx3090ti"]
upstream_repo: "https://huggingface.co/bartowski/Qwen2.5-32B-Instruct-GGUF"
upstream_commit: "91d17d52a233b8fbca971842ba7cecfc8fe7ab41"
primary_artifact: "Qwen2.5-32B-Instruct-Q4_K_S.gguf"
provenance_status: "validated_metadata_bounded_runtime_evidence"
evidence_status: "reported_community_reproducible_and_estimated"
last_updated: "2026-08-29"
limitations: "Artifact metadata is reported upstream metadata; hardware throughput is reported community evidence; KV/VRAM matrices are estimates. Native versus extended context and architecture discrepancies are preserved explicitly."
---

# Qwen2.5 32B Instruct Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

The base-model and GGUF identities below come from the existing import receipt. Artifact byte size and hash are reported upstream metadata, not a local recomputation. Architecture/context figures remain separated from runtime/client support and deployment estimates.

- **Model Identity**: Qwen2.5 32B Instruct (`Qwen/Qwen2.5-32B-Instruct`)
- **Architecture**: Dense Transformer (32.5B total / 32.5B active parameters)
- **Base Precision**: BF16 / FP16
- **Layer and head count:** 64 layers and 8 KV heads are reported consistently; the existing records disagree on the attention-head count (`64` on this page versus `40` in the import/deep-research receipts), and head dimension is not locally verified. Preserve this discrepancy; do not infer a value.
- **Context limit:** the import/deep-research records distinguish `32,768` config-native context from `131,072` extended context via YaRN/RoPE. Runtime/client support and usable context remain `unknown` here.
- **Primary GGUF artifact:** `Qwen2.5-32B-Instruct-Q4_K_S.gguf`; reported upstream metadata is `18.78 GB / 18,784,410,496 bytes` at the cited GGUF revision. The page's previous `20,165,165,472`-byte value is not reconciled with that record; local verification is `unknown`.

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance

The following are bounded `reported_community_reproducible` observations from the linked deep-research receipt, not universal reference rates. Exact artifact, runtime/version, backend, hardware configuration, context, workload, concurrency, sampling, and measurement method are not fully recorded on this page and remain `unknown` where absent.

- **Single RTX 3090 / 3090 Ti (24GB):** reported ~24.5 tok/s generation throughput.
- **Dual RTX 3090 / 3090 Ti (2x24GB):** reported ~44.0 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB):** reported ~29.5 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (8 KV Heads, 64 Layers)

The matrix is an `estimated` architecture-based calculation, not a runtime allocation measurement. It assumes the listed quantization and KV-cache types; allocator overhead, runtime placement, prompt length, backend behavior, and usable headroom are `unknown`. `FITS`, `TIGHT`, and `OOM` are estimates for the named nominal hardware, not guarantees across runtimes.

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~1.07 GB | ~0.54 GB | ~19.85 GB | ✅ **FITS** (4.15GB margin) | ✅ **FITS** |
| **32,768 (32k)** | ~4.29 GB | ~2.15 GB | ~23.07 GB | ⚠️ **TIGHT** (0.93GB margin) | ✅ **FITS** |
| **98,304 (98k)** | ~12.88 GB | ~6.44 GB | ~31.66 GB | ❌ **OOM on 24GB** | ✅ **FITS** |
| **131,072 (128k)** | ~17.18 GB | ~8.59 GB | ~35.96 GB | ❌ **OOM on 24GB** | ✅ **FITS** |

---

## 3. Deployment Recommendations

- **Baseline stability:** The model is described as a general instruction model, but “predictable token output” and mature support across all inference runtimes are not universal guarantees. Runtime/client compatibility, prompt-template behavior, and output stability depend on the selected artifact and integration and remain `unknown` unless separately validated.

**Evidence status:** Architecture and artifact metadata are reported upstream metadata; throughput is `reported_community_reproducible` only within bounded receipt conditions; KV/VRAM matrix and fit statuses are `estimated`. See the [Qwen2.5 deep-research receipt](../receipts/qwen2.5-32b-deep-research-2026-08-23.md) and [Qwen2.5 import receipt](../receipts/qwen2.5-32b-instruct-import-2026-08-23.md).
