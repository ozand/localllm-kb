---
source_url: https://unsloth.ai/blog/gpt-oss-context
slug: gpt-oss-context
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: gpt-oss-context

Blog

# Long context gpt-oss Fine-tuning

## Aug 28, 2025 • By Daniel & Michael

## Aug 28, 2025

## •

## By Daniel & Michael

We’re excited to introduce Unsloth Flex Attention support for OpenAI gpt-oss training that enables >8× longer context lengths, >50% less VRAM usage and >1.5× faster training vs. all implementations including those using Flash Attention 3 (FA3). Unsloth Flex Attention makes it possible to train with a 60K context length on just 80GB of VRAM for BF16 LoRA. Also:

- You can now export/save your QLoRA fine-tuned gpt-oss model to llama.cpp, vLLM, Ollama, or HF

- We fixed gpt-oss training losses going to infinity on float16 GPUs (like T4 Colab)

- We fixed gpt-oss implementation issues irrelevant to Unsloth, most notably ensuring that swiglu_limit = 7.0 is properly applied during MXFP4 inference in transformersgpt-oss-20b1xH100 80GB>8xlonger contextgpt-oss-20b1xH100 80GB>1.7xfastergpt-oss-20b1xH100 80GB>50%less VRAM🦥Introducing Unsloth Flex AttentionWith Unsloth Flex Attention, a single 80GB VRAM H100 can handle up to 81K context length with QLoRA and 60K context with BF16 LoRA. The more context length you use, the more gains you'll get from Unsloth Flex Attention:In comparison, all other non-Unsloth implementations max out at 9K context length on an 80GB GPU, and only reaches 15K context with FA3. But, FA3 is unsuitable for gpt-oss training since it lacks backward pass support for attention sinks. So if you were previously using FA3 for gpt-oss training, we'd recommend you to not use it for now. Thus, the max context length you can get without Unsloth on 80GB VRAM is ~9K.Training with Unsloth Flex Attention delivers at least a 1.3× speedup, with gains growing as context length increases, reaching up to 2× faster. Because Flex Attention scales with context, longer sequences yield bigger savings in both VRAM and training time.A huge thank you to Rohan Pandey for his Flex Attention implementation, which directly inspired the development of Unsloth Flex Attention.We tested using the Alpaca Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied LoRA on all linear layers (q, k, v, o, gate, up, down).📐Unsloth's Flex Attention implementationFlex Attention is extremely powerful as it provides the practitioner 2 customization routes for the attention mechanism - a score modifier (f) and a masking function (M).The score modifier (f) allows us to edit the attention logits before the softmax operation, and the masking function (M) allows us to skip operations if we don't need them (for eg sliding window attention only sees last 128 tokens).The trick is Flex Attention provides fast auto generated Triton kernels with arbitrary score modifiers and masking functions!This means we can use Flex Attention to implement attention sinks! Implementing a single attention sink is provided both in OpenAI's original gpt-oss repo and HuggingFace's transformers's implementation.combined_logits = torch.cat([attn_weights, sinks], dim=-1)

probs = F.softmax(combined_logits, dim=-1)

scores = probs[..., :-1]The above shows we concatenate the sink at the very end of the Q @ K.T , do the softmax, and remove the last column which was the sink token.By using some visualization utilities from Flex Attention's Github repo, we can visualize this. Assume the sequence length was 16, and a sliding window of 5. On the left is the last sink column (default implementation), and on the right is if we move the sink location to index 0 (our implementation).Interesting finding: The official Flex Attention sliding window implementations considers the window size as the number of last tokens PLUS ONE as it includes the current token. The HuggingFace and GPT OSS implementations strictly only sees the last N tokens. Ie the below is from Flex Attention and Attention Gym:def sliding_window_causal(b, h, q_idx, kv_idx):

causal_mask = q_idx >= kv_idx

window_mask = q_idx - kv_idx <= SLIDING_WINDOW

return causal_mask & window_maskWe also confirmed through OpenAI's official GPT-OSS implementation on whether we attend to the last N or N+1 tokens here:mask = torch.triu(Q.new_full((n_tokens, n_tokens), -float("inf")), diagonal=1)

if sliding_window > 0:

mask += torch.tril(

mask.new_full((n_tokens, n_tokens), -float("inf")), diagonal=-sliding_window

)🕶️ Attention SinksOpenAI's GPT OSS model uses an alternating pattern of sliding window attention, full attention, sliding window attention and so on (SWA, FA, SWA, FA, etc). Each sliding window only attends to 128 tokens (including the current token), so computation is vastly reduced. However, this also means long context retrieval and reasoning becomes useless due to the small sliding window. Most labs fix this by expanding the sliding window to 2048 or 4096 tokens.OpenAI leveraged Attention Sinks from the Efficient Streaming Language Models with Attention Sinks paper which shows that you can use a small sliding window, except you must add a global attention on the first token! The paper provides a good illustration below:The paper finds that the attention mechanism seems to assign a lot of weight to the first few tokens (1 to 4), and by removing them during the sliding window operation, since we can only see the last N (say 128) tokens, these "important" first few tokens disappear.If we plot log perplexity (higher is worse), and do long context inference after the pretrained model's context length, we see the perplexity shoots up (not good). However the red line (Attention Sinks) stays low, which is very good!The paper also shows that the Attention Is Off By One method does partially work, except one must also add a few extra sink tokens to get lower perplexities. The paper shows that adding a single sink token that is learnable does remarkably well!And that's what OpenAI did for GPT-OSS!The paper also shows that the Attention Is Off By One method does partially work, except one must also add a few extra sink tokens to get lower perplexities. The paper shows that adding a single sink token that is learnable does remarkably well!And that's what OpenAI did for GPT-OSS!💾New: Saving to GGUF, vLLM after gpt-oss trainingYou can now QLoRA fine-tune gpt-oss and directly save, export, or merge the model to llama.cpp, vLLM, or HF - not just Unsloth. We will be releasing a free notebook hopefully soon.Previously, any QLoRA fine-tuned gpt-oss model was restricted to running in Unsloth. We’ve removed that limitation by introducing on-demand dequantization of MXFP4 base models (like gpt-oss) during the LoRA merge process. This makes it possible to export your fine-tuned model in bf16 format.After fine-tuning your gpt-oss model, you can now merge it into a 16-bit format with a single command:`model.save_pretrained_merged(save_directory, tokenizer)`If you prefer to merge the model and push to the hugging-face hub directly instead,  you could do so using:`model.push_to_hub_merged(repo_name, tokenizer=tokenizer, token=hf_token)`

## ✨Fine-tuning gpt-oss directly

We also added support for directly fine-tuning of gpt-oss models by implementing patches that allow loading the native MXFP4 quantized format. This makes it possible to load the 'openai/gpt-oss' model with less than 24GB of VRAM, and QLoRA fine-tune it. Simply load the model using:model, tokenizer = FastLanguageModel.from_pretrained(

#model_name = "unsloth/gpt-oss-20b-BF16",

model_name = "unsloth/gpt-oss-20b",

dtype = dtype, # None for auto detection

max_seq_length = max_seq_length, # Choose any for long context!

load_in_4bit = True,  # 4 bit quantization to reduce memory

full_finetuning = False, # [NEW!] We have full finetuning now!

# token = "hf_...", # use one if using gated models

)🐛Bug Fixes for gpt-ossWe recently collaborated with Hugging Face to resolve inference issues by using OpenAI’s kernels and ensuring that swiglu_limit = 7.0 is correctly applied during MXFP4 inference.Based on user feedback, we discovered that extended QLoRA training runs (beyond 60 steps) could cause the loss to diverge and eventually error out. This issue only occurred on devices that do not support BF16 and instead fall back to F16 (e.g., T4 GPUs). Importantly, it did not impact QLoRA training on A100 or H100 GPUs, nor LoRA training on f16 GPUs.After extensive investigation, we’ve now aligned training loss behavior across all GPU setups, including GPUs limited to F16. If you were previously experiencing issues because of this, we recommend using our new updated gpt-oss notebook!We had to do many many experiments to move float16's training loss curve to be equivalent to bfloat16 machines (blue line). We found the following:Pure float16 will go to infinity on step 50We found the down projections in the MoE to have huge outliersActivations must be saved in bfloat16 or float32Below shows the absolute magnitude activations for GPT OSS 20B, and some really spike - this will overflow in float16 machines since float16's maximum range is 65504.We fixed this in Unsloth, so all float16 training works out of the box!📈gpt-oss-20b benchmarks We tested gpt-oss-20b and did LoRA on all linear layers (Q, K, V, O, gate, up and down) with rank = 32 with a batch size of 1. We padded all sequences to a certain maximum sequence length to mimic long context finetuning workloads.

## gpt-oss-20b BF16 LoRA - Context Length vs/ GPU VRAM

Context LengthUnsloth(+ Flex A)Official Cookbook + FA3Official Cookbook102445.246.647.3204845.9449.751.3409647.0756.171.1819249.2768.7OOM16,38454OOMOOM32,76863.73OOMOOM61,23480OOMOOM💕 Thank you! As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and our newsletter on: Substack.Thank you for reading!Daniel & Michael Han 🦥Aug 28, 2025

## Fine-tune gpt-oss now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
