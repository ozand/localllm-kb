---
id: LLM-KB-WIKI-OPENNESS-FINETUNING
title: "Artificial Analysis Openness Index & Local Adaptation Feasibility Matrix"
category: wiki
tags: [openness, fine-tuning, qlora, grpo, consumer_gpu, data_transparency]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, windows
  shell: bash, powershell
  tools: [unsloth, trl, peft, deepspeed]
error_signatures:
  - "CUDA out of memory during backward pass with LoRA"
  - "gradient checkpointing required for sequence length > 4096"
---

# Artificial Analysis Openness Index & Local Adaptation Feasibility

Understanding the distinction between **Open Weights** and **Truly Open Source** (Open Data / Open Training) models is essential when evaluating models for fine-tuning, domain adaptation, and local post-training.

---

## 1. The 6 Dimensions of Model Openness

| Dimension | Open Weights Baseline | Truly Open Source Target | Impact on Local Adaptation |
|---|---|---|---|
| **1. Model Weights** | Publicly downloadable (HF/GGUF) | Publicly downloadable | Basic requirement for local inference & fine-tuning. |
| **2. Inference Code** | Public (Transformers / llama.cpp) | Public | Enables custom engine integration. |
| **3. Training Code & Config** | Proprietary / Absent | Public (loss, LR schedules, optimizer) | Critical for reproducible Continual Pre-Training. |
| **4. Pretraining Data** | Opaque / Undisclosed Mixture | Public / Fully Documented Corpus | Prevents benchmark contamination audit & catastrophic forgetting analysis. |
| **5. RL / SFT Datasets** | Proprietary | Public prompts & preference pairs | Required to replicate alignment or align on domain tasks. |
| **6. Technical Paper / Specs** | High-level marketing/blog | Detailed architecture & ablation paper | Essential for understanding attention quirks & kernel optimizations. |

---

## 2. Cohort Model Openness Classification

| Model | Architecture | Openness Tier | Weights | Train Code | Pretrain Data | SFT/RL Data | Local Adaptation Suitability |
|---|---|---|---|---|---|---|---|
| **OpenAI gpt-oss-20b** | MoE 21B / 3.6B | **High Transparency** | Yes | Yes (recipes) | Yes (sample mix) | Partial | **Excellent**: Easy domain adaptation & small footprint. |
| **Mistral Small 3.1 24B** | Dense 24B | **Open Weights** | Yes | No | No | No | **High**: Fast QLoRA tuning for coding & vision. |
| **Qwen3 30B A3B / Coder** | MoE 30.5B / 3.3B | **Open Weights** | Yes | No | No | No | **High**: Fast QLoRA, very low active param backward pass. |
| **Qwen3.8 27B (xhigh)** | Dense 27B | **Open Weights** | Yes | No | No | No | **High**: LoRA/GRPO reasoning tuning on 24GB. |
| **DeepSeek R1 Distill 32B** | Dense 32.5B | **Open Weights** | Yes | No | No | Partial (R1 traces) | **High**: SFT on reasoning chains. |
| **Gemma 3 27B Instruct** | Dense 27.2B | **Open Weights** | Yes | No | No | No | **Medium**: High KV memory requires strict sequence limits. |
| **DeepSeek V3 671B MoE** | MoE 671B / 37B | **Open Weights + Deep Paper** | Yes | No | No | No | **Low (Consumer)**: Requires 8x 80GB cluster for FT. |

---

## 3. Consumer Hardware Fine-Tuning Feasibility Matrix (24GB & 48GB)

```
+---------------------------------------------------------------------------------------+
|  Training Method       |  1x RTX 3090 / 4090 (24GB VRAM)  |  2x RTX 3090 / 4090 (48GB)        |
+---------------------------------------------------------------------------------------+
|  QLoRA (4-bit Base)    |  Up to 32B Dense / 30B MoE (8K)  |  Up to 70B Dense (16K context)    |
|  LoRA (16-bit Base)    |  Up to 14B Dense (4K context)    |  Up to 32B Dense / 30B MoE (8K)   |
|  GRPO (RL Reasoning)   |  Up to 27B Dense / 21B MoE (4K)  |  Up to 32B Dense (8K context)     |
|  Continual Pretraining |  Up to 14B QLoRA (4K sequence)   |  Up to 32B QLoRA (8K sequence)    |
|  Full Fine-Tuning (FP16)| Up to 7B/8B Dense (2K sequence) |  Up to 14B Dense (ZeRO-3 FSDP)    |
+---------------------------------------------------------------------------------------+
```

### Key VRAM Optimization Rules for Local Training:
1. **Gradient Checkpointing**: Mandatory for sequences $\ge 2048$ tokens (reduces activation VRAM by up to 65%).
2. **Optimizer Offload**: Use `paged_adamw_8bit` or `adamw_8bit` via BitsAndBytes to keep optimizer states $< 2.0	ext{ GB}$.
3. **MoE Advantage in QLoRA**: Backward pass compute only touches active parameters (3.3B in Qwen3 30B vs 32.5B in Qwen3 32B), achieving $\sim 3	imes$ faster training steps on the same 24GB GPU.

---

## 4. Related Knowledge
- [Local Fine-Tuning Runbook](../procedures/local-fine-tuning.md)
- [Dynamic Quantization Methodology](../procedures/dynamic-quantization.md)
- [Unsloth Runtime Architecture](../runtimes/unsloth.md)
