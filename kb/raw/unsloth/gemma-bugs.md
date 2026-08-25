---
source_url: https://unsloth.ai/blog/gemma-bugs
slug: gemma-bugs
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: gemma-bugs

Unsloth Fixing Gemma bugs

unsloth

ModelsBlogUnsloth Desktop✨Docs

Download

☰

ModelsBlogUnsloth DesktopDocumentation

Download

Blog

# Fixing All Gemma Bugs

## Mar 6, 2024 •  By Daniel & Michael

## Mar 6, 2024

## •

## By Daniel & Michael

Over the past week, Unsloth has been hard at work finding and fixing Gemma bugs. At first, Google showcased Gemma’s promising results however, many problems like discrepancies in loss values made us step in to help Gemma live up to its initial promise.We've already pushed all the fixes in our free Colab notebooks but not elsewhere. Here are the bugs we found:

- Must add <bos>

- Paper typo? <end_of_turn>model

- sqrt(3072)=55.4256 but bfloat16 is 55.5

- Layernorm (w+1) should be done in float32

- Keras mixed_bfloat16 RoPE is wrong

- RoPE is sensitive to a*(1/x) vs a/x

- RoPE should be float32 not bfloat16 (Fixed in Hugging Face 4.38.2)

- GELU should be approx tanh not exact (Ongoing PR)💡 Detailed findings1. Must add <bos>The most important caveat for finetuning is you must add the <bos> token (red loss). The blue loss is no <bos> token. Packing with TRL works, but has a higher base loss - it’s possible Gemma does not use the T5 packing trick anymore! See the T5 paper page 12 or TensorFlow2. Paper typo? <end_of_turn>modelThere is a typo in the technical report. <end_of_turn>model is wrong, and should just be <end_of_turn>. And you must add newlines at the end of <start_of_turn>model.

- No <bos> token generates [Knock knock.]

- With <bos> token generates [Gemma who?] which is correct.

- With <bos> but no newline generates [\nSure, here is the complete response:]

- With <end_of_turn>model generates [Gemma what?]If we assume the report is correct, and [Gemmo who?] is the correct choice, then it’s just <end_of_turn> and not <end_of_turn>model. Also a newline is a must, and the <bos> token.3. sqrt(3072)=55.4256 but bfloat16 is 55.5Interestingly, Gemma multiplies the embeddings by sqrt(hidden_dim). However, there is a precision problem! Gemma uses jnp.sqrt(self.embed_dim) .astype(x.dtype) which means sqrt(3072) = 55.4256, but casting it to bfloat16 rounds it to 55.5. For Gemma 2b, sqrt(2048) = 45.2548, but casting it to bfloat16 makes it 45.25.See Gemma repo and Keras for reference.4. Layernorm (w+1) should be done in float32The layernorms must be upcasted to float32 and not bfloat16 or float16 halfway. It must be done unlike Llama’s RMS Layernorm which downcasted before multiplying by the weights. We must downcast at the end.5. Keras mixed_bfloat16 RoPE is wrongTPUs on Colab cast RoPE positions in int32, whilst in Keras, they’re cast to compute_dtype (bfloat16), causing [8190, 8191] to become [8192, 8192]Keras’s incorrect line casting positions to bfloat16Deepmind uses int32 for positions and I also verified on TPUs its int326. RoPE is sensitive to a*(1/x) vs a/xWeirdly precalculating RoPE Embeddings seem to have precision issues when doing the reciprocal first then multiplying, whilst doing a division attains higher accuracy. I call this the RoPE Creation fix, where we follow exactly how Deepmind creates the RoPE sin and cos matrices. You can see the error decreases quite a bit in float32, and has some effect in mixed precision.7. RoPE should be float32. Fixed it in HF 4.38.2.We already pushed our first fix for Gemma which reduced errors a lot in transformers. Upgrade your transformers version to 4.38.2 to get the fix. Essentially we found the same issue like in the Keras codebase. I wrote a detailed bug report and analysis on the PR.8. GELU should be approx tanh not exact. Ongoing PRAnd finally we identified the approx GELU issueWe need to use the approximate GELUand not the exact GELU. We’re working on a PR for transformers and we already pushed a PR to Pytorch Gemma.💕 Support us! As a team of just 2 brothers with 0 revenue or funding, it would be amazing if you could support us via our Ko-fi donation page. Shout out to: prateekgupta, machine1235 and cnbeining who are new supporters! 🙏As always, be sure to join our Discord server for help or just to show your support! You can also follow us on Twitter and Substack. We appreciate your continued love and support!Thank you for reading!Daniel & Michael Han 🦥6 March 2024

## Unsloth Studio coming soon!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
