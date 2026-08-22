---
name: reddit-deep-research
description: >
  Use this skill when the user asks for deep, mass, exhaustive, or 50+ source Reddit research; investigation of community benchmarks, hardware configurations, local LLM deployments, troubleshooting, or an auditable Reddit corpus with links and citations. Run hypothesis-driven discovery through Surf CLI, preserve every query/search URL and selected thread URL, capture posts/comments and outbound evidence, score source quality, resume failures, sanitize publication copies, and produce separate immutable raw and OKF synthesis artifacts.
compatibility: Requires Python 3.8+, Surf CLI, and an authenticated Chromium tab when Reddit content requires login.
---

# Reddit Deep Research

Run reproducible, hypothesis-driven Reddit investigations. A polished summary is not enough: preserve the executable collector, exact discovery URLs, selected source inventory, immutable captures, outbound verification state, and error/resume history.

## When to use

Use this skill for:

- requests for deep or mass Reddit research, especially `50+` sources;
- `r/LocalLLaMA` hardware, model, runtime, benchmark, and troubleshooting investigations;
- community evidence that must later be distilled into a canonical KB;
- follow-up research when Reddit claims contain GitHub, Hugging Face, Gist, or vendor references;
- auditing or preparing a sanitized publication copy of research artifacts.

Do not use it for a single known Reddit URL that only needs a quick quotation, or for non-Reddit web research with no community-source requirement.

## Non-negotiable rules

1. **Load this skill explicitly before execution.** In the final receipt, state that `reddit-deep-research` governed the run.
2. **Use checked-in scripts.** Run the bundled scripts under `.agents/skills/reddit-deep-research/scripts/`. Do not invent the collector or sanitizer in `C:/Temp`, `/tmp`, an agent session folder, or inline code as the only executable copy.
3. **Preserve all discovery provenance.** Store every query, sort, time filter, and exact search URL, including failed attempts.
4. **Preserve all source URLs.** Every discovered and selected canonical Reddit thread URL must remain in the manifest with discovery-query IDs and processing status.
5. **Count researched sources honestly.** A search result is not a researched source. Count only successfully captured threads or explicit skips with reasons. Do not say `50+ researched` when only 47 captures succeeded.
6. **Keep raw and synthesis separate.** Per-thread raw JSON is immutable. Corpus and synthesis Markdown are derived artifacts and never replace raw evidence.
7. **Do not promote Reddit observations to facts.** Separate community observations, upstream claims, locally validated facts, and hypotheses.
8. **Verify outbound claims separately.** A linked GitHub/Hugging Face page starts as `unverified`; preserve its verification state.
9. **Use repository-relative paths in artifacts.** Never store browser profiles, cookies, authorization headers, API keys, private prompts, or unsanitized local paths in generated project artifacts.
10. **Use kebab-case and OKF frontmatter.** Rendered Markdown must pass the artifact contract.
11. **Sanitize only explicit copies.** Use `sanitize_artifacts.py` with separate input/output paths. Never modify immutable raw captures in place.

## Required references

- Read [`references/research-methodology.md`](references/research-methodology.md) before designing hypotheses, query coverage, quality scoring, saturation, or outbound verification.
- Read [`references/artifact-contract.md`](references/artifact-contract.md) before creating, resuming, validating, rendering, or publishing a run.
- Use [`assets/queries.example.txt`](assets/queries.example.txt) as a query-matrix starting point for hardware research.
- Use [`assets/run-config.example.json`](assets/run-config.example.json) when documenting run parameters.

## Process

### Step 1 — Define hypotheses and the run ID

Write hypotheses across the relevant dimensions: model/quant fit, runtime kernels, throughput, context/KV cache, power/thermals, PCIe/offload, failure modes, and adjacent hardware comparisons.

Choose a stable kebab-case run ID, for example:

```text
rtx-3090-ti-llm-optimization-2026-08
```

Create:

```text
kb/raw/research/runs/<run-id>/
```

Copy or author a repository-relative query file with one query per line. For a 50+ source run, default to at least 10 distinct queries and the `relevance,top,new` sorts.

### Step 2 — Verify Surf and identify the authenticated tab

Use the project-approved Surf browser launcher when one is required. Run `surf doctor` and `surf tab.list`. Record only the tab ID in the command invocation; do not write browser profile details to the KB.

If Surf or Reddit fails, use the applicable error/KB lookup workflow before retrying. Do not silently switch to unauthenticated scraping when the user authorized an authenticated browser session.

### Step 3 — Run durable discovery

```bash
python .agents/skills/reddit-deep-research/scripts/reddit_research.py discover \
  --tab <TAB_ID> \
  --topic "RTX 3090 Ti local LLM deployment and optimization" \
  --run-id rtx-3090-ti-llm-optimization-2026-08 \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --queries-file kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08/queries.txt \
  --target 50 \
  --sorts relevance,top,new
```

Discovery writes `run.json`, `queries.json`, and `threads.json` after each query. It deduplicates by canonical Reddit thread URL while preserving every query that found the thread. For hypothesis coverage, pass `--coverage-mode enabled --coverage-plan <path>` with a JSON object containing `dimensions`, where each dimension has a stable `id` and a non-empty `queries` list. Every assigned query must exist in the query file; the run records covered and uncovered dimensions. Omit the flags, or pass `--coverage-mode disabled`, for documented count-only backward compatibility.

Inspect counts and selection diversity before extraction. Expand the query matrix if a hypothesis dimension is absent. Do not select only positive or highly upvoted reports.

### Step 4 — Extract and resume selected threads

```bash
python .agents/skills/reddit-deep-research/scripts/reddit_research.py extract \
  --tab <TAB_ID> \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --keywords "rtx 3090 ti,24gb,llama.cpp,vram,context,kv cache,tokens/s,power,temperature"
```

The extractor:

- processes only selected `pending` or `error` records;
- skips successful immutable captures;
- stores one JSON capture per Reddit thread under `raw/`;
- records title, cleaned post body, top comments, query provenance, deterministic comment-evidence rankings, explainable quality components, separate human-review metadata, readiness metadata, and outbound links;
- rejects shell/error pages and empty or too-short posts with stable readiness reasons;
- appends sanitized failures to `errors.jsonl`;
- records bounded per-query and per-thread `attempt_history` entries and derives `retry-summary.json` with final status, retry classification, attempt count, and elapsed time;
- writes `outbound-references.json` and an explicit `follow-up.json` ledger.

Each captured comment receives deterministic dimension-specific prioritization for measurements, commands, model names, and counter-evidence. Scores, matched signals, missing-text status, exact source URL, author, and original comment index are retained in `comment_ranking`; rankings do not verify, summarize, or exclude comments.

Re-run the same command to resume. A timeout is a recorded state, not permission to remove the URL from the denominator. If a selected source must be excluded, create an explicit durable skip:

```bash
python .agents/skills/reddit-deep-research/scripts/reddit_research.py skip \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --thread-id <THREAD_ID> \
  --reason "Off-topic after full post inspection"
```

### Step 5 — Inspect and verify outbound references

Prioritize high-value primary sources listed in the methodology reference. Use the resumable verifier for the browsing pass:

```bash
python .agents/skills/reddit-deep-research/scripts/reddit_research.py verify-outbound \
  --tab <TAB_ID> \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --limit 25
```

This records bounded reachability, redirects, and timestamps in the separate outbound ledger. Filtering excludes irrelevant/static/private links as `skipped`; included references are ordered by deterministic priority. A successful page load remains `unverified`. Failed access is recorded as `failed`. After manually inspecting the referenced evidence, promote it explicitly with `mark-outbound`.

Do not conflate outbound verification counts with the number of Reddit sources. Outbound verification updates the bounded ledger, never immutable per-thread raw captures. The `--limit` flag applies only to included `unverified` references.

### Step 6 — Evaluate quality and saturation

Keep source-type, evidence-field, relevance, scoring-version, and human-review components visible. The bundled score is deterministic triage, not final truth; keyword presence alone cannot produce a high-quality result when evidence fields are absent.

Default discovery saturation requires five consecutive completed query records yielding fewer than two new unique URLs, after all hypothesis dimensions are covered. Saturation can stop discovery; it cannot turn failed extraction into completed research.

Populate `follow-up.json` with confirmed facts, bottlenecks, new hypotheses, and exact follow-up queries. Confirmed facts require primary-source or local validation evidence.

### Step 7 — Validate the run

```bash
python .agents/skills/reddit-deep-research/scripts/reddit_research.py validate \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --require-target
```

Validation checks URL deduplication, query provenance, capture existence, kebab-case names, required capture fields including readiness and review metadata, outbound verification states, retry-history/summary consistency, whether the source target or saturation rule is satisfied, and (when enabled) whether every planned coverage dimension has at least one completed query. The result reports `covered_dimensions` and `uncovered_dimensions`; a target count alone cannot pass an enabled coverage plan.

Resolve or explicitly report remaining `pending` and `error` records before describing the research as complete.

### Step 8 — Render separate OKF artifacts

Use `render_research.py corpus` and `synthesis` as documented in the artifact contract. The corpus must list all exact search URLs and all selected Reddit URLs. The synthesis must report coverage and failures and must not invent consensus.

### Step 9 — Audit a publication candidate

Before publishing a research corpus, audit a source tree without exposing matched values:

```bash
python .agents/skills/reddit-deep-research/scripts/sanitize_artifacts.py audit \
  --input kb/raw/research/runs/<run-id>
```

The audit report contains only file counts and category counts. It does not print matched paths, IPs, tokens, or surrounding text. Treat any finding as a publication blocker until explicitly reviewed.

### Step 10 — Create a sanitized publication copy

Never modify `kb/raw/research/` or a run's immutable `raw/` directory in place. Write to an explicit separate destination:

```bash
python .agents/skills/reddit-deep-research/scripts/sanitize_artifacts.py sanitize \
  --input kb/raw/research/runs/<run-id> \
  --output kb/raw/research/published/<run-id>
```

The sanitizer is deterministic and idempotent. It replaces only documented regex categories:

- Windows absolute paths → `<windows-path>`;
- selected Unix absolute paths → `<unix-path>`;
- RFC1918/loopback endpoints → `<private-endpoint>`;
- supported assignments/tokens → category-specific redaction markers.

Re-run `audit` against the publication copy. Publish only after the report has zero findings and manifests/receipts remain internally consistent. The sanitizer is bounded detection, not proof that arbitrary secrets or private data are absent.

### Step 11 — Update and query the KB index

From the project root:

```bash
python -m pytest -q
kb-bootstrap validate --dir kb
qmd update
qmd search "<topic terms>" -c localllm-raw
```

Confirm raw research remains absent from the canonical wiki collection.

### Step 12 — Report an auditable completion receipt

Report skill used, run ID, repository-relative paths, query/discovered/selected/captured/skipped/error counts, audit category counts, sanitized output path, test results, residual risks, and whether the publication gate passed. Never report only a polished conclusion without the source/manifests receipt.

## Gotchas

- **Do not use temporary scripts.** All collection and sanitization code must be checked in under the skill.
- **Do not publish an unaudited raw corpus.** Public Reddit content can still contain usernames, local paths, LAN endpoints, or copied credentials.
- **Do not sanitize in place.** Immutable evidence and publication copies must remain separate.
- **Do not print audit matches.** Reports contain category/count metadata only.
- **Regex coverage is bounded.** A zero count means no supported pattern matched; it does not prove the corpus contains no possible sensitive data.
- **Do not confuse discovered, selected, and captured counts.** Report all three.
- **Do not claim completion after partial success.** Forty-seven successful captures out of fifty-five attempts is `partial`, not “50+ researched.”
- **Quality scores are heuristics.** A high score does not validate a claim.
- **QMD search relevance is not evidence confidence.** A 97% search match only means retrieval relevance.
- **No generator template currently exists.** This skill is project-local and intentionally not added to `kb_bootstrap/templates/skills/`.

## Related

- `skill-creator` — evolve this skill and its evals.
- `surf-cli` — browser automation details and authenticated proxy sessions.
- `kb-wiki-builder` — promote reviewed evidence into canonical OKF entries.
- `qmd-operator` — update and query raw/canonical collections.
- `kb-lookup` — investigate failures before retries.
