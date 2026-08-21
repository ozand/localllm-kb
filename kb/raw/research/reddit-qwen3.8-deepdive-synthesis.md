---
source: "https://www.reddit.com/r/LocalLLaMA/"
title: "Deep Dive Reddit Synthesis: Qwen 3.8 27B Configurations, MTP Speeds, Jinja Templates, and Agent Harnesses"
capture_date: "2026-08-21"
quality_score: 0.95
tags: [reddit, local-llm, qwen, llama-cpp, pi-agent, litellm, mtp, mmproj, benchmarks]
---

# Deep Dive Reddit Community Synthesis: Qwen 3.8 27B

Synthesized from multiple high-signal r/LocalLLaMA discussions, empirical community benchmarks, and bug reports.

---

## 1. Verified Breakthrough Configurations (llama-server)

From the benchmark report by user `dsdt` hitting up to **70 tokens/sec** on single GPU using Multi-Token Prediction (MTP):

```bash
llama-server.exe \
  -m "models/Qwen3.8-27B-UD-Q4_K_S.gguf" \
  --mmproj "models/mmproj-BF16.gguf" \
  --jinja \
  --chat-template-kwargs "{\"reasoning_effort\":\"medium\"}" \
  --reasoning on \
  --reasoning-preserve \
  -c 98304 \
  --flash-attn on \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --spec-type draft-mtp,ngram-mod \
  --spec-draft-n-max 2 \
  --spec-ngram-mod-n-match 24 \
  --spec-ngram-mod-n-min 24 \
  --spec-ngram-mod-n-max 86 \
  -t 16 \
  --batch-size 1024 \
  --ubatch-size 512
```

### Key Parameter Explanations
* `--spec-type draft-mtp,ngram-mod`: Combines model-internal multi-token prediction heads with n-gram repetition matching, giving +35% to +65% tok/s generation throughput without external draft models.
* `--reasoning-preserve`: Prevents thinking state destruction during multi-turn conversational compaction.
* `--cache-type-k q8_0 --cache-type-v q8_0`: Retains numeric precision for code/JSON syntax while fitting 98k context on 24GB VRAM.

---

## 2. Agent Harness Comparison Poll (4.3k Community Votes)

From poll `r/LocalLLaMA/comments/1vpdrxl/`:
* **Pi Coding Agent**: #1 Choice (1,800 votes) — Praised for low token overhead, clean terminal UI, and robust handling of tool execution loops.
* **OpenCode**: #2 Choice (1,500 votes) — Strong multi-provider support and project indexing.
* **Continue / Roo / Cline**: Falling behind due to token waste and verbose prompt padding that triggers context degradation on 27B models.

---

## 3. Tool Calling Failures & The "Thinking Loop" Trap

From thread `r/LocalLLaMA/comments/1uue278/`:
* **Root Cause**: When agent harnesses strip `<think>` blocks or fail to pass `--reasoning-preserve`, Qwen 3.8 loses track of prior reasoning steps and attempts to emit raw tool calls inside new thinking tags or enters infinite repetition loops.
* **Fix**:
  1. Ensure Jinja template renders native `<think>...</think>` tokens without regex stripping.
  2. Set LiteLLM to preserve reasoning tokens in message history.
  3. Maintain minimum 64k-98k context to prevent early compaction.

---

## 4. Multimodal & Video Processing Status

* **mmproj Support**: Requires `mmproj-BF16.gguf` loaded via `--mmproj`.
* **Video Ingestion**: Qwen 3.8 natively supports video frames sampled at 1-2 FPS. Llama.cpp CLI/server accepts images and frame sequences through the vision projector.
* **VRAM Overhead**: Adding `mmproj` requires ~1.2 GB additional VRAM. On RTX 3090 Ti (24GB), running with `UD-Q4_K_S` + `q8_0` KV allows full vision inference with up to 64k context.

---

## 5. Next Hypotheses & Follow-up Investigations

1. **Hypothesis**: YaRN RoPE scaling (`--rope-scaling yarn --rope-freq-scale 0.25`) can extend Qwen 3.8 from 98k to 262k/500k context with acceptable perplexity by offloading KV-cache to 128GB CPU RAM.
2. **Hypothesis**: SGLang with RadixAttention provides superior prefix caching compared to llama.cpp for multi-turn Pi agent sessions.
