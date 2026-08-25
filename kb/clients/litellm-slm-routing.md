---
id: LLM-KB-CLIENTS-LITELLM-SLM
title: "LiteLLM local routing and small language model (SLM) orchestration"
category: clients
tags: [litellm, slm, routing, proxy, triage, latency_optimization]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: any
  shell: any
  tools: [litellm, llama.cpp, vllm, ollama]
error_signatures:
  - "litellm.exceptions.ContextWindowExceededError on SLM fallback"
  - "tool calling schema invalid on sub-3B model"
---

# LiteLLM Local SLM Routing & Proxy Architecture

Small Language Models (SLMs, 0.5B–14B) provide ultra-low latency (TTFT < 0.15s, >100–200 tok/s) and minimal VRAM requirements (1.5GB–12GB). LiteLLM acts as an intelligent proxy gateway, routing low-complexity subtasks to SLMs while escalating heavy reasoning and frontier queries to 20B–32B or 671B models.

## 1. SLM Cohort Profiles

| Model | Parameters | Q4_K_S (GB) | RTX 3090 TPS | TTFT (s) | Best Roles |
|---|---|---|---|---|---|
| **Qwen 2.5 0.5B** | 0.49B | 0.39 GB | ~210 tok/s | ~0.08s | Triage, Format Validation, Speculative Draft |
| **Qwen 2.5 1.5B** | 1.54B | 1.10 GB | ~175 tok/s | ~0.12s | Fast Router, Intent Classifier, Title Extractor |
| **Llama 3.2 1B** | 1.23B | 0.85 GB | ~185 tok/s | ~0.11s | Speculative Draft, Filter |
| **Llama 3.2 3B** | 3.21B | 2.10 GB | ~135 tok/s | ~0.18s | Structured Tool Calls, Concise Summaries |
| **Qwen 2.5 7B** | 7.61B | 4.68 GB | ~88 tok/s | ~0.28s | Primary Edge Coding, Single-File Edits |
| **Gemma 2 9B** | 9.24B | 5.80 GB | ~74 tok/s | ~0.35s | Knowledge Retrieval, Multi-turn Assistant |
| **Mistral NeMo 12B** | 12.2B | 7.50 GB | ~61 tok/s | ~0.42s | Multilingual Tasks, Context Reranking |
| **Qwen 2.5 14B** | 14.7B | 9.00 GB | ~52 tok/s | ~0.48s | Heavy Edge Orchestrator, Complex Tool Chains |

## 2. LiteLLM Multi-Tier Routing Configuration

Below is the canonical `config.yaml` for a tiered local deployment:

```yaml
model_list:
  # Tier 1: Ultra-fast Triage / Router (<0.15s)
  - model_name: router-triage
    litellm_params:
      model: openai/qwen2.5-0.5b
      api_base: http://localhost:8081/v1
      api_key: none

  # Tier 2: Structured Tool Caller & Edge Worker (<0.3s)
  - model_name: tool-worker
    litellm_params:
      model: openai/qwen2.5-7b
      api_base: http://localhost:8082/v1
      api_key: none

  # Tier 3: Primary Frontier Reasoning
  - model_name: frontier-coder
    litellm_params:
      model: openai/qwen3-30b-a3b
      api_base: http://localhost:8080/v1
      api_key: none

router_settings:
  routing_strategy: latency-based-routing
  fallbacks:
    - router-triage: ["tool-worker", "frontier-coder"]
    - tool-worker: ["frontier-coder"]
```

## 3. Key Agent Pipeline Patterns
- **Speculative Draft Acceleration**: Pair `qwen2.5-0.5b` as draft model with `qwen3-32b` in llama.cpp (`--draft-model qwen2.5-0.5b.gguf`) for 1.8x–2.4x speedup.
- **Context Summarization & Memory Compaction**: Route periodic rolling conversation summaries to `llama-3.2-3b`, offloading background maintenance from the main coding model.
