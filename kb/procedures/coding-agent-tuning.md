---
id: procedure-coding-agent-tuning
title: "Autonomous Coding Agent Optimization & Tool-Calling Stability Guide"
type: procedure
status: active
revision: "v1.1"
evidence:
  - "../raw/research/reddit-50-threads-corpus.md"
  - "../raw/research/reddit-qwen3.8-deepdive-synthesis.md"
  - "../clients/pi.md"
  - "../clients/litellm.md"
scope: "Agent harnesses (Pi, OpenCode, Claude Code) paired with local 27B-32B reasoning models"
evidence_status: reported_community_partial
limitations: "Numeric budgets, thresholds, and latency statements are scoped starting points or reported observations; they are not universal tuning guarantees."
---

# Autonomous Coding Agent Optimization Guide

## 1. The "Memento Bug" & Tool Hallucination Prevention

In agentic coding workflows, the cited corpus reports failures after 10–20 turns in some setups due to context clipping or thinking-tag removal. This is a reported observation, not a universal turn threshold; model, runtime, context, harness, workload, and failure-detection method are otherwise `unknown`.

### Root Causes
1. **Thinking Tag Stripping**: When proxies strip `<thought>` blocks from historical turns, the model loses intermediate derivations and repeats tool calls or hallucinates file modifications.
2. **Context saturation:** The cited corpus reports a `<64k` context as a risk condition and `2,000–8,000` reasoning tokens per turn in some workflows. These figures are `reported_community_partial`; model, runtime/version, context accounting, workload, and harness are `unknown` here. Do not treat them as universal boundaries.

### Solutions
- **Preserve Reasoning in Session History**: Ensure the agent harness passes full turn histories back to the server.
- **Adaptive thinking budgets (reported starting points):**
  - Complex Architectural Planning: `budget: 8192` / `reasoning_effort: high`
  - Standard Implementation & Multi-file Edits: `budget: 4096` / `reasoning_effort: medium`
  - Fast Single-file Fixes & Linting: `budget: 1024` / `reasoning_effort: low`
  - Pure Routing & Status Checks: `budget: 0` / Instruct mode.

  These values are not measured optima. Appropriate budgets depend on the selected model, provider/runtime, harness, task, context, and output policy; exact conditions are `unknown` unless recorded by a matching receipt.
---

## 2. Sampling Matrix for Agent Workflows

The matrix is a reported starting-point configuration, not a universal optimum. Evidence status: `reported_community_partial`; model, runtime/version, task distribution, evaluation method, and output-quality criteria are `unknown` unless separately recorded.

| Mode | Temperature | Top-P | Top-K | Min-P | Presence Penalty | Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Reasoning / Thinking** | 1.00 | 0.95 | 20 | 0.00 | 0.00 | Architecture, deep debugging, complex refactoring |
| **Direct Tool Calling** | 0.70 | 0.80 | 20 | 0.00 | 1.50 | Precise JSON tool dispatch, single-step execution |
| **Log / Data Parsing** | 0.20 | 0.50 | 10 | 0.05 | 0.00 | Extraction, summarization, deterministic filtering |

---

## 3. Harness Best Practices (Pi & OpenCode)

1. **Keep System Prompts Compact**: Favor compact XML or Markdown instructions. Every token saved in the system prompt extends the effective conversation memory.
2. **Local Model Caching**: Consider prefix caching in llama-server (`--flash-attn on`) when the runtime supports the selected configuration and the prompt prefix is stable. The earlier `0 ms prefill` wording is unsupported as a universal claim; actual prompt-processing time, cache hit behavior, and hardware/runtime conditions are `unknown` until measured.
3. **Automatic Context Compaction**: A reported starting point is to compact or summarize tool outputs exceeding `5 KB`; the threshold is workload- and harness-specific, not a universal limit. Preserve provenance and avoid treating compaction as lossless without validation.

---

## Related Documents
- [Pi Coding Agent Setup](../clients/pi.md)
- [LiteLLM Proxy Routing](../clients/litellm.md)
- [llama.cpp Optimization Guide](../runtimes/llamacpp-qwen3.8.md)
