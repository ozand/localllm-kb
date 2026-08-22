---
id: "raw-reddit-qwen-3090ti-hardened-workflow-comparison-2026-08"
category: "raw-research-comparison"
title: "Old versus hardened Reddit research: Qwen and RTX 3090 Ti"
capture_date: "2026-08-22"
evidence_status: "community-workflow-evaluation"
run_ids:
  - "qwen-3090ti-hardened-evaluation-2026-08"
  - "qwen-3-8-27b-hardened-evaluation-2026-08"
source_count: 93
tags: [reddit, workflow-evaluation, qwen, rtx-3090-ti, provenance]
---

# Old versus hardened Reddit research

This is a workflow evaluation, not a new hardware or model capability claim. It compares the earlier ad-hoc captures with two reruns executed using the checked-in `reddit-deep-research` scripts.

## Artifacts

### Prior ad-hoc captures

- `kb/raw/research/reddit_50_deep_dive_raw.json`: 46 unique Reddit threads, 644 comments, 45 non-empty bodies, no captured outbound links.
- `kb/raw/research/reddit_3090ti_deep_dive_raw.json`: 47 unique Reddit threads, 590 comments, 46 non-empty bodies, no captured outbound links.
- `kb/raw/research/reddit_threads_manifest.json`: 75 discovered links with only `href` and `title` fields.
- `kb/raw/research/reddit_3090ti_manifest.json`: 93 discovered links with only `href` and `title` fields.

The prior files do not preserve exact discovery query URLs, per-source status, retry history, quality components, or outbound-reference verification state.

### Hardened reruns

- Qwen/RTX 3090 Ti target: [`qwen-3090ti-hardened-evaluation-2026-08-corpus.md`](qwen-3090ti-hardened-evaluation-2026-08-corpus.md) with run state under `runs/qwen-3090ti-hardened-evaluation-2026-08/`.
- Qwen 3.8 27B target: [`qwen-3-8-27b-hardened-evaluation-2026-08-corpus.md`](qwen-3-8-27b-hardened-evaluation-2026-08-corpus.md) with run state under `runs/qwen-3-8-27b-hardened-evaluation-2026-08/`.
- The exact executable inputs are `.agents/skills/reddit-deep-research/scripts/reddit_research.py` and `render_research.py`.

## Coverage comparison

| Run | Query records | Query records completed | Unique discovered | Selected | Captured | Skipped | Query errors | Outbound refs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Prior Qwen ad-hoc | not recorded | not recorded | 75 manifest hits | not recorded | 46 | 0 recorded | not recorded | 0 |
| Prior RTX 3090 Ti ad-hoc | not recorded | not recorded | 93 manifest hits | not recorded | 47 | 0 recorded | not recorded | 0 |
| Hardened RTX 3090 Ti | 36 | 4 | 53 | 50 | 50 | 0 | 32 query records | 578 |
| Hardened Qwen 3.8 27B | 36 | 5 | 50 | 50 | 49 | 1 | 567 |

The hardened process makes the denominator explicit. The RTX run reached 50/50 captures after resumable retries. The Qwen run reached 49 captures plus one explicit skip after three navigation timeouts; its receipt is complete because every selected record is terminal and the 50-source target is represented by 49 captures + 1 documented skip.

## Provenance and deduplication

- Prior captures have unique URLs within each JSON file, but do not record which query found each source.
- Hardened runs preserve exact search URLs, query IDs, sort, time filter, attempts, query errors, canonical thread URLs, and discovery-query provenance.
- The hardened RTX run selected 50 URLs; 13 overlapped with the union of the two prior raw corpora and 37 were new to those old captures.
- The hardened Qwen run selected 50 URLs; 13 overlapped with the old union and 37 were new.
- The overlap is not a content-quality comparison: Reddit search results and page state changed between runs.

## What works effectively

1. **Durable manifests:** `run.json`, `queries.json`, and `threads.json` make the source denominator and exact URLs auditable.
2. **Windows process recovery:** The first rerun exposed an actual Windows `surf.cmd` ampersand-splitting defect. After the fix, search URLs containing `&` passed intact and discovery completed.
3. **Resume behavior:** The RTX extraction recovered from 7 initial source errors and finished 50/50. The Qwen extraction recovered from repeated timeouts and preserved one explicit skip rather than deleting the source.
4. **Immutable raw separation:** Per-thread captures remain separate from the outbound ledger; subsequent link-state work does not rewrite raw evidence.
5. **Honest completion receipts:** Counts distinguish discovered, selected, captured, skipped, pending, and errors. The prior process could only report a success count.
6. **Reproducible rendering:** Corpus and synthesis files have kebab-case names, OKF frontmatter, and links back to run artifacts.

## What needs improvement

### High priority

1. **Query plan execution stops early.** Discovery stops after reaching 50 selected sources, leaving most of the 36 planned query records unattempted. This means the run has a target count but not full query-matrix coverage. Future runs should either execute all hypothesis dimensions before selecting the final sample or record an explicit `coverage_policy` and dimension coverage check.
2. **Outbound verification is only inventory.** The reruns found 578 and 567 external links, but all remained `unverified`. The extractor also captures sidebar/navigation links, creating a very large queue. Add relevance filtering and a bounded primary-source verification stage.
3. **Page extraction includes chrome.** Captures commonly begin with `Repost / Go to LocalLLaMA` and one capture is an error shell with an empty body. Add a page-readiness/error-page gate and extract the post body from a narrower selector before including comments.
4. **Quality scoring is triage-only.** Average scores were 0.645 for the RTX run and 0.568 for the Qwen run. Low scores include relevant questions, polls, announcements, and one empty shell. Add source-type classification, evidence-field extraction, and human review fields; never treat the score as evidence confidence.

### Medium priority

5. **The default 15-comment capture is broad but not relevance-ranked.** Capture top comments with scores, but prioritize comments containing measurements, commands, model names, or counter-evidence.
6. **Error receipts record repeated attempts but do not summarize retry history per thread/query.** Add `attempt_history` or a derived retry summary to the manifest.
7. **The comparison currently evaluates workflow and corpus shape, not substantive claim agreement.** A next iteration should cluster claims by hypothesis, link each claim to exact source URLs, and mark contradictions explicitly.

## Safety and interpretation

- These reruns provide community observations only; they do not validate universal RTX 3090 Ti throughput, thermal, power, PCIe, or model-capability claims.
- The old synthesis contains broad numeric/conclusive wording such as `consensus`, `zero measurable`, `20–30%`, `40–50%`, `72–82°C`, and `98k` without source-level evidence links. Those claims must not be promoted to canonical KB facts without primary-source or local validation receipts.
- All conclusions above are traceable to the prior raw files, new run manifests, new receipts, and new source captures. No prior raw capture was replaced.

## Follow-up

- Fix extraction readiness and content selectors.
- Add source-type and evidence-field scoring.
- Add outbound relevance filtering and primary-source verification.
- Require explicit hypothesis-dimension coverage before declaring a 50+ batch complete.
- Create a separate claim-clustering pass before promoting any hardware or model claims to `kb/wiki/`.
