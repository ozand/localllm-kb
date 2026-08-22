---
id: receipt-research-corpus-parity-2026-08-22
title: Research corpus parity and staging cleanup receipt
category: receipt
status: validated
date: 2026-08-22
tags: [receipt, research, parity, sanitizer, publication]
---

# Research corpus parity and staging cleanup receipt

## Scope

This receipt records synchronization of the local Reddit research staging set with the Git-authoritative sanitized corpus at `kb/raw/research/published/`.

## Verified before cleanup

| Check | Result |
|---|---:|
| Local staging artifacts | 128 |
| Published artifacts | 128 |
| Local-only extra paths | 0 |
| Published-only paths | 0 |
| Same SHA-256 content pairs | 7 |
| Different SHA-256 content pairs | 121 |
| Local JSON files | 115 |
| Invalid local JSON files | 0 |
| Published JSON files | 115 |
| Invalid published JSON files | 0 |
| Published sanitizer findings | 0 |

The differing hashes are expected for the sanitized publication transformation. Relative-path parity was complete before cleanup.

## Cleanup

After the checks above passed, the 128 unsanitized local staging artifacts outside `kb/raw/research/published/` were removed from the working tree. The published sanitized corpus remains tracked in Git and was not overwritten.

## Final invariant

- The Git repository is the source of truth for the complete sanitized corpus.
- No research artifacts remain local-only outside the defined publication location.
- Future research runs must use the parity procedure before local staging cleanup.

## Limitations

The sanitizer detects only its documented regex categories. This receipt does not claim detection of arbitrary undiscovered private-data formats.
