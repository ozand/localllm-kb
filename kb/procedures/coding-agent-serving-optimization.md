---
id: LLM-KB-PROCEDURES-CODING-AGENT-SERVING
title: "Serving and prefix caching optimization for coding agents"
category: procedures
tags: [coding_agents, prefix_caching, prompt_eval, ttft, pi, opencode]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: linux, windows
  shell: bash, powershell
  tools: [llama.cpp, vllm, sglang, unsloth, litellm]
error_signatures:
  - "prefix cache invalidated by dynamic tool schemas"
  - "excessive TTFT in multi-turn tool loops"
---

# Serving & Prefix Caching Optimization for Coding Agents

Autonomous coding agents (Pi, OpenCode, Claude Code, Cursor CLI, Aider) place unique demands
on local LLM serving backends compared to standard chat interfaces.

## 1. The Multi-Turn Prefix Caching Problem

Coding agent interactions generate rapidly growing context (system prompts, tool definitions,
file reads, bash outputs, turn history). In unoptimized setups, every new turn re-evaluates the
entire context from token 0:

- **Without Prefix Caching**: Turn $N$ prompt eval latency scales $O(N)$ with total context size, causing 10s-60s TTFT delays per tool step.
- **With Deterministic Prefix Caching**: Prompt eval scales $O(\Delta N)$ (only newly added user/tool output tokens evaluated), reducing TTFT to <1.5s.

## 2. Server Configuration Best Practices

### llama.cpp (`llama-server`)
```bash
llama-server -m /models/Qwen3.8-27B-UD-Q4_K_S.gguf   --ctx-size 98304   --n-gpu-layers 99   --prompt-cache /models/cache/qwen38.cache   --prompt-cache-all   --cache-type-k q8_0   --cache-type-v q8_0   --parallel 1   --threads 16   --host 0.0.0.0 --port 8080
```
- `--prompt-cache-all`: Essential for agent harnesses to cache intermediate turn prefixes.
- `--cache-type-k/v q8_0`: Prevents KV cache OOM at 98K tokens while preserving attention precision.

### SGLang / vLLM (RadixAttention & Chunked Prefill)
- Enable `--enable-prefix-caching` in vLLM or RadixAttention in SGLang.
- Set `--chunked-prefill-size 2048` to prevent GPU lockup during large context prefill.

## 3. Harness System Prompt & Tool Placement Constraints
To maximize prefix cache hit rate (>90%):
1. **Static System Prompt**: Place system prompt and immutable rules at token 0.
2. **Fixed Tool Definitions**: Do not dynamically reorder or modify tool JSON schemas between turns.
3. **Append-Only History**: Structure file reads and command outputs as strictly appended turns.

## 4. Reasoning-Effort Parameter Constraints
For reasoning models (DeepSeek R1, gpt-oss-20b):
- **High reasoning effort**: Produces 2,000-8,000 thinking tokens before each tool call. Latency overhead is 3x-6x standard generation.
- **Low/Medium reasoning effort**: Recommended for iterative tool loops (file reading, grepping) to keep agent turn latency under 15 seconds.
