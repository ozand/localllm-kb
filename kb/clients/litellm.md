---
id: litellm-client-guide
title: LiteLLM Gateway Integration Guide
category: client
status: canonical
tags: [litellm, gateway, openai-compatible, routing, qwen3.8]
---

# LiteLLM Gateway Integration Guide

## Overview
This document outlines the architecture and configuration for integrating local LLM runtimes (Unsloth Studio / llama.cpp) running **Qwen3.8-27B** behind a [LiteLLM Proxy](https://docs.litellm.ai/).

LiteLLM acts as the central API gateway, standardizing model names, managing request fallbacks, sanitizing context length constraints, and mapping thinking/reasoning parameters for client harnesses like Pi and OpenCode.

## Architecture

```
+-----------------------------------------------------------+
|                   Client Applications                     |
|           (Pi Coding Agent, OpenCode, Codex, Aider)       |
+-----------------------------+-----------------------------+
                              | OpenAI-compatible API
                              v
+-----------------------------------------------------------+
|                      LiteLLM Proxy                        |
|   - Route Aliases: local/qwen3.8-27b, local/qwen-instruct |
|   - Thinking Budgets: pass-through & clamping             |
|   - Context Window enforcement (98k safe ceiling)         |
+-----------------------------+-----------------------------+
                              | Upstream HTTP / OpenAI API
                              v
+-----------------------------------------------------------+
|                 Local Runtime (Host Port 8000)            |
|   - llama.cpp server / Unsloth Studio                     |
|   - GPU Offload: RTX 3090 Ti (24GB VRAM)                  |
|   - Model: Qwen3.8-27B-UD-Q4_K_S.gguf                     |
+-----------------------------------------------------------+
```

## Recommended `config.yaml` for LiteLLM

```yaml
model_list:
  # Thinking / Deep Reasoning Route (Default for complex coding & architecture)
  - model_name: local/qwen3.8-27b
    litellm_params:
      model: openai/qwen3.8-27b
      api_base: http://127.0.0.1:8000/v1
      api_key: "sk-local-no-key-required"
      max_tokens: 32768
      max_input_tokens: 98304
      temperature: 1.0
      top_p: 0.95
      extra_body:
        top_k: 20
        min_p: 0.0

  # Instruct / Fast Non-Thinking Route (For quick file edits, tool loops, routing)
  - model_name: local/qwen3.8-27b-instruct
    litellm_params:
      model: openai/qwen3.8-27b
      api_base: http://127.0.0.1:8000/v1
      api_key: "sk-local-no-key-required"
      max_tokens: 8192
      max_input_tokens: 98304
      temperature: 0.7
      top_p: 0.80
      extra_body:
        top_k: 20
        presence_penalty: 1.5
        # Disable thought generation in runtime
        reasoning_budget: 0

router_settings:
  routing_strategy: simple-shuffle
  timeout: 300
```

## Parameter Mapping & Rules

1. **Context Window Protection**:
   - Upstream engine advertises 262k tokens, but on a 24GB VRAM GPU with `q8_0` KV-cache, hard-cap the proxy route at `max_input_tokens: 98304` to avoid CUDA OOM during active multi-turn turns.
2. **Thinking Budget Pass-Through**:
   - When requests come with `reasoning_effort` (e.g. low/medium/high), map them to `extra_body.llama_extra_args` or pass `reasoning_budget` integers (2048 / 4096 / 8192) without patching runtime engine files.

## References
- [Qwen3.8-27B Model Profile](../models/qwen3.8-27b.md)
- [Pi Client Guide](pi.md)
