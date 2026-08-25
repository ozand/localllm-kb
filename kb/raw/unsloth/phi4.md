---
source_url: https://unsloth.ai/blog/phi4
slug: phi4
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: phi4

Blog

# Phi-4 Finetuning + Bug Fixes by Unsloth

## Jan 10, 2025 • By Daniel & Michael

## Jan 10, 2025

## •

## By Daniel & Michael

Phi-4, Microsoft's new 14B model that performs on par with OpenAI's GPT-4o-mini is now in Unsloth! We found & fixed 4 bugs in Phi-4, greatly increasing the model’s accuracy—details below. We previously worked with Google & Hugging Face for our Gemma bug fixes and Meta with our Llama bug fixes.Unsloth makes Phi-4 finetuning 2x faster, use 70% less memory, and enables >128K context lengths which is 12x longer than Hugging Face + FA2’s 12K on a 48GB GPU.We converted Phi-4 to Llama’s architecture for better accuracy and easier use. We also uploaded fixed Phi-4 GGUFs and dynamic 4-bit quants here.Try fine-tuning via our Phi-4 (14B) Colab Notebook which fits on Google's free Tesla T4 16GB GPU.Phi-4 Bug Fixes

## 1. Tokenizer bug fixes

The Phi-4 tokenizer interestingly uses <|endoftext|> as the BOS (beginning of sentence), EOS (end of sentence) and PAD (padding) tokens. The main issue is the EOS token is wrong - it should be <|im_end|>. Otherwise, you will get <|im_end|><|endoftext|> in generations.

## 2. Fine-tuning bug fixes

The padding token should be a designated pad token like in Llama (<|finetune_right_pad_id|>) or we can use an untrained token - for example we use <|dummy_87|>. Using the incorrect pad token, can result in infinite generations because the pad token get masked during the loss calculations. Thus, we must use the correct pad token to not accidentally mask out the eos token, since in this case it is the same as the pad token.

## 3. Chat template issues

The Phi-4 tokenizer always adds an assistant prompt - it should only do this if prompted by add_generation_prompt. Most LLM serving libraries expect non auto assistant additions, and this might cause issues during serving.

💡 Do our fixes work?

Multiple reports from Redditors shows our fixes do in fact work! For example, using the Hugging Face OpenLLM Leaderboard, we see our fixes and Llama-fication of Phi-4 does better or on par with Microsoft’s official Phi-4 model!

Reddit comments show our fixes make Phi-4 inference much better:Exhibit #1: Someone’s internal multiple choice testing shows our fixed version does much better:

Exhibit #2: Telling Phi-4 to draw an ASCII art of a house:

🦙 Llama-fication

We also ported Phi-4 directly into a Llama architecture! This allows finetuning to be much more accurate since QKV are unmerged, and gate/up are also unmerged. This allows LoRA finetuning to learn separate A matrices for each. View the uploads are here.

🦥 Dynamic 4-bit Quants

We uploaded 4-bit bitsandbytes pre-quantized models for 4x faster downloading, however, Unsloth's Dynamic 4-bit quant shows we mustn't quantize all layers. This results in largely increased accuracy while only using 10% more VRAM.A great example of our dynamic quants' effectiveness is through submitting our dynamic 4-bit quants to Hugging Face's OpenLLM Leaderboard. Our 4-bit dynamic quant scored nearly as high as our 16-bit version—and well above standard Bnb 4-bit and Microsoft's official 16-bit model, especially for MMLU.

We uploaded our dynamic 4-bit quants which leave some layers in 16-bit here.See the activation and weight error analysis plots are below:

🛠️ Finetuning Phi-4Phi-4 (14B)1xL4 24GB12xlonger contextPhi-4 (14B)1xL4 24GB2xfasterPhi-4 (14B)1xL4 24GB>70%less VRAMPhi-4 finetuning fits with Unsloth in under 15GB of VRAM! It’s also 2x faster, and default uses our dynamic 4-bit quants for superior accuracy! Inference is also natively 2x faster!Try fine-tuning Phi-4 with Unsloth in our free Google Colab Notebook here. To view the rest of our notebooks and model uploads, please visit our documentation.

## Performance benchmarks

ModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer context🤗Hugging Face+FA2Phi-424GB2x70%12x longer1xWe tested using the Alpaca  Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down).💕 Thank you! As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Thank you for reading!Daniel & Michael Han 🦥10 Jan 2025

## Fine-tune Phi-4 for free now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
