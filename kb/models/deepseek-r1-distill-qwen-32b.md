---
id: M-DEEPSEEK-R1-DISTILL-QWEN-32B
title: "DeepSeek R1 Distill Qwen 32B Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "deepseek", "r1", "reasoning", "distill", "qwen", "32b", "dense", "gguf", "bartowski", "rtx3090ti"]
upstream_repo: "https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-32B-GGUF"
upstream_commit: "91d17d52a233b8fbca971842ba7cecfc8fe7ab41"
primary_artifact: "DeepSeek-R1-Distill-Qwen-32B-Q4_K_S.gguf"
provenance_status: "validated"
evidence_status: "verified"
last_updated: "2026-08-23"
---

# DeepSeek R1 Distill Qwen 32B Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

- **Model Identity**: DeepSeek R1 Distill Qwen 32B (`deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`)
- **Architecture**: Dense Transformer fine-tuned with DeepSeek R1 reasoning traces (32.5B parameters)
- **Base Precision**: BF16 / FP16
- **Layer & Head Count**: 64 Layers, 64 Attention Heads, 8 KV Heads (GQA, Head Dim 128)
- **Native Context Limit**: `131,072` tokens (128k)
- **Primary GGUF Artifact**: `DeepSeek-R1-Distill-Qwen-32B-Q4_K_S.gguf` (18.78 GB / 20,165,165,472 bytes)

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance
- **Single RTX 3090 / 3090 Ti (24GB)**: ~23.8 tok/s raw token generation. Total query completion time is 2x–5x longer due to reasoning `<think>` token generation.
- **Dual RTX 3090 / 3090 Ti (2x24GB)**: ~43.5 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB)**: ~28.5 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (8 KV Heads, 64 Layers)

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~1.07 GB | ~0.54 GB | ~19.85 GB | ✅ **FITS** (4.15GB margin) | ✅ **FITS** |
| **32,768 (32k)** | ~4.29 GB | ~2.15 GB | ~23.07 GB | ⚠️ **TIGHT** (0.93GB margin) | ✅ **FITS** |
| **98,304 (98k)** | ~12.88 GB | ~6.44 GB | ~31.66 GB | ❌ **OOM on 24GB** | ✅ **FITS** |
| **131,072 (128k)** | ~17.18 GB | ~8.59 GB | ~35.96 GB | ❌ **OOM on 24GB** | ✅ **FITS** |

---

## 3. Reasoning Budget & Deployment Considerations

- **Thinking Overhead**: In complex math, algorithmic coding, or deep logical verification, thinking traces often produce 2,000–8,000 extra tokens before the final response.
- **Single 24GB Constraint**: Keep max generation context bounded to avoid out-of-memory during lengthy chain-of-thought expansions.
