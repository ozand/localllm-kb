---
source_url: https://unsloth.ai/blog/phi3
slug: phi3
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: phi3

Blog

# Phi-3  support, Llama 3 bug fixes, Mistral v0.3

## May 23, 2024 • By Daniel & Michael

## May 23, 2024

## •

## By Daniel & Michael

Phi-3 models (medium & mini) are now supported. We also resolved all issues affecting Llama 3 finetuning, so to get proper results, make sure to use Unsloth!Many Llama 3 finetunes are broken, and we discussed this on a Reddit thread. So, be sure to use our Llama 3 base notebook or our Instruct notebook!Mistral v0.3, Qwen and Yi  are also now supported. We make Phi-3 2x faster and use 50% less memory and make Mistral v3 2.2x faster with 73% less VRAM. All pre-quantized 4bit models (4x faster downloading) are on our Hugging Face page including Phi 3, Qwen etc.We also uploaded on Colab a new ORPO notebook. We've also hit 10K stars on GitHub and were selected to take part in the annual GitHub Accelerator Program!Don't forget to ⭐Star us on GitHub and join our Discord server ❤️

## Performance benchmarks

ModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer context🤗Hugging Face+FA2Llama-3 8B24GB2x63%3x longer1xLlama-3 70B80GB1.8x68%6x longer1xPhi-3 Mini24GB1.85x51%3x longer1xPhi-3 Medium24GB1.8x50%3x longer1xMistral v0.3 7B24GB2x74%4x longer1xFA2 = Flash Attention 2. We tested using the Alpaca Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down). 24GB cards use Google Colab's new L4 GPUs, and 80GB cards are A100 80GB.🦙 Llama 3 finetuning issuesThere is a common misconception that Llama 3 finetunes are either useless or poor. However, this belief stems from various issues that we've identified and addressed. With the help of the Unsloth community, we have resolved many of these problems, and fine-tuning with Unsloth should now work perfectly fine!Here's a list of the main issues:

- Double BOS tokens during finetuning can break things. Check this. Unsloth auto fixes this.

- GGUF conversion is broken. Be careful of double BOS. Also use CPU and not GPU conversion. Unsloth has builtin auto GGUF conversions.

- Some of Llama 3's base (not instruct) weights are "buggy" (untrained): <|reserved_special_token_{0->250}|> <|eot_id|> <|start_header_id|> <|end_header_id|>. This can cause NaNs and buggy results. Unsloth auto fixes this.

-

- According to the Unsloth community, adding a system prompt makes finetuning of the Instruct version (maybe the base) much better.

- Quantization issues are rampant which shows actually you can get good performance with Llama3, but using the wrong ones can hurt perf. For eg for finetuning use bitsandbytes nf4 which boosts accuracy. Or for GGUF use the "I" versions as much as possible.

- Long context models are sometimes badly trained - some simply extend the RoPE theta, sometimes without any training, then train one some weird concatted dataset to make it a long dataset - hence why it doesnt work.

Many Llama 3 finetunes are broken due to these issues, and we discussed this further on a Reddit thread. So, be sure to use our Llama 3 base notebook or our Instruct notebook!

Phi-3 finetuning is 1.8x fasterWe successfully converted Phi-3 mini and medium to Mistral type models, allowing Unsloth's full suite of optimizations to work! We uploaded to our Hugging Face page.But how are we certain our Mistral-fication worked? Unsloth Community members have uploaded our Mistral-fied Phi-3 mini version to the Hugging Face Open LLM Leaderboard and showed our version attains comparable accuracy to the original Microsoft version. Other Llama-fied versions seem to fall short, especially on MMLU.

In fact, if you compare the training loss between Unsloth's Mistral-fied version for Phi-3, we actually attain slightly lower loss than using the original version! This is most likely because we split the attention matrices into 3 modules (Q, K, V), allowing 4bit quantization to represent each matrix more accurately. The original module fused all 3. The MLP gate and up are also merged in the original model, and we unmerged it.

Try out our Phi-3 Mini 3.8B notebook and our Phi-3 Medium 14B notebook via Colab! Phi-3 Medium fits comfortably in a free Tesla T4 Colab with Unsloth, and you can fit 3 to 4x longer context lengths than FA2 with Unsoth!

💕 Thank you! We're also grateful we've been selected to be in Github's annual accelerator program! We're super pumped to be working alongside 10 other cool projects from all around the world, and we're super excited for it! Github's blog post has more details!Also feel free to support us via our Ko-fi donation page. Huge shout out to: Abuben, Jaya, Oliver, jedamaster, Nguyen, Mo, Icecream102, arthrod, Teto,  Chimiste, Martin & FullOff_Bad_Ideas who are new supporters! 🙏As always, be sure to join our Discord server for help or just to show your support! You can also follow us on Twitter and Substack.Thank you for reading!Daniel & Michael Han 🦥23 May 2024

## All model support coming

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
