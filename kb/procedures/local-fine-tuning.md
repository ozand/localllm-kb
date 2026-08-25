---
id: LLM-KB-PROC-LOCAL-FINETUNING
title: "Local LLM Fine-Tuning and Continual Pretraining"
category: procedures
tags: [unsloth, qlora, lora, fine-tuning, contpretraining, grpo, vision_rl]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, windows
  shell: bash, powershell
  tools: [python, unsloth, trl, pytorch]
error_signatures:
  - "CUDA out of memory during backward pass"
  - "gradient checkpointing slowing down step time by 3x"
  - "catastrophic forgetting during continuous pretraining"
---

# Local LLM Fine-Tuning and Continuous Pretraining Runbook

## Overview

Based on verified research and Triton kernel optimizations from Unsloth AI,
local fine-tuning and continuous pretraining can achieve 2x–5x training speedups
and 60%–80% VRAM reductions on consumer hardware (e.g. single RTX 3090 / 4090 24GB).

## 1. Parameter-Efficient Fine-Tuning (LoRA & QLoRA)

### A. Target Modules
For maximum performance without VRAM explosion, attach LoRA adapters to:
- Attention projections: `q_proj`, `k_proj`, `v_proj`, `o_proj`
- MLP / FFN projections: `gate_proj`, `up_proj`, `down_proj`

### B. 4-bit Quantized Base Models (QLoRA)
- Unsloth integrates custom 4-bit dequantization Triton kernels directly into
  the forward pass, avoiding FP16 upcasting memory spikes.
- Enables fine-tuning 70B parameter models (e.g. Llama 3 70B) on 2x24GB GPUs or
  14B/32B models on a single 24GB GPU with batch size >= 2.

## 2. Continuous Pretraining on Raw Text

To teach a model an entirely new language, domain corpus, or documentation:
1. **Unembedding & Embedding Resizing**: Ensure new vocabulary tokens are initialized
   with normal distribution matching existing embedding weights.
2. **Learning Rate & Schedule**: Use 1/5th to 1/10th of standard SFT learning rate
   (e.g., `5e-5` down to `1e-5`) with cosine warmup.
3. **Loss Masking**: Do not mask prompt tokens; compute cross-entropy loss across
   the entire context sequence.

## 3. Local Reinforcement Learning (GRPO & Reasoning Models)

### A. Group Relative Policy Optimization (GRPO)
- Eliminates the separate critic / value model required by PPO, saving 50% VRAM.
- Generates multiple candidate completions per prompt (group size $G=4..8$).
- Computes reward normalizations within the group to calculate policy gradients.

### B. Local Reasoning Emergence
- Reward functions must be rule-based / verifiable (e.g. XML format checker,
  regex verification, Python AST syntax validator).
- Models self-discover `<think>...</think>` tokens when given length incentives
  combined with deterministic correctness verification.

## 4. Multimodal & Vision-RL Fine-Tuning

- Freeze vision encoder weights during initial instruction tuning.
- Train vision-language adapter / projector layers alongside text attention blocks.
- In GRPO for visual reasoning, feed image tokens through frozen projector and
  evaluate candidate responses using visual bounding-box / OCR verifiers.

## 5. Verification Commands

```bash
python -c "import unsloth; print(unsloth.__version__)"
```
