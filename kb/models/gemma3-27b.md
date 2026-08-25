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
provenance_status: "validated"
evidence_status: "verified"
last_updated: "2026-08-23"
---

# Gemma 3 27B Instruct Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

- **Model Identity**: Gemma 3 27B Instruct (`google/gemma-3-27b-it`)
- **Architecture**: Dense Multimodal Transformer (Text + Vision) — 27.2B text parameters + SigLIP-based vision encoder
- **Base Precision**: BF16 / FP16
- **Layer & Head Count**: 62 Layers, 32 Attention Heads, 16 KV Heads (GQA, Head Dim 128)
- **Native Context Limit**: `131,072` tokens (128k)
- **Primary GGUF Artifact**: `gemma-3-27b-it-Q4_K_S.gguf` (15.67 GB / 16,825,487,360 bytes)
- **Vision Projector Artifact**: `mmproj-BF16.gguf` (857.7 MB / 899,357,984 bytes)

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance
- **Single RTX 3090 / 3090 Ti (24GB)**: ~28.5 tok/s text generation.
- **Dual RTX 3090 / 3090 Ti (2x24GB)**: ~48.0 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB)**: ~32.0 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (16 KV Heads, 62 Layers)

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~2.03 GB | ~1.02 GB | ~17.70 GB | ✅ **FITS** (6.30GB margin) | ✅ **FITS** |
| **32,768 (32k)** | ~8.12 GB | ~4.06 GB | ~23.79 GB | ⚠️ **TIGHT** (0.21GB margin) | ✅ **FITS** |
| **98,304 (98k)** | ~24.36 GB | ~12.18 GB | ~40.03 GB | ❌ **OOM on 24GB** | ✅ **FITS** |
| **131,072 (128k)** | ~32.48 GB | ~16.24 GB | ~48.15 GB | ❌ **OOM on 24GB** | ⚠️ **TIGHT** (Dual 3090) |

---

## 3. Key Findings & Multimodal Deployment

- **Large KV Cache Alert**: Because Gemma 3 uses 16 KV heads (double standard GQA models), its KV cache footprint at 98k alone exceeds the entire 24GB VRAM capacity of a single RTX 3090. Single GPU deployments must use Q4 KV or cap context to ≤32k tokens.
- **Vision Integration**: Load `--mmproj mmproj-BF16.gguf` for native visual reasoning and document parsing.
