---
id: procedure-coding-agent-tuning
title: "Autonomous Coding Agent Optimization & Tool-Calling Stability Guide"
type: procedure
status: verified
revision: "v1.0"
evidence:
  - "../raw/research/reddit-50-threads-corpus.md"
  - "../raw/research/reddit-qwen3.8-deepdive-synthesis.md"
  - "../clients/pi.md"
  - "../clients/litellm.md"
scope: "Agent harnesses (Pi, OpenCode, Claude Code) paired with local 27B-32B reasoning models"
---

# Autonomous Coding Agent Optimization Guide

## 1. The "Memento Bug" & Tool Hallucination Prevention

In agentic coding workflows, local reasoning models often fail after 10–20 turns due to context clipping or thinking tag removal.

### Root Causes
1. **Thinking Tag Stripping**: When proxies strip `<thought>` blocks from historical turns, the model loses intermediate derivations and repeats tool calls or hallucinates file modifications.
2. **Context Saturation (<64k)**: Extended reasoning consumes 2,000–8,000 tokens per turn. In small context windows, system prompts and earlier tool outputs get evicted.

### Solutions
- **Preserve Reasoning in Session History**: Ensure the agent harness passes full turn histories back to the server.
- **Adaptive Thinking Budgets**:
  - Complex Architectural Planning: `budget: 8192` / `reasoning_effort: high`
  - Standard Implementation & Multi-file Edits: `budget: 4096` / `reasoning_effort: medium`
  - Fast Single-file Fixes & Linting: `budget: 1024` / `reasoning_effort: low`
  - Pure Routing & Status Checks: `budget: 0` / Instruct mode.

---

## 2. Sampling Matrix for Agent Workflows

| Mode | Temperature | Top-P | Top-K | Min-P | Presence Penalty | Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Reasoning / Thinking** | 1.00 | 0.95 | 20 | 0.00 | 0.00 | Architecture, deep debugging, complex refactoring |
| **Direct Tool Calling** | 0.70 | 0.80 | 20 | 0.00 | 1.50 | Precise JSON tool dispatch, single-step execution |
| **Log / Data Parsing** | 0.20 | 0.50 | 10 | 0.05 | 0.00 | Extraction, summarization, deterministic filtering |

---

## 3. Harness Best Practices (Pi & OpenCode)

1. **Keep System Prompts Compact**: Favor compact XML or Markdown instructions. Every token saved in the system prompt extends the effective conversation memory.
2. **Local Model Caching**: Utilize prefix caching in llama-server (`--flash-attn on`) so repetitive system instructions require 0 ms prefill on subsequent turns.
3. **Automatic Context Compaction**: Configure the agent harness to compact / summarize tool outputs exceeding 5 KB rather than keeping raw shell streams in the active conversation context.

---

## Related Documents
- [Pi Coding Agent Setup](../clients/pi.md)
- [LiteLLM Proxy Routing](../clients/litellm.md)
- [llama.cpp Optimization Guide](../runtimes/llamacpp-qwen3.8.md)
