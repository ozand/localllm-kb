---
id: pi-client-guide
title: Pi Coding Agent Integration with Qwen3.8-27B
category: client
status: canonical
tags: [pi, coding-agent, models.json, litellm, qwen3.8]
---

# Pi Coding Agent Integration with Qwen3.8-27B

## Overview
This document specifies how to configure the **Pi coding agent** (`@earendil-works/pi-coding-agent`) to use local instances of **Qwen3.8-27B**, either via a LiteLLM Proxy or directly against an OpenAI-compatible local server (llama.cpp / Unsloth Studio).

## Configuration (`~/.pi/agent/models.json`)

Pi resolves available models from `~/.pi/agent/models.json`. Add the local provider block under `providers`:

```json
{
  "providers": {
    "local-gateway": {
      "baseUrl": "http://127.0.0.1:4000/v1",
      "api": "openai-completions",
      "apiKey": "sk-local-dev",
      "models": [
        {
          "id": "local/qwen3.8-27b",
          "name": "Qwen3.8 27B (Local Reasoning)",
          "contextWindow": 98304,
          "maxTokens": 32768,
          "reasoning": true,
          "input": ["text"],
          "cost": {
            "input": 0,
            "output": 0,
            "cacheRead": 0,
            "cacheWrite": 0
          }
        },
        {
          "id": "local/qwen3.8-27b-instruct",
          "name": "Qwen3.8 27B (Local Instruct / Non-Thinking)",
          "contextWindow": 98304,
          "maxTokens": 8192,
          "reasoning": false,
          "input": ["text"],
          "cost": {
            "input": 0,
            "output": 0,
            "cacheRead": 0,
            "cacheWrite": 0
          }
        }
      ]
    }
  }
}
```

## Critical Configuration Settings

1. **Reasoning Separation (`reasoning: true`)**:
   - Setting `"reasoning": true` signals Pi that the model outputs thinking steps inside `<thought>...</thought>` or channel blocks.
   - Pi extracts thought traces for UI folding and feeds only final tool invocations into the harness pipeline.
2. **Context Window Ceiling**:
   - Set `"contextWindow": 98304` to maintain safe GPU headroom on the 24GB VRAM host.
3. **Tool Calling Reliability**:
   - In Thinking mode, Qwen3.8 outputs JSON tool calls after completing reasoning steps.
   - Ensure the runtime prompt template maps tool definitions into the `<|im_start|>system` role using standard Qwen tool formatting.

## References
- [LiteLLM Integration Guide](litellm.md)
- [Qwen3.8-27B Model Profile](../models/qwen3.8-27b.md)
- [Integration Test Receipt](../receipts/qwen3.8-pi-litellm.md)
