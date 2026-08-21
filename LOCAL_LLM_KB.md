# Local LLM Knowledge Base

This checkout uses `ozand/kb-bootstrap` as the bootstrap framework and adds a
project-specific knowledge layer for locally hosted language models.

## Boundary

`T:/Code/servers_team` remains the source of truth for installed software,
host infrastructure, launchers, secrets policy, and live service operations.
This project records reusable model knowledge: upstream model identity,
artifacts, quantization, runtime behavior, client compatibility, benchmarks,
known limitations, and rollback/validation procedures.

The first subject is Qwen3.8 27B served locally through Unsloth Studio and the
llama.cpp-compatible runtime.

## Layout

- `kb/raw/` — local-only source captures and sanitized raw observations.
- `kb/wiki/` — canonical architecture and cross-cutting knowledge.
- `kb/models/` — model families, artifacts, aliases, and provenance.
- `kb/runtimes/` — runtime-specific behavior and version-qualified limits.
- `kb/clients/` — Pi, OpenCode, LiteLLM, OpenAI-compatible API, and UI checks.
- `kb/procedures/` — repeatable acquisition, validation, rollout, and rollback.
- `kb/receipts/` — local-only sanitized validation receipts.
- `qmd/collections/` — intended collection configuration for searchable KB
  content; the active QMD registration is the `localllm-kb` collection.

## Operating rule

A model claim is not a runtime claim. Every canonical entry must identify its
source authority, validation status, environment class, and limitations. Raw
captures are evidence inputs, not canonical truth.

See [`kb/wiki/architecture.md`](kb/wiki/architecture.md) for the full model and
artifact lifecycle and [`kb/models/qwen3.8-27b.md`](kb/models/qwen3.8-27b.md)
for the initial subject record.

## Verification

```text
python -m pytest -q
kb-bootstrap validate --dir kb
qmd update
qmd search "Qwen3.8" -c localllm-kb --no-rerank
```

Do not place GGUF files, checkpoints, credentials, raw private prompts,
unsanitized logs, or absolute host paths in this repository.
