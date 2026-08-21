---
title: "Qwen3.8 27B Artifact and Model Profile"
id: "M-QWEN3.8-27B"
layer: "models"
status: "active"
tags: ["model", "qwen", "gguf", "unsloth", "rtx3090ti", "ryzen5950x", "reasoning", "multimodal"]
upstream_repo: "https://huggingface.co/unsloth/Qwen3.8-27B-GGUF"
upstream_commit: "4ca720788d1e01f1bff70c033e0d0028fd02e502"
primary_artifact: "Qwen3.8-27B-UD-Q4_K_S.gguf"
local_alias: "Qwen3.8-27B-Q4_K_S.gguf"
provenance_status: "validated"
evidence_status: "verified"
last_updated: "2026-04-18"
---

# Qwen3.8 27B Model & Hardware Execution Profile

## 1. Upstream Identity & Artifact Specs

- **Model Family**: Qwen3.8 (hybrid DeltaNet + Gated Attention architecture)
- **Base Precision**: BF16 / FP16
- **Recommended Quantization**: `UD-Q4_K_S` (Unsloth Dynamic V3 imatrix quantization)
- **Primary GGUF Artifact**: `Qwen3.8-27B-UD-Q4_K_S.gguf`
- **Compatibility Symlink / Alias**: `Qwen3.8-27B-Q4_K_S.gguf`
- **Native Context Limit**: `262,144` tokens (expandable to `1,000,000` with YaRN)
- **Multi-Token Prediction (MTP)**: Integrated native draft prediction layer (self-speculative decoding).

---

## 2. Hardware Allocation & Memory Profiles

### Host Reference Architecture
- **GPU**: NVIDIA GeForce RTX 3090 Ti (24 GB GDDR6X / 24,564 MiB, Driver 610.88)
- **CPU**: AMD Ryzen 9 5950X (16 Physical Cores / 32 Threads)
- **System RAM**: 128 GB DDR4 (high-capacity context buffer)

### Memory Footprint & Context Scaling Matrix

| Quant / KV Config | VRAM Weight | KV Cache (32k) | KV Cache (98k) | KV Cache (262k) | Max Safe GPU Context | Recommended Host Profile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **UD-Q4_K_S + FP16 KV** | ~16.5 GB | ~7.2 GB | ~22.0 GB (OOM) | ~58.0 GB (OOM) | **32,768** | GPU only (tight margin) |
| **UD-Q4_K_S + Q8_0 KV** | ~16.5 GB | ~3.6 GB | ~11.0 GB | ~29.0 GB (OOM) | **98,304** | **Default Production Profile** (fits 24GB VRAM) |
| **UD-Q4_K_S + Q4_0 KV** | ~16.5 GB | ~1.8 GB | ~5.5 GB | ~14.5 GB | **131,072** | Extended Long-Context Profile |
| **UD-Q4_K_S + CPU Offload**| ~16.5 GB (GPU) | - | - | System RAM (~32 GB) | **262,144** | Full 262k Context (KV in 128GB RAM, CPU threads: 16) |

---

## 3. Sampling & Reasoning Parameters

### Thinking Mode (Analytical & Coding Tasks)
```json
{
  "temperature": 1.0,
  "top_p": 0.95,
  "top_k": 20,
  "min_p": 0.0,
  "presence_penalty": 0.0,
  "repetition_penalty": 1.0
}
```

### Instruct / Fast Non-Thinking Mode
```json
{
  "temperature": 0.7,
  "top_p": 0.80,
  "top_k": 20,
  "min_p": 0.0,
  "presence_penalty": 1.5,
  "repetition_penalty": 1.0
}
```

---

## 4. Reasoning Budget Reference (`llama_extra_args`)

Thinking token limits must be passed dynamically via runtime arguments without patching base installations:

- `2048` — Strict deterministic diagnosis / classification.
- `4096` — Standard bounded test / single-step coding task.
- `8192` — Complex multi-file architectural planning.
- `0` — Hard disable thinking tokens (pure instruct mode).
- `-1` — Unbounded thinking (strictly prohibited in automated production pipelines).

---

## 5. Performance Optimizations & Modalities

### Draft-MTP (Self-Speculative Decoding)
Because Qwen3.8 embeds a native Multi-Token Prediction head, enabling `--draft-mtp` or `--speculative-draft` in llama.cpp yields an acceleration of **30% to 60% tok/s** without allocating VRAM for a secondary small draft model.

### Multimodal (Vision & Video)
- **Image Support**: Requires loading the matching `mmproj` tensor (`--mmproj Qwen3.8-27B-mmproj-f16.gguf`).
- **Video Sampling**: Supported natively via temporal slice sampling (recommended 1-2 FPS keyframes downsampled to 448x448) within the extended context window.

---

## 6. Related References

- [Raw Capture: Model Card Specs](../raw/research/qwen3.8-27b-card.md)
- [Raw Capture: Reddit VRAM Benchmarks](../raw/research/reddit-27b-32b-vram-tuning.md)
