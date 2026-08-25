---
id: M-QWEN3-30B-A3B
title: "Qwen3 30B A3B Instruct Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "qwen", "qwen3", "30b", "moe", "a3b", "gguf", "unsloth", "rtx3090ti"]
upstream_repo: "https://huggingface.co/unsloth/Qwen3-30B-A3B-Instruct-GGUF"
upstream_commit: "40d2f928eeb59be20d885a0694ef2fa2aeb049eb"
primary_artifact: "Qwen3-30B-A3B-Instruct-Q4_K_S.gguf"
provenance_status: "validated"
evidence_status: "verified"
last_updated: "2026-08-23"
---

# Qwen3 30B A3B Instruct Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

- **Model Identity**: Qwen3 30B A3B Instruct (`Qwen/Qwen3-30B-A3B-Instruct`)
- **Architecture**: Sparse Mixture-of-Experts (MoE) — 30.5B total parameters / 3.3B active parameters per token
- **Base Precision**: BF16 / FP16
- **Layer & Head Count**: 48 Layers, 32 Attention Heads, 4 KV Heads (GQA, Head Dim 128)
- **Native Context Limit**: `131,072` tokens (128k)
- **Primary GGUF Artifact**: `Qwen3-30B-A3B-Instruct-Q4_K_S.gguf` (17.46 GB / 18,745,860,096 bytes)

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance
- **Single RTX 3090 / 3090 Ti (24GB)**: ~55.0 tok/s generation throughput (due to 3.3B active compute load).
- **Dual RTX 3090 / 3090 Ti (2x24GB)**: ~78.0 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB)**: ~62.0 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (4 KV Heads, 48 Layers)

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~0.40 GB | ~0.20 GB | ~17.86 GB | ✅ **FITS** (6.14GB margin) | ✅ **FITS** |
| **32,768 (32k)** | ~1.61 GB | ~0.81 GB | ~19.07 GB | ✅ **FITS** (4.93GB margin) | ✅ **FITS** |
| **98,304 (98k)** | ~4.83 GB | ~2.42 GB | ~22.29 GB | ✅ **FITS** (1.71GB margin!) | ✅ **FITS** |
| **131,072 (128k)** | ~6.44 GB | ~3.22 GB | ~23.90 GB | ⚠️ **TIGHT** (0.10GB margin) | ✅ **FITS** |

---

## 3. Key Findings & Deployment Recommendations

- **Single GPU Champion**: Thanks to having only 4 KV heads and 48 layers, the KV cache footprint is minimal. It is one of the few 30B-class models that can run **98,304 tokens of context on a single 24GB GPU** without VRAM offloading or context degradation.
