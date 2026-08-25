---
id: M-QWEN3-CODER-30B-A3B
title: "Qwen3 Coder 30B A3B Instruct Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "qwen", "qwen3", "coder", "30b", "moe", "a3b", "gguf", "unsloth", "rtx3090ti"]
upstream_repo: "https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF"
upstream_commit: "9971034f59048a1c6a7e0c4f8261e6878b27eb5c"
primary_artifact: "Qwen3-Coder-30B-A3B-Instruct-Q4_K_S.gguf"
provenance_status: "validated"
evidence_status: "verified"
last_updated: "2026-08-23"
---

# Qwen3 Coder 30B A3B Instruct Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

- **Model Identity**: Qwen3 Coder 30B A3B Instruct (`Qwen/Qwen3-Coder-30B-A3B-Instruct`)
- **Architecture**: Sparse Mixture-of-Experts (MoE) specialized for Agentic Coding (non-thinking/direct code output)
- **Parameters**: 30.5B total / 3.3B active parameters per token
- **Base Precision**: BF16 / FP16
- **Layer & Head Count**: 48 Layers, 32 Attention Heads, 4 KV Heads (GQA, Head Dim 128)
- **Native Context Limit**: `262,144` tokens (262k)
- **Primary GGUF Artifact**: `Qwen3-Coder-30B-A3B-Instruct-Q4_K_S.gguf` (17.46 GB / 18,745,860,096 bytes)

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance
- **Single RTX 3090 / 3090 Ti (24GB)**: ~58.0 tok/s generation throughput (direct coding response without reasoning latency).
- **Dual RTX 3090 / 3090 Ti (2x24GB)**: ~82.0 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB)**: ~65.0 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (4 KV Heads, 48 Layers)

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~0.40 GB | ~0.20 GB | ~17.86 GB | ✅ **FITS** (6.14GB margin) | ✅ **FITS** |
| **32,768 (32k)** | ~1.61 GB | ~0.81 GB | ~19.07 GB | ✅ **FITS** (4.93GB margin) | ✅ **FITS** |
| **98,304 (98k)** | ~4.83 GB | ~2.42 GB | ~22.29 GB | ✅ **FITS** (1.71GB margin!) | ✅ **FITS** |
| **131,072 (128k)** | ~6.44 GB | ~3.22 GB | ~23.90 GB | ⚠️ **TIGHT** (0.10GB margin) | ✅ **FITS** |
| **262,144 (262k)** | ~12.88 GB | ~6.44 GB | ~30.34 GB | ❌ **OOM on 24GB** | ✅ **FITS** (fits with Q4 KV!) |

---

## 3. Key Findings & Deployment Recommendations

- **Top Pick for Agentic Coding**: Highly recommended for autonomous agent harnesses (Pi, OpenCode, Claude Code) when sub-second tool responses and low latency are critical.
