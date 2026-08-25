---
id: LLM-KB-RECEIPT-OPENNESS-FINETUNING
title: "Receipt: Openness Index Cross-Reference & Local Adaptation Validation"
category: receipt
tags: [receipt, openness, fine-tuning, feasibility, validation]
status: active
created: 2026-08-25
updated: 2026-08-25
environment:
  os: any
  shell: any
  tools: [pytest, kb-bootstrap]
error_signatures: []
---

# Receipt: Openness Index Cross-Reference & Local Adaptation Validation

## 1. Artifact Verification
- Canonical Wiki Page: `kb/wiki/openness-finetuning-matrix.md`
- Raw Research Analysis: `kb/raw/research/openness-finetuning-analysis.json`
- Target Model Coverage: 10 Cohort Models + DeepSeek V3 671B.

## 2. Feasibility Findings Summary
1. **Open-Weights vs Truly Open Source**: 90% of frontier open models provide open weights without pretraining data mixtures or pretraining code. OpenAI gpt-oss-20b provides the highest level of training recipe transparency in the cohort.
2. **1x 24GB RTX 3090 Capability**: Supports QLoRA fine-tuning up to 32B dense / 30B MoE with `paged_adamw_8bit` and gradient checkpointing.
3. **GRPO on Single GPU**: Feasible on Qwen3.8 27B and gpt-oss-20b using 4-bit base weights and unsloth fast-inference draft acceleration.

## 3. Knowledge Graph Integrity
- Node Count: 61 Markdown documents.
- Connected Subgraphs: 1 (fully connected).
- Dead Links: 0.
- Orphans: 1 (root `wiki/index.md`).
