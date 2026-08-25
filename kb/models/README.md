---
id: LLM-KB-MODELS
title: "Local model records"
category: index
tags: [models, artifacts, provenance, cohort]
status: active
created: 2026-08-21
updated: 2026-08-23
environment:
  os: any
  shell: any
  tools: []
error_signatures: []
---

# Models

Canonical OKF profiles for locally hosted LLM architectures and GGUF artifacts:

### Cohort Model Profiles
- [Qwen3.8 27B (xhigh)](qwen3.8-27b.md) — Dense Multimodal (Text + Vision), MTP speculative draft decoding, 160k context.
- [Qwen3 32B Instruct](qwen3-32b.md) — Dense 32.8B instruction model, 128k context, GQA 8 KV heads.
- [Qwen3 30B A3B Instruct](qwen3-30b-a3b.md) — Sparse MoE (30.5B total / 3.3B active), 4 KV heads, 98k fits single 24GB GPU.
- [Qwen3 Coder 30B A3B Instruct](qwen3-coder-30b-a3b.md) — Sparse MoE Coder (30.5B total / 3.3B active), 262k context, direct code generation.
- [Qwen2.5 32B Instruct](qwen2.5-32b.md) — Dense 32.5B baseline instruction model, 128k context, stable predictable generation.
- [DeepSeek R1 Distill Qwen 32B](deepseek-r1-distill-qwen-32b.md)
- [DeepSeek V3 (671B MoE)](deepseek-v3-671b.md) — Dense 32.5B reasoning model with `<think>` trace generation.
- [Gemma 3 27B Instruct](gemma3-27b.md) — Dense 27.2B multimodal model with SigLIP vision projector, 16 KV heads.
- [Mistral Small 3.1 24B Instruct](mistral-small-3.1-24b.md) — Dense 24.0B multimodal model, fast ~33.2 TPS throughput, 98k fits 24GB with Q4 KV.
- [OpenAI gpt-oss-20b](gpt-oss-20b.md) — Sparse MoE (21B total / 3.6B active), native MXFP4, ultra-compact 11.62GB weights, ~65.4 TPS.
- [NVIDIA Nemotron 3.5 Lightning 30B A3B](nemotron-3.5-lightning.md) — Hybrid Linear Mamba-2 SSM + MoE + Attention, sub-quadratic context scaling.

### Cross-Model Matrices & Procedures
- [Research Corpus Parity Procedure](../procedures/research-corpus-parity.md)
- [LiteLLM Integration](../clients/litellm.md)
- [Pi Coding Agent Integration](../clients/pi.md)
