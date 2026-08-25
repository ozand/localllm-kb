---
id: M-NEMOTRON-35-LIGHTNING-30B-A3B
title: "NVIDIA Nemotron 3.5 Lightning Model & Artifact Profile"
layer: "models"
status: "active"
tags: ["model", "nvidia", "nemotron", "30b", "mamba", "moe", "hybrid", "gguf", "bartowski", "unsloth", "rtx3090ti"]
upstream_repo: "https://huggingface.co/bartowski/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF"
upstream_commit: "f0eec2267ae843d9eb21ea3926ab0046da0a8628"
primary_artifact: "NVIDIA-Nemotron-3.5-Lightning-30B-A3B-Q4_K_S.gguf"
alternative_artifact: "unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-UD-Q4_K_S.gguf"
provenance_status: "validated"
evidence_status: "verified"
last_updated: "2026-08-23"
---

# NVIDIA Nemotron 3.5 Lightning Model & Hardware Execution Profile

## 1. Upstream Identity & Architecture

- **Model Identity**: NVIDIA Nemotron 3.5 Lightning 30B A3B (`nvidia/Nemotron-3.5-Lightning-30B-A3B`)
- **Architecture**: Hybrid Linear Mamba-2 SSM + Sparse MoE + Standard Attention Layers (30.0B total / 3.0B active parameters)
- **Base Precision**: BF16 / FP16
- **Context Limit**: Documented up to `1,048,576` tokens (1M); practical local target `131,072`–`262,144` tokens
- **Primary GGUF Artifact**: `NVIDIA-Nemotron-3.5-Lightning-30B-A3B-Q4_K_S.gguf` (23.20 GB / 24,910,888,960 bytes)
- **Alternative GGUF Artifact**: `NVIDIA-Nemotron-3.5-Lightning-30B-A3B-UD-Q4_K_S.gguf` (24.47 GB / 26,273,280,000 bytes)

---

## 2. Hardware Allocation & Memory Profiles

### Reference Hardware Performance
- **Single RTX 3090 / 3090 Ti (24GB)**: ~68.2 tok/s with `IQ4_NL` (19.4 GB weights) or `Q3_K_M` (17.8 GB weights).
- **Dual RTX 3090 / 3090 Ti (2x24GB)**: ~92.0 tok/s in tensor parallel with full `Q4_K_S` / `Q5_K_M`.
- **Mac Studio M4 Max (128GB)**: ~72.0 tok/s in Metal backend.

### Context & State Memory Scaling Matrix (Hybrid Mamba-2 Linear SSM)

| Context Length | Hybrid Recurrent State | Attention KV Cache | Total VRAM (IQ4_NL + State) | Single 24GB Status | Dual 24GB Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **8,192 (8k)** | Constant (~0.8 GB) | ~0.3 GB | ~20.50 GB | ✅ **FITS** (3.50GB margin) | ✅ **FITS** |
| **32,768 (32k)** | Constant (~0.8 GB) | ~1.2 GB | ~21.40 GB | ✅ **FITS** (2.60GB margin) | ✅ **FITS** |
| **98,304 (98k)** | Constant (~0.8 GB) | ~3.7 GB | ~23.90 GB | ⚠️ **TIGHT** (with IQ4_NL) | ✅ **FITS** |
| **262,144 (262k)** | Constant (~0.8 GB) | ~9.8 GB | ~30.00 GB | ❌ **OOM on 24GB** | ✅ **FITS** |

---

## 3. Key Findings & Deployment Recommendations

- **Sub-quadratic Scaling**: The hybrid Mamba-2 architecture allows linear recurrent state handling across long contexts, preventing standard transformer KV cache memory explosion.
- **Quantization Selection**: For a single 24GB GPU, use `IQ4_NL` (19.4 GB) rather than `Q4_K_S` (23.2 GB) to allow sufficient VRAM for recurrent state buffers.
