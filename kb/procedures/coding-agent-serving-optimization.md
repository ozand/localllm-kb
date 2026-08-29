---
id: LLM-KB-PROCEDURES-CODING-AGENT-SERVING
title: "Serving and prefix caching optimization for coding agents"
category: procedures
tags: [coding_agents, prefix_caching, prompt_eval, ttft, pi, opencode]
status: active
created: 2026-08-25
updated: 2026-08-29
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

**Evidence status:** `reported_community_partial` / bounded receipt observation. These complexity descriptions explain the intended mechanism; they do not establish a universal latency formula or target. See the [coding-agent serving receipt](../receipts/coding-agent-serving-receipt.md).

- **Without Prefix Caching:** Re-evaluating an append-only context can increase prompt-processing work as the context grows. The existing receipt reports 10s–60s TTFT delays in some tool loops; model, runtime version, hardware, context, workload, and measurement method are not universal and must be recorded for any reuse.
- **With Deterministic Prefix Caching:** Reusing an unchanged prefix can reduce the amount of prompt processing required for a later turn. The existing receipt reports sub-1.5s TTFT in one bounded setup; this is not a general guarantee across backends or harnesses.

## 2. Server Configuration Best Practices

### llama.cpp (`llama-server`)
```bash
llama-server -m /models/Qwen3.8-27B-UD-Q4_K_S.gguf   --ctx-size 98304   --n-gpu-layers 99   --prompt-cache /models/cache/qwen38.cache   --prompt-cache-all   --cache-type-k q8_0   --cache-type-v q8_0   --parallel 1   --threads 16   --host 0.0.0.0 --port 8080
```
- `--prompt-cache-all`: Useful when the harness emits reusable intermediate turn prefixes; whether it is effective depends on prompt stability and runtime behavior.
- `--cache-type-k/v q8_0`: A configuration option for reducing KV-cache storage. The earlier `98K` OOM-prevention statement is a bounded, runtime/model-specific claim, not a universal guarantee; exact memory impact and output behavior are `unknown` without a matching measurement.

### SGLang / vLLM (RadixAttention & Chunked Prefill)
- Enable `--enable-prefix-caching` in vLLM or RadixAttention in SGLang.
- Set `--chunked-prefill-size 2048` to prevent GPU lockup during large context prefill.

## 3. Harness System Prompt & Tool Placement Constraints
To maximize prefix cache hit rate (the earlier `>90%` value is a reported target, not a guaranteed result; actual hit rate is `unknown` until measured for the specific harness and workload):
1. **Static System Prompt**: Place system prompt and immutable rules at token 0.
2. **Fixed Tool Definitions**: Do not dynamically reorder or modify tool JSON schemas between turns.
3. **Append-Only History**: Structure file reads and command outputs as strictly appended turns.

## 4. Reasoning-Effort Parameter Constraints
For reasoning models (DeepSeek R1, gpt-oss-20b):
- **High reasoning effort:** The existing receipt reports 2,000–8,000 thinking tokens before some tool calls and 3x–6x latency overhead in a bounded setup. Exact token counts and overhead depend on model, runtime, reasoning policy, hardware, workload, and output; these conditions are otherwise `unknown`.
- **Low/Medium reasoning effort:** A reported operational recommendation for iterative tool loops; the earlier under-15-second target is not a universal guarantee.
