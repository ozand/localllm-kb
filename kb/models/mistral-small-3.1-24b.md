---
id: M-MISTRAL-SMALL-31-24B
title: "Mistral Small 3.1 24B Instruct Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "mistral", "mistral-small", "24b", "dense", "multimodal", "vision", "gguf", "unsloth", "rtx3090ti"]
upstream_repo: "https://huggingface.co/unsloth/Mistral-Small-3.1-24B-Instruct-2503-GGUF"
upstream_commit: "d449b42d93e1c2c7bda5312f5c25c8fb91dfa9b4"
primary_artifact: "Mistral-Small-3.1-24B-Instruct-2503-Q4_K_S.gguf"
vision_artifact: "mmproj-BF16.gguf"
provenance_status: "validated"
evidence_status: "verified"
last_updated: "2026-08-23"
---

# Mistral Small 3.1 24B Instruct Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

- **Model Identity**: Mistral Small 3.1 24B Instruct (`mistralai/Mistral-Small-3.1-24B-Instruct-2503`)
- **Architecture**: Dense Multimodal Transformer (Text + Vision) — 24.0B parameters
- **Base Precision**: BF16 / FP16
- **Layer & Head Count**: 56 Layers, 32 Attention Heads, 8 KV Heads (GQA, Head Dim 128)
- **Native Context Limit**: `131,072` tokens (128k)
- **Primary GGUF Artifact**: `Mistral-Small-3.1-24B-Instruct-2503-Q4_K_S.gguf` (13.55 GB / 14,547,404,800 bytes)
- **Vision Projector Artifact**: `mmproj-BF16.gguf` (878.1 MB / 920,748,032 bytes)

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance
- **Single RTX 3090 / 3090 Ti (24GB)**: ~33.2 tok/s text generation (fastest among 24B–32B dense architectures).
- **Dual RTX 3090 / 3090 Ti (2x24GB)**: ~56.0 tok/s in tensor parallel.
- **Mac Studio M4 Max (128GB)**: ~38.0 tok/s in Metal backend.

### Context & KV Cache Scaling Matrix (8 KV Heads, 56 Layers)

| Context Length | Q8_0 KV Cache | Q4_0 KV Cache | Total VRAM (Q4_K_S + Q8 KV) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | ~0.94 GB | ~0.47 GB | ~14.49 GB | ✅ **FITS** (9.51GB margin) | ✅ **FITS** |
| **32,768 (32k)** | ~3.75 GB | ~1.88 GB | ~17.30 GB | ✅ **FITS** (6.70GB margin) | ✅ **FITS** |
| **98,304 (98k)** | ~11.27 GB | ~5.63 GB | ~24.82 GB | ⚠️ **BORDERLINE** (fits with Q4 KV!) | ✅ **FITS** |
| **131,072 (128k)** | ~15.03 GB | ~7.52 GB | ~28.58 GB | ❌ **OOM on 24GB** | ✅ **FITS** |

---

## 3. Key Findings & Deployment Recommendations

- **Compact Footprint**: Base Q4_K_S model takes only 13.55 GB VRAM, leaving over 10.4 GB headroom for KV cache and vision activations on a single 24GB GPU.
- **98K Context on Single 24GB GPU**: Using `q4_0` KV cache (`--ctk q4_0 --ctv q4_0`), 98,304 context requires only 5.63 GB KV memory, yielding a total VRAM of **19.18 GB** (comfortably within 24GB with 4.8 GB headroom).
