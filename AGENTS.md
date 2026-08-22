# Local LLM Knowledge Base — Agent Instructions

## Scope

This project stores reusable knowledge about locally hosted language models,
GGUF artifacts, quantization, llama.cpp/Unsloth runtimes, multimodal assets,
client compatibility, and validated operating procedures. Installed-software
and host infrastructure source-of-truth remains in `T:/Code/servers_team` and
its project-local documentation.

## Language

System files, metadata, and agent instructions are written in English.
User-facing summaries may be written in Russian.

## Knowledge layers

- `kb/raw/` — immutable or append-only source captures: official model cards,
  release notes, Reddit/forum discussions, sanitized runtime observations, and
  upstream command output. Do not treat raw captures as canonical facts without
  provenance and review.
- `kb/wiki/` — canonical OKF Markdown entries with stable IDs, frontmatter,
  source links, evidence status, and explicit scope.
- `kb/receipts/` — sanitized validation receipts for artifact, runtime, client,
  and regression checks. Never store API keys, raw prompts, private outputs,
  local absolute paths, or unsanitized logs.
- `kb/models/` — model-family and artifact records. Keep upstream identity,
  revision, filename, quantization, context claims, modality claims, and
  compatibility aliases separate.
- `kb/runtimes/` — llama.cpp, Unsloth Studio, LiteLLM, Pi, OpenCode, and client
  integration notes. Record runtime version and limitations separately from
  model capability.
- `kb/procedures/` — repeatable workflows for download, checksum verification,
  staged replacement, rollback, load/generate/unload, and client smoke tests.

## Required provenance

Every canonical model or artifact entry must distinguish:

1. upstream repository and immutable revision/commit;
2. upstream filename and local compatibility filename, if different;
3. checksum and byte size when an artifact was locally verified;
4. model capability claims versus runtime/client support;
5. validation date, environment class, and limitations.

Never infer that a local file is the newest upstream file merely because the
repository name is unchanged. Prefer explicit artifact filenames and hashes.

## QMD

## QMD Search Collections

This knowledge base is indexed in local QMD using two dedicated collections:
- `localllm-wiki` — Canonical OKF knowledge (models, runtimes, procedures, clients, receipts).
  - Search: `qmd search "<term>" -c localllm-wiki`
  - Query: `qmd query "<intent>" -c localllm-wiki`
- `localllm-raw` — Raw source captures, benchmarks, and Reddit dumps.
  - Search: `qmd search "<term>" -c localllm-raw`
  - Query: `qmd query "<intent>" -c localllm-raw`


Use the project-local `qmd.json` and `qmd/collections/` configuration for this
KB. Keep collections scoped to `kb/`; do not index the whole `T:/Code` tree from
this project. After adding or changing Markdown, run `qmd update` for the
configured collection and use targeted `qmd search`/`qmd query` checks.

## Safety

- Do not download or replace model artifacts without an approved Issue and an
  explicit execution request.
- Stage new artifacts separately; verify size/hash/metadata before replacement.
- Preserve a rollback artifact until acceptance is complete.
- Do not modify installed Studio packages from this repository.
- Do not publish secrets, API keys, raw private prompts, generated responses,
  local model paths, host inventories, or unsanitized logs.
- Do not claim multimodal support from model-card text alone: validate model,
  projector, runtime, API, and client layers independently.

## Verification

From this project root:

```bash
python -m pytest -q
kb-bootstrap validate --dir kb
qmd update
```

<!-- kb-bootstrap:repository-governance:start -->
## Repository routing and completion safety

- Expected repository: `ozand/localllm-kb`.
- Run `kb-bootstrap doctor --repo ozand/localllm-kb` before GitHub mutations.
- Use explicit `--repo` for every mutating `gh` command.
- Keep consumer-specific work in the consumer repository; use a separate verified checkout or worktree for upstream framework changes.
- Before completion claims, run `kb-bootstrap check-completion --repo ozand/localllm-kb --commit <commit> [--pr <number>]`.
- Fail closed on missing or mismatched repository, branch, pull request, or commit evidence.
- Never include credentials, private payloads, runtime checkpoints, or unsanitized logs in receipts.
<!-- kb-bootstrap:repository-governance:end -->
