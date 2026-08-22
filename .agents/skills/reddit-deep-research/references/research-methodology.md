# Reddit deep-research methodology

Read this reference when designing the query matrix, selecting sources, scoring evidence, deciding saturation, or performing outbound verification.

## Hypothesis ledger

Start with explicit hypotheses, not only keywords. For a hardware investigation, divide the topic into independently testable dimensions:

1. capacity and model/quant fit;
2. runtime and kernel choices;
3. generation throughput and prompt processing;
4. context/KV-cache behavior;
5. power, thermals, noise, and reliability;
6. PCIe, CPU/RAM offload, and multi-GPU behavior;
7. failure modes and contradictory reports;
8. comparisons with adjacent hardware.

For each dimension write:

- current hypothesis;
- evidence that would support it;
- evidence that would falsify it;
- exact search strings;
- required primary/outbound sources.

## Discovery coverage

Default for a 50+ source request:

- at least 10 distinct search strings;
- use `relevance`, `top`, and `new` sorts unless the topic makes one invalid;
- include positive, negative, troubleshooting, benchmark, and comparison formulations;
- deduplicate only by canonical Reddit thread URL;
- preserve all exact query/search URLs, including failed queries;
- select at least 50 unique threads unless a recorded saturation threshold is reached.

A discovery hit is not a researched source. Count a source as researched only after its post capture succeeds or it receives an explicit `skipped` record with a reason.

## Source selection

Prefer threads with:

- exact matching hardware/model/runtime;
- reproducible commands or flags;
- tok/s, prompt processing, VRAM, context, power, or temperature measurements;
- multiple configurations compared under one environment;
- comments that replicate, contradict, or correct the post;
- external primary references.

Keep a minority of negative or contradictory sources. Do not select only high-engagement success stories.

## Quality scoring

Store components separately. A default deterministic score is:

```text
quality = 0.45 * evidence + 0.35 * relevance + 0.20 * community_scrutiny
```

Where each component is in `[0, 1]`:

- **evidence**: concrete measurements, environment, commands, or artifacts;
- **relevance**: exact match to the research hypothesis and target environment;
- **community scrutiny**: substantive comments that reproduce or challenge the result.

The bundled script supplies a conservative keyword-based first pass. The synthesis must disclose the scoring method. Human review can add a separate assessment but must not overwrite the original score.

## Saturation

Use saturation to stop expanding the query plan, not to excuse incomplete extraction.

Default discovery threshold:

- five consecutive completed query records;
- each yields fewer than two new unique thread URLs;
- coverage already includes all planned hypothesis dimensions.

Record `reached`, the threshold values, and a human-readable reason. If the target is not met and saturation is not reached, the run is incomplete.

## Outbound verification

Extract external links from the post and selected comments, then verify high-value links separately.

Prioritize:

1. NVIDIA specifications and technical documentation;
2. llama.cpp, vLLM, ExLlamaV2, TensorRT-LLM, and related GitHub issues/releases;
3. Hugging Face model cards and quant repositories;
4. benchmark scripts, Gists, and configuration files;
5. vendor board specifications and teardown data.

For each visited reference record original URL, final URL, verification state, access time, and a short note describing what evidence was actually inspected.

## Contradictions and claim promotion

Reddit provides community evidence, not canonical truth. A claim can move to canonical KB only when its scope and evidence are explicit:

- **community observation** — one or more Reddit reports;
- **upstream claim** — primary documentation or repository says it;
- **locally validated** — a sanitized local receipt reproduces it;
- **hypothesis** — plausible but unverified.

Never convert numeric claims such as throughput, temperature, power savings, VRAM usage, context limits, or quality loss into universal recommendations based only on a Reddit synthesis.

## Follow-up ledger

After every batch populate `follow-up.json` with:

- confirmed facts;
- identified bottlenecks;
- new hypotheses;
- targeted follow-up queries.

Start a new iteration when a high-impact claim remains supported only by community observations, when sources conflict materially, or when a new runtime/hardware-specific bottleneck emerges.
