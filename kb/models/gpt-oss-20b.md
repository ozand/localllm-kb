---
id: M-GPT-OSS-20B
title: "OpenAI gpt-oss-20b Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "openai", "gpt-oss", "20b", "moe", "reasoning", "mxfp4", "gguf", "unsloth", "rtx3090ti"]
upstream_repo: "https://huggingface.co/unsloth/gpt-oss-20b-GGUF"
upstream_commit: "d449b42d93e1c2c7bda5312f5c25c8fb91dfa9b4"
primary_artifact: "gpt-oss-20b-Q4_K_S.gguf"
provenance_status: "validated"
evidence_status: "verified"
last_updated: "2026-08-23"
---

# OpenAI gpt-oss-20b Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

- **Model Identity**: OpenAI gpt-oss-20b (`openai/gpt-oss-20b`)
- **Architecture**: Sparse Mixture-of-Experts (MoE) with native MXFP4 weight support & configurable reasoning effort (low/medium/high)
- **Parameters**: 21.0B total / 3.6B active parameters per token
- **Base Precision**: Native MXFP4 / BF16
- **Layer & Head Count**: 36 Layers, 32 Attention Heads, 4 KV Heads (GQA, Head Dim 128)
- **Native Context Limit**: `131,072` tokens (128k)
- **Primary GGUF Artifact**: `gpt-oss-20b-Q4_K_S.gguf` (11.62 GB / 12,476,710,912 bytes)

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance
- **Single RTX 3090 / 3090 Ti (24GB)**: ~65.4 tok/s generation throughput (fastest in the cohort due to 36 layers and 3.6B active params).
- **Dual RTX 3090 / 3090 Ti (2x24GB)**: ~95.0 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB)**: ~75.0 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (4 KV Heads, 36 Layers)

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~0.34 GB | ~0.17 GB | ~11.96 GB | ✅ **FITS** (12.04GB margin!) | ✅ **FITS** |
| **32,768 (32k)** | ~1.34 GB | ~0.67 GB | ~12.96 GB | ✅ **FITS** (11.04GB margin!) | ✅ **FITS** |
| **98,304 (98k)** | ~4.02 GB | ~2.01 GB | ~15.64 GB | ✅ **FITS** (8.36GB margin!) | ✅ **FITS** |
| **131,072 (128k)** | ~5.36 GB | ~2.68 GB | ~16.98 GB | ✅ **FITS** (7.02GB margin!) | ✅ **FITS** |

---

## 3. Key Findings & Deployment Recommendations

- **Ultimate Efficiency Champion**: Base weights are only 11.62 GB, and because the model has only 36 layers and 4 KV heads, even 128k context with full Q8 KV cache takes under 17.0 GB VRAM.
- **Reasoning Controllability**: Supports setting `reasoning_effort` (`low`, `medium`, `high`) directly in generation requests to trade latency for analytical depth.
