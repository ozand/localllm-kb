---
name: reddit-deep-research
description: >
  Autonomous deep-research and iterative investigation engine for Reddit communities using Surf CLI.
  Executes an iterative scientific loop: Hypothesis -> Targeted Reddit Search -> Post & Comment Extraction
  -> Outbound Link & Evidence Inspection -> Quality & Signal-to-Noise Evaluation -> Fact Synthesis ->
  New Hypothesis Generation. Use when researching cutting-edge AI developments, hardware configs, benchmarks,
  troubleshooting complex local setups, or gathering verified community knowledge.
compatibility: Requires surf CLI installed locally and Chromium-based browser connected.
---

# Reddit Deep Research Skill (`reddit-deep-research`)

Autonomous, hypothesis-driven research skill for navigating, extracting, and synthesizing deep technical knowledge from Reddit (e.g., `r/LocalLLaMA`, `r/MachineLearning`, `r/SelfHosted`) and connected external references using `surf`.

---

## The Iterative Research Cycle

Do not perform superficial, single-shot searches. Follow the continuous **Hypothesis-Driven Loop**:

```text
┌────────────────────────────────────────────────────────┐
│ 1. Formulate Hypothesis / Technical Query              │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. Targeted Search & Candidate Discovery               │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. Deep Extraction (Post Content + Top Comments)       │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. Outbound Link Traversal (GitHub, HuggingFace, Gist) │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 5. Quality & Signal-to-Noise Scoring                   │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 6. Fact Synthesis & Raw Archive Recording (OKF)        │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 7. Formulate Next-Tier Hypotheses / Open Questions     │
└──────────────────────────┬─────────────────────────────┘
                           │ (Repeat until knowledge saturated)
```

---

## 1. Targeted Reddit Search Patterns

### Direct Subreddit Search URL
Use direct URL navigation with `surf go` to avoid UI clicking overhead:

```bash
# Subreddit specific keyword query
surf go "https://www.reddit.com/r/LocalLLaMA/search/?q=<QUERY>&restrict_sr=1&sort=relevance"

# Time-bounded or top sorted queries
surf go "https://www.reddit.com/r/LocalLLaMA/search/?q=<QUERY>&restrict_sr=1&sort=top&t=month"
```

### Search via Google/DuckDuckGo Fallback
When Reddit search lacks precision for complex queries:
```bash
surf go "https://www.google.com/search?q=site:reddit.com/r/LocalLLaMA+<QUERY>"
```

---

## 2. Extraction via JavaScript DOM Helpers

Reddit pages render complex nested web components (`shreddit-post`, `shreddit-comment`). Use `surf js` with explicit `return` statements for fast, clean JSON extraction.

### Extract Post List from Search Results:
```javascript
// Run via: surf js "return (() => { ... })()"
return (() => {
  const posts = [];
  const links = Array.from(document.querySelectorAll('a[href*="/comments/"]'));
  const seen = new Set();
  for (const a of links) {
    const href = a.href.split('?')[0];
    if (seen.has(href) || !href.includes('/r/LocalLLaMA/comments/')) continue;
    seen.add(href);
    const title = a.innerText.trim();
    if (title.length > 10) {
      posts.push({ title, url: href });
    }
  }
  return JSON.stringify(posts.slice(0, 15));
})();
```

### Extract Post Body and High-Value Comments:
```javascript
// Run on the post page
return (() => {
  const title = document.querySelector('h1')?.innerText || document.title;
  const postElement = document.querySelector('shreddit-post');
  const postBody = postElement?.innerText || document.querySelector('div[data-click-id="text"]')?.innerText || '';
  
  // Extract top comments with author & score
  const commentElements = Array.from(document.querySelectorAll('shreddit-comment')).slice(0, 10);
  const comments = commentElements.map(c => {
    const author = c.getAttribute('author') || 'anonymous';
    const score = c.getAttribute('score') || '0';
    return { author, score, text: c.innerText.trim() };
  });

  // Extract external links mentioned in post & comments
  const externalLinks = Array.from(document.querySelectorAll('a[href^="http"]'))
    .map(a => a.href)
    .filter(h => !h.includes('reddit.com') && !h.includes('redd.it') && !h.includes('google.com'));

  return JSON.stringify({
    title,
    postBody: postBody.slice(0, 4000),
    comments,
    externalLinks: Array.from(new Set(externalLinks)).slice(0, 10)
  });
})();
```

---

## 3. Outbound Link Deep-Dive

If a post or comment references a critical external source:
1. **GitHub Repos / PRs / Issues**: Check release notes, config files, or bug discussions.
2. **HuggingFace Model Cards / GGUFs**: Inspect quantization matrices, `imatrix` parameters, and `mmproj` artifacts.
3. **Gist / Config Snippets**: Extract exact `llama.cpp` CLI flags, `modelfile` templates, or `litellm` configs.

Navigate directly via `surf go "<EXTERNAL_URL>"` and capture facts before returning to Reddit.

---

## 4. Quality & Signal-to-Noise Evaluation

Evaluate each thread against strict criteria before storing facts:

| Criterion | High Value (Weight $\ge 0.8$) | Low Value / Discard (Weight $\le 0.3$) |
| :--- | :--- | :--- |
| **Evidence** | Real benchmark numbers (tok/s, VRAM GB, context len), exact config flags, reproducible scripts. | Vague assertions ("feels fast", "seems smarter"), clickbait titles without data. |
| **Community Scrutiny** | Top comments validate findings, replicate results, or provide technical counterpoints. | Unanswered questions, unverified hype, zero comment engagement. |
| **Relevance** | Exact hardware matching (e.g. 24GB VRAM, Ryzen/CUDA), exact quantization (UD-Q4_K_S, imatrix). | Incompatible setups (cloud H100 clusters, Apple Silicon specific workarounds). |

---

## 5. Capturing into OKF Markdown (`kb/raw/research/`)

Save raw captures in immutable Markdown with structured frontmatter:

```markdown
---
source: "https://www.reddit.com/r/LocalLLaMA/comments/..."
title: "..."
author: "..."
capture_date: "YYYY-MM-DD"
quality_score: 0.9
tags: [local-llm, qwen, vram, optimization]
---

### Summary of Hypotheses Tested
...

### Verified Configurations & Commands
...

### Outbound References Verified
...
```

---

## 6. Recursive Question & Hypothesis Formulation

After analyzing a batch of threads, systematically list:
1. **Confirmed Facts**: What has been proven by multiple sources with config evidence.
2. **Identified Bottlenecks**: Known failure modes (e.g., context truncation, KV-cache OOM, speculative decoding mismatch).
3. **New Hypotheses to Test**: Open questions raised by the findings (e.g., "Can YaRN scaling extend context to 500k without perplexity explosion on RTX 3090 Ti?").
4. **Targeted Follow-up Queries**: Specific next search strings to execute in the next iteration.
