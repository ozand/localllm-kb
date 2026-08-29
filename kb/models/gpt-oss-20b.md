---
id: M-GPT-OSS-20B
title: "OpenAI gpt-oss-20b Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "openai", "gpt-oss", "20b", "moe", "reasoning", "mxfp4", "gguf", "unsloth", "rtx3090ti"]
upstream_repo: "https://huggingface.co/unsloth/gpt-oss-20b-GGUF"
upstream_commit: "d449b42d93e1c2c7bda5312f5c25c8fb91dfa9b4"
primary_artifact: "gpt-oss-20b-Q4_K_S.gguf"
provenance_status: "validated_metadata_bounded_runtime_evidence"
evidence_status: "reported_community_reproducible_and_estimated"
last_updated: "2026-08-29"
limitations: "Artifact metadata is reported upstream metadata; hardware throughput is reported community evidence; KV/VRAM matrices are estimates. Architecture and context discrepancies are preserved explicitly."
---

# OpenAI gpt-oss-20b Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

The base-model and GGUF identities below come from the existing import receipt. Artifact byte size and hash are reported upstream metadata, not a local recomputation. Architecture/context figures remain separated from runtime/client support and deployment estimates.

- **Model Identity**: OpenAI gpt-oss-20b (`openai/gpt-oss-20b`)
- **Architecture**: Sparse Mixture-of-Experts (MoE) with native MXFP4 weight support & configurable reasoning effort (low/medium/high)
- **Parameters**: 21.0B total / 3.6B active parameters per token
- **Base Precision**: Native MXFP4 / BF16
- **Layer and head count:** existing records disagree materially: this page reports 36 layers, 32 attention heads, and 4 KV heads; the deep-research receipt reports 40/32/4; the import receipt reports 24/64/8. Preserve this architecture discrepancy; no value is inferred.
- **Context limit:** `131,072` tokens is reported model metadata, while the import record also notes a `4,096` initial context with YaRN scaling. Usable runtime/client context and KV behavior remain `unknown` here.
- **Primary GGUF artifact:** `gpt-oss-20b-Q4_K_S.gguf`; reported upstream metadata is `11.62 GB / 11,618,492,608 bytes` at GGUF revision `d449b42d93e1c2c7bda5312f5c25c8fb91dfa9b4`. The page's previous `12,476,710,912`-byte value is not reconciled with that record; local verification is `unknown`.

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance

The following are bounded `reported_community_reproducible` observations from the linked deep-research receipt, not universal reference rates. Exact artifact, runtime/version, backend, hardware configuration, context, workload, concurrency, reasoning effort, sampling, and measurement method are not fully recorded on this page and remain `unknown` where absent.

- **Single RTX 3090 / 3090 Ti (24GB):** reported ~65.4 tok/s generation throughput. The efficiency explanation is a hypothesis tied to architecture/active parameters, not a controlled cross-model comparison.
- **Dual RTX 3090 / 3090 Ti (2x24GB):** reported ~95.0 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB):** reported ~75.0 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (4 KV Heads, 36 Layers)

The matrix is an `estimated` architecture-based calculation using the page's 4-KV-head/36-layer interpretation, not a runtime allocation measurement. Because existing receipts disagree on architecture counts, these estimates are not authoritative until the model configuration is resolved. Allocator overhead, runtime placement, reasoning/output tokens, backend behavior, and usable headroom are `unknown`. `FITS` and headroom values are estimates for nominal hardware, not guarantees.

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~0.34 GB | ~0.17 GB | ~11.96 GB | ✅ **FITS** (12.04GB margin!) | ✅ **FITS** |
| **32,768 (32k)** | ~1.34 GB | ~0.67 GB | ~12.96 GB | ✅ **FITS** (11.04GB margin!) | ✅ **FITS** |
| **98,304 (98k)** | ~4.02 GB | ~2.01 GB | ~15.64 GB | ✅ **FITS** (8.36GB margin!) | ✅ **FITS** |
| **131,072 (128k)** | ~5.36 GB | ~2.68 GB | ~16.98 GB | ✅ **FITS** (7.02GB margin!) | ✅ **FITS** |

---

## 3. Key Findings & Deployment Recommendations

- **Memory profile:** The reported 11.62 GB file footprint and this page's estimated matrix suggest a compact deployment profile under the stated assumptions. “Ultimate Efficiency Champion” and “under 17.0 GB” are not universal conclusions because artifact, architecture, runtime allocation, KV settings, and workload evidence are not fully reconciled.
- **Reasoning controllability:** `reasoning_effort` (`low`, `medium`, `high`) is a reported model/interface capability. The effect on latency, token count, and quality is runtime-, task-, and policy-specific; no effort-specific local benchmark is claimed.

**Evidence status:** Architecture and artifact metadata are reported upstream metadata; throughput is `reported_community_reproducible` only within bounded receipt conditions; KV/VRAM matrix and fit statuses are `estimated`. See the [gpt-oss deep-research receipt](../receipts/gpt-oss-20b-deep-research-2026-08-23.md) and [gpt-oss import receipt](../receipts/gpt-oss-20b-import-2026-08-23.md).
