---
id: PROC-LLM-001
title: "Local model artifact acquisition and rollout"
category: procedure
tags: [gguf, artifact, checksum, rollback, validation]
status: active
created: 2026-08-21
updated: 2026-08-21
environment:
  os: Windows
  shell: PowerShell or Bash
  tools: [Hugging Face, sha256sum, Unsloth Studio, llama.cpp]
error_signatures: []
---

# Local model artifact acquisition and rollout

## Preconditions

- A governing Issue exists and is explicitly in progress.
- The target model, artifact variant, upstream repository, revision, and
  compatibility requirements are known.
- The active model and rollback path are identified.
- Runtime mutation is separately authorized.

## Staging

1. Query the official upstream repository and pin an immutable revision.
2. Download to a staging path outside the active model directory.
3. Record the upstream filename, expected byte size, and expected checksum.
4. Verify local byte size and SHA-256.
5. Inspect GGUF metadata without exposing local paths or private logs.
6. Stop or unload only the target inference process when the active file is
   memory-mapped; do not kill unrelated services.

## Compatibility replacement

1. Preserve the current artifact as a rollback copy.
2. Replace or map only the compatibility path required by existing clients.
3. Keep model IDs, profile IDs, aliases, scripts, launchers, and API contracts
   unchanged unless a separate migration explicitly approves changes.
4. Record that compatibility identity and upstream artifact identity differ.

## Validation gates

### Load gate

Load through the supported API and confirm a successful response, model
metadata, effective context, and health endpoint. A direct `llama-server`
check is supplemental, not a Studio integration proof.

### Generation gate

Send an authenticated, minimal, non-sensitive chat request and verify a
non-empty response. Use a fresh conversation for reasoning-loop tests.

### Context gate

Test below the configured context boundary with headroom. A request at or above
the nominal limit can be rejected even when the model's native context is larger.
Record effective and advertised context separately.

### Runtime gate

Record KV-cache configuration, speculative/MTP behavior, draft acceptance, and
lifecycle startup/unload status. Do not claim that absent profile flags guarantee
absent automatic runtime behavior.

### Client gate

Run separately bounded checks for API, LiteLLM, OpenCode, Pi, and browser/UI.
A passing backend request does not prove each client integration.

### Multimodal gate

Validate the projector, vision route, payload schema, runtime metadata, and
client independently. Do not repeat image tests until the projector and route
are known to be configured.

### Rollback gate

Before acceptance closes, restore the prior artifact in a controlled test or
prove that the rollback copy is intact and readable. Never delete rollback
material as routine cleanup.

## Reasoning budget

Numerical reasoning budgets are load-time settings. When supported, pass them
through the approved `llama_extra_args` path and reload the target inference
process. Suggested diagnostics are 2,048 for strict tests and 4,096–8,192 for
normal bounded tests; unrestricted thinking is not a stable acceptance gate.

## Evidence hygiene

Receipts may include status, aggregate timings, model alias, effective context,
KV-cache mode, and pass/fail results. Exclude API keys, raw prompts, generated
output, absolute paths, PIDs, host inventories, and unsanitized logs.
