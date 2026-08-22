---
name: reddit-deep-research
description: >
  Use this skill when the user asks for deep, mass, exhaustive, or 50+ source Reddit research; investigation of community benchmarks, hardware configurations, local LLM deployments, troubleshooting, or emerging AI behavior; or an auditable Reddit corpus with links and citations. Run hypothesis-driven discovery through Surf CLI, preserve every query/search URL and selected thread URL, capture posts/comments and outbound evidence, score source quality, resume failures, and produce separate immutable raw and OKF synthesis artifacts.
compatibility: Requires Python 3.8+, Surf CLI, and an authenticated Chromium tab when Reddit content requires login.
---

# Reddit Deep Research

Run reproducible, hypothesis-driven Reddit investigations. A polished summary is not enough: preserve the executable collector, exact discovery URLs, selected source inventory, immutable captures, outbound verification state, and error/resume history.

## When to use

Use this skill for:

- requests for deep or mass Reddit research, especially `50+` sources;
- `r/LocalLLaMA` hardware, model, runtime, benchmark, and troubleshooting investigations;
- community evidence that must later be distilled into a canonical KB;
- follow-up research when Reddit claims contain GitHub, Hugging Face, Gist, or vendor references.

Do not use it for a single known Reddit URL that only needs a quick quotation, or for non-Reddit web research with no community-source requirement.

## Non-negotiable rules

1. **Load this skill explicitly before execution.** In the final receipt, state that `reddit-deep-research` governed the run.
2. **Use checked-in scripts.** Run `.agents/skills/reddit-deep-research/scripts/reddit_research.py` and `render_research.py`. Do not invent the collector in `C:/Temp`, `/tmp`, an agent session folder, or inline code as the only executable copy.
3. **Preserve all discovery provenance.** Store every query, sort, time filter, and exact search URL, including failed attempts.
4. **Preserve all source URLs.** Every discovered and selected canonical Reddit thread URL must remain in the manifest with discovery-query IDs and processing status.
5. **Count researched sources honestly.** A search result is not a researched source. Count only successfully captured threads or explicit skips with reasons. Do not say `50+ researched` when only 47 captures succeeded.
6. **Keep raw and synthesis separate.** Per-thread raw JSON is immutable. Corpus and synthesis Markdown are derived artifacts and never replace raw evidence.
7. **Do not promote Reddit observations to facts.** Separate community observations, upstream claims, locally validated facts, and hypotheses.
8. **Verify outbound claims separately.** A linked GitHub/Hugging Face page starts as `unverified`; preserve its verification state.
9. **Use repository-relative paths in artifacts.** Never store browser profiles, cookies, authorization headers, API keys, private prompts, or unsanitized local paths.
10. **Use kebab-case and OKF frontmatter.** Rendered Markdown must pass the artifact contract.

## Required references

- Read [`references/research-methodology.md`](references/research-methodology.md) before designing hypotheses, query coverage, quality scoring, saturation, or outbound verification.
- Read [`references/artifact-contract.md`](references/artifact-contract.md) before creating, resuming, validating, or rendering a run.
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

Discovery writes `run.json`, `queries.json`, and `threads.json` after each query. It deduplicates by canonical Reddit thread URL while preserving every query that found the thread.

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
- records title, cleaned post body, top comments, query provenance, quality components, readiness metadata, and outbound links;
- rejects shell/error pages and empty or too-short posts with stable readiness reasons;
- appends sanitized failures to `errors.jsonl`;
- writes `outbound-references.json` and an explicit `follow-up.json` ledger.

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

This records reachability, redirects, and timestamps in the separate outbound ledger. A successful page load remains `unverified`. After manually inspecting the referenced evidence, promote it explicitly:

```bash
python .agents/skills/reddit-deep-research/scripts/reddit_research.py mark-outbound \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --reference-id <THREAD_ID:INDEX> \
  --state verified \
  --note "Inspected upstream benchmark command and environment section."
```

Do not conflate outbound verification counts with the number of Reddit sources. Outbound verification updates the ledger, never immutable per-thread raw captures.

### Step 6 — Evaluate quality and saturation

Keep deterministic score components visible. Treat the bundled keyword score as triage, not final truth.

Default discovery saturation requires five consecutive completed query records yielding fewer than two new unique URLs, after all hypothesis dimensions are covered. Saturation can stop discovery; it cannot turn failed extraction into completed research.

Populate `follow-up.json` with confirmed facts, bottlenecks, new hypotheses, and exact follow-up queries. Confirmed facts require primary-source or local validation evidence.

### Step 7 — Validate the run

```bash
python .agents/skills/reddit-deep-research/scripts/reddit_research.py validate \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --require-target
```

Validation checks URL deduplication, query provenance, capture existence, kebab-case names, required capture fields including readiness metadata, outbound verification states, and whether the source target or saturation rule is satisfied.

Resolve or explicitly report remaining `pending` and `error` records before describing the research as complete.

### Step 8 — Render separate OKF artifacts

```bash
python .agents/skills/reddit-deep-research/scripts/render_research.py corpus \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --output kb/raw/research/rtx-3090-ti-llm-optimization-2026-08-corpus.md

python .agents/skills/reddit-deep-research/scripts/render_research.py synthesis \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --output kb/raw/research/rtx-3090-ti-llm-optimization-2026-08-synthesis.md \
  --minimum-score 0.5
```

The corpus must list all exact search URLs and all selected Reddit URLs. The synthesis must report coverage and failures and must not invent consensus. Manually add claim clusters only with supporting URLs and evidence labels.

### Step 9 — Update and query the KB index

From the project root:

```bash
python -m pytest -q
kb-bootstrap validate --dir kb --check-collections
qmd update
qmd search "<topic terms>" -c localllm-raw
```

Confirm raw research remains absent from the canonical wiki collection.

### Step 10 — Report an auditable completion receipt

Generate a machine-readable receipt:

```bash
python .agents/skills/reddit-deep-research/scripts/reddit_research.py receipt \
  --run-dir kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08 \
  --output kb/raw/research/runs/rtx-3090-ti-llm-optimization-2026-08/receipt.json
```

The command exits non-zero when selected extraction remains incomplete or neither the source target nor saturation condition is met. Report:

- skill used: `reddit-deep-research`;
- run ID and repository-relative run directory;
- number of query records, unique discovered URLs, selected URLs, successful captures, skips, and errors;
- whether target or saturation was reached;
- corpus and synthesis paths;
- script paths used;
- outbound verification counts;
- residual risks and unverified claims.

Never report only a polished conclusion without the source/manifests receipt.

## Batch defaults

| Setting | Default |
|---|---:|
| Selected Reddit source target | 50 |
| Distinct query strings | >= 10 |
| Search sorts | relevance, top, new |
| Top comments captured | 15 |
| Saturation window | 5 completed queries |
| Minimum new URLs per query before low-yield | 2 |
| Synthesis quality threshold | 0.5 |

Change a default only when the run manifest records the reason.

## Gotchas

- **The description is the trigger.** Requests saying “mass research,” “deep research,” or “50+ sources” must activate this skill even if the user does not explicitly say Reddit when the context is an existing Reddit investigation.
- **Do not use temporary scripts.** The prior failure mode was generating collectors under `C:/Temp`, then leaving no reusable implementation in the skill.
- **Do not hide source URLs inside a huge JSON dump.** Persist explicit query and thread manifests and render a corpus document where links are reviewable.
- **Do not confuse discovered, selected, and captured counts.** Report all three.
- **Do not claim completion after partial success.** Forty-seven successful captures out of fifty-five attempts is `partial`, not “50+ researched.”
- **Reddit DOM changes.** Keep selector fallbacks in the bundled script and record stable readiness failures instead of treating shell/error pages as captures.
- **Reddit pages contain irrelevant anchors.** Filter navigation/ad links and verify only evidence-bearing outbound references.
- **Quality scores are heuristics.** A high score does not validate a claim.
- **QMD search relevance is not evidence confidence.** A 97% search match only means retrieval relevance.
- **No generator template currently exists.** This skill is project-local and intentionally not added to `kb_bootstrap/templates/skills/` under Issue #3. Reassess alignment if a reusable template is introduced later.

## Evals

Read [`evals/evals.json`](evals/evals.json) when evaluating changes to this skill. Run baseline and with-skill comparisons using the `skill-evaluator` agent as described by the `skill-creator` methodology. Cover completeness/provenance, outbound evidence/OKF separation, and resume/error handling.

## Related

- `skill-creator` — evolve this skill and its evals.
- `surf-cli` — browser automation details and authenticated proxy sessions.
- `kb-wiki-builder` — promote reviewed evidence into canonical OKF entries.
- `qmd-operator` — update and query raw/canonical collections.
- `kb-lookup` — investigate failures before retries.
