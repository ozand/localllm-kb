---
id: LLM-KB-001
title: "Local LLM knowledge base architecture"
category: architecture
tags: [local-llm, knowledge-base, okf, qmd, provenance]
status: active
created: 2026-08-21
updated: 2026-08-21
environment:
  os: Windows
  shell: PowerShell or Bash
  tools: [kb-bootstrap, qmd]
error_signatures: []
---

# Local LLM knowledge base architecture

## Purpose

Keep durable knowledge about local language models separate from the operational
source of truth for installed software and infrastructure. The KB is a versioned
research and validation record, not a model directory and not a live control
plane.

## Layers

### Raw evidence

`kb/raw/` contains source captures such as official model cards, release notes,
upstream repository metadata, public issue discussions, and sanitized runtime
observations. Raw evidence is append-only where practical. It may remain local
if it contains sensitive operational context and must not be indexed as
canonical knowledge without review.

### Canonical wiki

`kb/wiki/` contains stable OKF Markdown pages. Each page states what is known,
what is inferred, what was validated locally, and what remains unknown. Pages
link to source material and validation receipts.

### Subject records

`kb/models/` describes model families and exact artifacts. `kb/runtimes/`
describes runtime behavior. `kb/clients/` describes client/API compatibility.
This prevents a model-card capability from being mistaken for support in one
specific runtime or client.

### Receipts

`kb/receipts/` stores sanitized, reproducible results for acquisition,
checksum, load, generation, context, KV-cache, multimodal, client, and rollback
checks. Receipts contain status and aggregate facts only; secrets, raw prompts,
private outputs, host inventory, and unsanitized logs are excluded.

## Provenance model

Every artifact record must distinguish:

1. upstream repository;
2. immutable revision or release;
3. upstream filename and local compatibility filename;
4. byte size and checksum when locally verified;
5. quantization, context, modality, and template claims;
6. runtime and client used for validation;
7. date, result, limitations, and rollback status.

Aliases are compatibility metadata. They must never erase the upstream artifact
identity.

## Lifecycle

1. **Discover** — collect official source metadata and public observations.
2. **Normalize** — convert raw evidence to OKF records with citations.
3. **Acquire** — stage an artifact outside the active model path.
4. **Verify** — check repository, revision, filename, size, checksum, metadata.
5. **Benchmark** — run bounded load/generation/context/feature checks.
6. **Integrate** — validate the serving runtime and client contracts.
7. **Promote** — update the canonical record and compatibility mapping.
8. **Retain rollback** — preserve the prior artifact until acceptance closes.
9. **Review** — record regressions, uncertainty, and next checks.

Artifact replacement requires a governing Issue and explicit execution approval.
The KB documents the procedure; it does not silently mutate a running service.

## Separation rule

The infrastructure repository may link to a KB record, but the KB must not copy
host secrets, launcher internals, private endpoints, or credentials. Conversely,
`servers_team` remains authoritative for how software is installed and started.
The KB is authoritative for model/artifact history and validated compatibility
claims.

## QMD policy

The `localllm-kb` collection indexes canonical `kb/` Markdown. Keep raw
captures excluded when they contain private operational data. Update the index
after canonical edits, then use collection-scoped search. Do not index the whole
workspace from this project.
