---
source_url: https://unsloth.ai/blog/deepseek-r1
slug: deepseek-r1
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: deepseek-r1

Blog

# Run & Finetune DeepSeek-R1

## Jan 20, 2025 • By Daniel & Michael

## Jan 20, 2025

## •

## By Daniel & Michael

DeepSeek’s new R1 models sets new benchmarks in reasoning performance, matching OpenAI’s o1 model. It follows the recently launched DeepSeek-V3, the most powerful open-source AI model to date. DeepSeek also distilled from R1 and fine-tuned it on Llama 3 and Qwen 2.5 models, meaning you can now also fine-tune the models out of the box with Unsloth.See our collection for all versions of the R1 model series including GGUF's, 4-bit and more! huggingface.co/collections/unsloth/deepseek-r1Jan 27, 2025 update: We've released 1.58-bit Dynamic GGUFs for DeepSeek-R1 allowing you to run R1 even better with a 80% size reduction: 1.58-bit Dynamic R1Feb 6, 2025 update: You can now train your own reasoning model like R1 using: GRPO + Unsloth🖥️ How to Run DeepSeek-R1 modelsRunning DeepSeek-R1 comes with challenges: its unquantized 8-bit version is a massive 700GB, trained originally in FP8. Direct GGUF conversion is not feasible, as GGUF requires FP16 so we converted it to FP16 and made the GGUF versions available. Thankfully, the DeepSeek team has created R1 Llama and Qwen distilled models that are much smaller and can easily be run locally on your own device.To run DeepSeek-R1 / R1-Zero, you'll need to install the open-source package llama.cpp, the original framework for using GGUF files. Hardware requirements: You do not need a GPU, a CPU with RAM will suffice, but make sure you have enough disk space.

## 🦙 Using llama.cpp:

These instructions work for the R1 distilled and non distilled models, however keep in mind that they will require different hardware requirements. See further below for R1 requirements.

- Do not forget about `<｜User｜>` and `<｜Assistant｜>` tokens! - Or use a chat template formatter

- You must obtain the latest `llama.cpp` version at: github.com/ggerganov/llama.cpp

- Example with Q8_0 K quantized cache **Notice -no-cnv disables auto conversation mode

./llama.cpp/llama-cli \

--model unsloth/DeepSeek-R1-Distill-Llama-8B-GGUF/DeepSeek-R1-Distill-Llama-8B-Q4_K_M.gguf \

--cache-type-k q8_0 \

--threads 16 \

--prompt '<｜User｜>What is 1+1?<｜Assistant｜>' \

-no-cnv

Example output:

<think>

Okay, so I need to figure out what 1 plus 1 is. Hmm, where do I even start? I remember from school that adding numbers is pretty basic, but I want to make sure I understand it properly.

Let me think, 1 plus 1. So, I have one item and I add another one. Maybe like a apple plus another apple. If I have one apple and someone gives me another, I now have two apples. So, 1 plus 1 should be 2. That makes sense.

Wait, but sometimes math can be tricky. Could it be something else? Like, in a different number system maybe? But I think the question is straightforward, using regular numbers, not like binary or hexadecimal or anything.

I also recall that in arithmetic, addition is combining quantities. So, if you have two quantities of 1, combining them gives you a total of 2. Yeah, that seems right.

Is there a scenario where 1 plus 1 wouldn't be 2? I can't think of any...

- If you have a GPU (RTX 4090 for example) with 24GB, you can offload multiple layers to the GPU for faster processing. If you have multiple GPUs, you can probably offload more layers.

./llama.cpp/llama-cli \

--model unsloth/DeepSeek-R1-Distill-Llama-8B-GGUF/DeepSeek-R1-Distill-Llama-8B-Q4_K_M.gguf

--cache-type-k q8_0

--threads 16

--prompt '<｜User｜>What is 1+1?<｜Assistant｜>'

--n-gpu-layers 20 \

-no-cnv

## Hardware Requirements for R1 / Zero:

A GPU will not necessary. You’ll just need a CPU with at least 48GB of RAM and at least 250GB of disk space.Although these are the minimum requirements, performance may be very slow. Expect less than 1.5 tokens per second on minimal hardware - but that doesn't mean you can't experiment! Using a GPU will make your inference faster.Below is a table of details for DeepSeek-R1 GGUF quants, including disk space requirements:

| R1 Quants

| Disk Size

| Details

| Q2_K_XS

| 207GB

| Q2 everything, Q4 embed, Q6 lm_head

| Q2_K_L

| 228GB

| Q3 down_proj Q2 rest, Q4 embed, Q6 lm_head

| Q3_K_M

| 298GB

| Standard Q3_K_M

| Q4_K_M

| 377GB

| Standard Q4_K_M

| Q5_K_M

| 443GB

| Standard Q5_K_M

| Q6_K

| 513GB

| Standard Q6_K

| Q8_0

| 712GB

| Standard Q8_0

⚙️Fine-tuning DeepSeek R1Fine-tuning reasoning models is still a relatively new area of exploration. However, since DeepSeek's distilled models are built on Llama and Qwen architectures, they are fully compatible with Unsloth out of the box.We will soon provide a dedicated example notebook for fine-tuning reasoning models. In the meantime, you can use our existing Llama or Qwen Colab notebooks for free fine-tuning. Simply update the model names to match the appropriate ones. For instance, replace 'unsloth/Meta-Llama-3.1-8B' with 'unsloth/DeepSeek-R1-Distill-Llama-8B-unsloth-bnb-4bit'.You can view all our current free fine-tuning notebooks here.💕 Thank you! As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and newsletter.Thank you for reading!Daniel & Michael Han 🦥20 Jan 2025

## Fine-tune Vision models now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
