---
id: procedure-research-corpus-parity
title: Research corpus parity and local staging cleanup
category: procedure
status: validated
date: 2026-08-22
tags: [research, provenance, sanitizer, publication, git]
---

# Research corpus parity and local staging cleanup

## Policy

`kb/raw/research/published/` is the Git-authoritative sanitized corpus. A local collection run may use `kb/raw/research/` as temporary staging, but it must not remain as a second unpublished source of truth after publication.

Before cleanup:

1. enumerate all local staging files;
2. compare relative file sets with `published/`;
3. compare SHA-256 values and classify equal versus sanitizer-transformed content;
4. parse every JSON artifact;
5. audit the published copy with `sanitize_artifacts.py audit`;
6. preserve the published copy in Git;
7. obtain explicit approval before deleting or relocating local staging files.

## Required final state

- every research artifact is represented under `kb/raw/research/published/`;
- no local-only research files remain outside `published/`;
- no source capture is overwritten by the sanitizer;
- parity and cleanup counts are recorded in a sanitized receipt;
- future reruns repeat the audit/publication/cleanup sequence.

## Sanitized publication sequence

```bash
python .agents/skills/reddit-deep-research/scripts/sanitize_artifacts.py audit \
  --input <staging-directory>

python .agents/skills/reddit-deep-research/scripts/sanitize_artifacts.py sanitize \
  --input <staging-directory> \
  --output kb/raw/research/published

python .agents/skills/reddit-deep-research/scripts/sanitize_artifacts.py audit \
  --input kb/raw/research/published
```

Only after the final audit and JSON validation pass may the approved local staging cleanup run. Do not use broad repository cleanup commands; delete only the explicitly enumerated staging files outside `published/`.
