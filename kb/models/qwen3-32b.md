---
id: M-QWEN3-32B
title: "Qwen3 32B Instruct Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "qwen", "qwen3", "32b", "dense", "gguf", "unsloth", "rtx3090ti", "dual-3090"]
upstream_repo: "https://huggingface.co/unsloth/Qwen3-32B-Instruct-GGUF"
upstream_commit: "9ea7cfb565a4439fa8bc3c6233baad9116e09e13"
primary_artifact: "Qwen3-32B-Instruct-Q4_K_S.gguf"
provenance_status: "validated"
evidence_status: "verified"
last_updated: "2026-08-23"
---

# Qwen3 32B Instruct Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

- **Model Identity**: Qwen3 32B Instruct (`Qwen/Qwen3-32B-Instruct`)
- **Architecture**: Dense Transformer (32.8B total / 32.8B active parameters)
- **Base Precision**: BF16 / FP16
- **Layer & Head Count**: 64 Layers, 64 Attention Heads, 8 KV Heads (GQA, Head Dim 128)
- **Native Context Limit**: `131,072` tokens (128k)
- **Primary GGUF Artifact**: `Qwen3-32B-Instruct-Q4_K_S.gguf` (18.77 GB / 20,154,679,296 bytes)

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance
- **Single RTX 3090 / 3090 Ti (24GB)**: ~23.5 tok/s (fits standard Q4_K_S weights @ 18.77 GB; strictly limited to short context ≤16K).
- **Dual RTX 3090 / 3090 Ti (2x24GB)**: ~42.0 tok/s in tensor parallel; comfortably hosts full 131k context.
- **Mac Studio M4 Max (128GB)**: ~28.0 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (8 KV Heads, 64 Layers)

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~1.07 GB | ~0.54 GB | ~19.84 GB | ✅ **FITS** (4.16GB margin) | ✅ **FITS** |
| **32,768 (32k)** | ~4.29 GB | ~2.15 GB | ~23.06 GB | ⚠️ **TIGHT** (0.94GB margin) | ✅ **FITS** |
| **98,304 (98k)** | ~12.88 GB | ~6.44 GB | ~31.65 GB | ❌ **OOM on 24GB** | ✅ **FITS** |
| **131,072 (128k)** | ~17.18 GB | ~8.59 GB | ~35.95 GB | ❌ **OOM on 24GB** | ✅ **FITS** |

---

## 3. Deployment Recommendations

- **Single 24GB GPU**: Best for reasoning and code synthesis with context windows restricted to ≤16,384 tokens.
- **Dual 24GB GPUs**: Recommended production setup for agentic workflows requiring >32k context.
