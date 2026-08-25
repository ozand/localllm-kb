---
id: LLM-KB-RUNTIMES-UNSLOTH
title: "Unsloth AI and Studio runtime integration"
category: runtimes
tags: [unsloth, dynamic_quants, flex_attention, llama_cpp, vram_optimization]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, windows
  shell: bash, powershell
  tools: [python, unsloth, llama.cpp, sglang]
error_signatures:
  - "swiglu_limit = 7.0 not applied in MXFP4 inference"
  - "gemma3 attention scaling factor missing"
  - "loss infinity on float16 GPUs"
---

# Unsloth Runtime & Optimization Architecture

Unsloth provides highly optimized kernels, fine-tuning backends, and quantization
pipelines specifically tailored for local LLM execution, memory reduction, and
dynamic quantization.

## 1. Unsloth Dynamic Quantization (UD-*)

Unsloth Dynamic Quants (UD-Q4_K_S, UD-Q4_K_M, UD-Q8_0, etc.) replace uniform layer
quantization with per-layer sensitivity-aware precision assignment:

- **Dynamic Layer Selection**: Rather than uniformly quantizing every tensor to 4-bit,
  critical attention layers (e.g. `q_proj`, `v_proj`, down-projection) and initial/final
  layers are preserved at higher bitrates (5-bit to 8-bit), while less sensitive MoE expert
  layers or mid-layer MLP projections are compressed to 3-bit/4-bit.
- **Perplexity & MMLU Retention**: Retains significantly lower KL divergence compared to
  standard uniform GGUF quantizations.
- **Compatibility**: Dynamic GGUF artifacts run out-of-the-box in `llama.cpp`, `ollama`,
  `vLLM`, and `SGLang` without requiring proprietary plugins.

## 2. Flex Attention & Long-Context Scaling

Unsloth integrates PyTorch Flex Attention optimizations to eliminate KV cache and
intermediate activation bottlenecks during long-context operations:

- **>8× Longer Context**: Enables 60K–81K context fine-tuning and inference on single GPUs.
- **>50% VRAM Reduction**: Removes quadratic memory overheads in non-standard attention
  architectures (such as hybrid sliding window / global attention in Gemma 3 and Mistral Small 3.1).
- **SwiGLU & MXFP4 Fixes**: Enforces `swiglu_limit = 7.0` during MXFP4 inference (e.g. OpenAI gpt-oss)
  to prevent numeric overflow and NaN activations.

## 3. Architecture Specific Optimizations

- **MoE Dynamic 1.58-bit & 2.5-bit**: Dynamic routing quantization for DeepSeek V3/R1 and
  Nemotron architectures.
- **Multimodal SigLIP / Vision**: Direct vision encoder optimization for Gemma 3 and Qwen3.8.
- **Speculative Decoding Support**: Native support for draft-model generation and Multi-Token
  Prediction (MTP) acceleration.

## Related Records

- [Dynamic Quantization Procedures](../procedures/dynamic-quantization.md)
- [OpenAI gpt-oss-20b](../models/gpt-oss-20b.md)
- [Qwen3.8 27B](../models/qwen3.8-27b.md)
- [NVIDIA Nemotron 3.5](../models/nemotron-3.5-lightning.md)
- [Llama.cpp Runtime](llamacpp-qwen3.8.md)
