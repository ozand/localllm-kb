# Reddit batch artifact contract

Read this reference when creating, resuming, validating, or rendering a Reddit research batch.

## Run directory

Use a repository-relative run directory under `kb/raw/research/runs/<run-id>/`.

```text
kb/raw/research/runs/<run-id>/
├── run.json
├── queries.json
├── threads.json
├── errors.jsonl
├── outbound-references.json
├── follow-up.json
├── browser-scripts/
└── raw/
    └── <thread-id>-<title-slug>.json
```

Never use `C:/Temp`, `/tmp`, a browser profile directory, or an agent session directory as the only copy of executable code or research state.

## `run.json`

Required top-level fields:

| Field | Meaning |
|---|---|
| `schema_version` | Integer schema version. |
| `run_id` | Stable kebab-case identifier. |
| `topic` | Human-readable research topic. |
| `created_at`, `updated_at` | UTC ISO-8601 timestamps. |
| `status` | `discovering`, `discovered`, `partial`, or `captured`. |
| `target_selected_sources` | Required source target; default 50. |
| `query_plan` | Complete query/search URL records. |
| `threads` | Complete discovered and selected Reddit thread records. |
| `counts` | Deterministic run counts. |
| `saturation` | Config, reached flag, and reason. |
| `artifacts` | Repository-relative artifact names. |

## Query record

Every discovery attempt must preserve:

```json
{
  "query_id": "stable-hash",
  "query": "rtx 3090 ti llama.cpp power limit",
  "subreddit": "LocalLLaMA",
  "sort": "top",
  "time_filter": "year",
  "search_url": "https://www.reddit.com/r/LocalLLaMA/search/?...",
  "status": "completed",
  "attempts": 1,
  "discovered_count": 12,
  "new_unique_count": 7,
  "error": null
}
```

Do not report "50+ sources researched" unless the selected/captured URL inventory is present and countable.

## Thread record

Every discovered Reddit URL must have:

```json
{
  "thread_id": "reddit-id",
  "canonical_url": "https://www.reddit.com/r/LocalLLaMA/comments/.../",
  "title": "...",
  "discovered_by_query_ids": ["stable-hash"],
  "selected": true,
  "selection_reason": "first unique canonical URL in deterministic query order",
  "status": "pending",
  "attempts": 0,
  "capture_file": null,
  "quality": null,
  "outbound_reference_count": 0,
  "last_error": null
}
```

Allowed processing statuses are `pending`, `captured`, `skipped`, and `error`. Resume only `pending` and `error` records. Never silently discard failed URLs.

## Raw thread capture

Per-thread raw JSON is immutable after successful creation. Outbound verification updates only `outbound-references.json`, never the raw capture. Raw JSON must include:

- canonical Reddit URL;
- capture timestamp;
- title and author when available;
- post body;
- selected top comments with authors/scores as exposed by Reddit;
- query IDs that discovered the thread;
- deterministic quality score with source type, evidence fields, score components, and scoring version;
- separate human-review metadata (`decision`, `rationale`, `reviewer`, `follow_up_status`);
- outbound references with verification state.

If a capture must be corrected, create a new versioned run or an explicit replacement artifact; do not rewrite historical evidence silently.

## Outbound references

Use these states only:

- `verified` — the referenced evidence was manually inspected and an evidence note was recorded;
- `redirected` — target loaded after redirect; preserve both original and final URL, but do not imply the claim was verified;
- `failed` — automated access was attempted and failed with a sanitized reason;
- `skipped` — excluded by the deterministic filter or intentionally not scheduled;
- `unverified` — included and not yet visited.

A Reddit comment mentioning a GitHub/Hugging Face URL does not make that external claim verified. The outbound ledger must retain normalized URL, original URL variants, source thread IDs, source capture files, inclusion/filter reason, priority score/class, and verification state.

## Error receipts

`errors.jsonl` is append-only. Each line contains:

```json
{
  "schema_version": 1,
  "timestamp": "2026-08-22T10:00:00Z",
  "stage": "extraction",
  "item_id": "reddit-thread-id",
  "error_type": "RuntimeError",
  "message": "sanitized diagnostic",
  "retryable": true
}
```

Never store cookies, authorization headers, browser profile paths, raw private prompts, API keys, or full local absolute paths.

## OKF corpus and synthesis Markdown

Rendered Markdown filenames must use kebab-case:

- `<run-id>-corpus.md`
- `<run-id>-synthesis.md`

Both must have YAML frontmatter with stable `id`, `category`, `title`, `capture_date`, `run_id`, `source_count`, `evidence_status`, and `tags`.

The corpus document lists every exact query URL and selected Reddit URL. The synthesis is separate and must distinguish:

1. verified facts supported by primary sources/local receipts;
2. repeated community observations still requiring verification;
3. hypotheses and open questions.
