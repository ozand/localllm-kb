---
id: M-GEMMA3-27B
title: "Gemma 3 27B Instruct Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "google", "gemma", "gemma3", "27b", "dense", "multimodal", "vision", "gguf", "unsloth", "rtx3090ti"]
upstream_repo: "https://huggingface.co/unsloth/gemma-3-27b-it-GGUF"
upstream_commit: "9bfd5d7870a3fa43df65d491c1fc552cb662d5e2"
primary_artifact: "gemma-3-27b-it-Q4_K_S.gguf"
vision_artifact: "mmproj-BF16.gguf"
provenance_status: "validated_metadata_bounded_runtime_evidence"
evidence_status: "reported_community_reproducible_and_estimated"
last_updated: "2026-08-29"
limitations: "Artifact metadata is reported upstream metadata; hardware throughput is reported community evidence; KV/VRAM matrices are estimates. Runtime/version, allocation, workload, and measurement conditions are not universal."
---

# Gemma 3 27B Instruct Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

The base-model and GGUF identities below come from the existing import receipt. Artifact byte size and hash are reported upstream metadata, not a local recomputation. Architecture/context figures describe model metadata and do not establish runtime/client/projector support.

- **Model Identity**: Gemma 3 27B Instruct (`google/gemma-3-27b-it`)
- **Architecture**: Dense Multimodal Transformer (Text + Vision) — 27.2B text parameters + SigLIP-based vision encoder
- **Base Precision**: BF16 / FP16
- **Layer & Head Count**: 62 Layers, 32 Attention Heads, 16 KV Heads (GQA, Head Dim 128)
- **Native Context Limit:** `131,072` tokens (128k) as reported model metadata; usable runtime context, KV-cache implementation, and client limit are `unknown`.
- **Primary GGUF Artifact:** `gemma-3-27b-it-Q4_K_S.gguf` (reported upstream metadata: 15.67 GB / 16,825,487,360 bytes; local verification: `unknown`).
- **Vision Projector Artifact:** `mmproj-BF16.gguf` (reported 857.7 MB / 899,357,984 bytes; exact revision and local verification: `unknown`).

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance

The following are bounded `reported_community_reproducible` observations from the linked deep-research receipt, not universal reference rates. Exact artifact, runtime/version, backend, hardware configuration, context, workload, concurrency, sampling, and measurement method are not fully recorded on this page and remain `unknown` where absent.

- **Single RTX 3090 / 3090 Ti (24GB):** reported ~28.5 tok/s text generation.
- **Dual RTX 3090 / 3090 Ti (2x24GB):** reported ~48.0 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB):** reported ~32.0 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (16 KV Heads, 62 Layers)

The matrix is an `estimated` architecture-based calculation, not a runtime allocation measurement. It assumes the listed quantization and KV-cache types; allocator overhead, projector memory, prompt/image tokens, backend behavior, and usable headroom are `unknown`. `FITS`, `TIGHT`, and `OOM` are estimates for the named nominal hardware, not guarantees across runtimes.

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~2.03 GB | ~1.02 GB | ~17.70 GB | ✅ **FITS** (6.30GB margin) | ✅ **FITS** |
| **32,768 (32k)** | ~8.12 GB | ~4.06 GB | ~23.79 GB | ⚠️ **TIGHT** (0.21GB margin) | ✅ **FITS** |
| **98,304 (98k)** | ~24.36 GB | ~12.18 GB | ~40.03 GB | ❌ **OOM on 24GB** | ✅ **FITS** |
| **131,072 (128k)** | ~32.48 GB | ~16.24 GB | ~48.15 GB | ❌ **OOM on 24GB** | ⚠️ **TIGHT** (Dual 3090) |

---

## 3. Key Findings & Multimodal Deployment

- **Large KV-cache alert:** The matrix estimates that the 98k Q8 KV entry exceeds nominal single-RTX-3090 VRAM. This is not a direct runtime measurement; actual allocation depends on KV type, allocator, model artifact, projector, prompt/image tokens, and backend. The recommendation to use Q4 KV or cap context to ≤32k is conditional guidance, not a universal requirement.
- **Vision integration:** Load `--mmproj mmproj-BF16.gguf` when the selected llama.cpp build and artifact support this projector path. Model capability, projector artifact availability, and client/runtime support remain separate checks.

**Evidence status:** Architecture and artifact metadata are `reported_official`/reported upstream metadata; throughput is `reported_community_reproducible`; KV/VRAM matrix and fit statuses are `estimated`. See the [Gemma 3 deep-research receipt](../receipts/gemma3-27b-deep-research-2026-08-23.md) and [Gemma 3 import receipt](../receipts/gemma3-27b-instruct-import-2026-08-23.md).
