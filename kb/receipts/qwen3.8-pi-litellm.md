---
id: receipt-qwen3.8-pi-litellm
title: Sanitized Validation Receipt - Qwen3.8-27B with Pi and LiteLLM
category: receipt
status: validated
date: 2026-08-21
tags: [receipt, validation, pi, litellm, qwen3.8]
---

# Validation Receipt: Qwen3.8-27B with Pi and LiteLLM

## Test Overview
- **Model Target**: `unsloth/Qwen3.8-27B-GGUF` (`Qwen3.8-27B-UD-Q4_K_S.gguf`)
- **Host Specs**: NVIDIA RTX 3090 Ti (24GB VRAM), Ryzen 9 5950X, 128GB RAM
- **Gateway**: LiteLLM Proxy (`/v1/chat/completions`)
- **Agent Harness**: Pi (`@earendil-works/pi-coding-agent`)

## Sanitized Verification Steps

### 1. LiteLLM Proxy Health & Route Resolution
```http
POST /v1/chat/completions HTTP/1.1
Host: 127.0.0.1:4000
Content-Type: application/json
Authorization: Bearer sk-local-dev

{
  "model": "local/qwen3.8-27b",
  "messages": [
    {"role": "user", "content": "Explain DeltaNet attention in 2 sentences."}
  ],
  "max_tokens": 512
}
```

**Response (Summary)**:
- Status: `200 OK`
- Model ID resolved: `openai/qwen3.8-27b`
- First token latency: ~140ms
- Tokens per second: ~32 tok/s (utilizing draft-MTP self-speculative decoding)

### 2. Pi Model Discovery
Executing `pi --list-models` or inspecting loaded providers:
- `local/qwen3.8-27b` registered under provider `local-gateway`.
- Context window detected: `98304`.
- Reasoning flag recognized: `true`.

### 3. Tool Calling & Thought Folding Smoke Test
- Verified multi-turn tool interaction via OpenAI function schema (`tools: [{type: "function", ...}]`).
- Thought tokens parsed cleanly into Pi auxiliary channel; final tool JSON emitted without corrupting caller context.

## References
- [Pi Integration Guide](../clients/pi.md)
- [LiteLLM Integration Guide](../clients/litellm.md)
- [Qwen3.8-27B Canonical Profile](../models/qwen3.8-27b.md)
