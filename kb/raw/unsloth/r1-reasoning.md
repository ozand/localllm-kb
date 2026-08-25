---
source_url: https://unsloth.ai/blog/r1-reasoning
slug: r1-reasoning
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: r1-reasoning

Blog

# Train your own R1 reasoning model with Unsloth (GRPO)

## Feb 6, 2025 • By Daniel & Michael

## Feb 6, 2025

## •

## By Daniel & Michael

Feb 20, 2025 Update: You can now train your own reasoning model with just 5GB VRAM (down from 7GB VRAM) + 10x longer context lengths with Unsloth! Read update here!View our step-by-step Tutorial in our docs here!Today, we're excited to introduce reasoning in Unsloth! DeepSeek’s R1 research revealed an “aha moment” where R1-Zero autonomously learned to allocate more thinking time without human feedback by using Group Relative Policy Optimization (GRPO).We've enhanced the entire GRPO process, making it use 80% less VRAM than Hugging Face + FA2. This allows you to reproduce R1-Zero's "aha moment" on just 7GB of VRAM using Qwen2.5 (1.5B).Try our free GRPO notebook: Llama 3.1 (8B) or our advanced GRPO notebook for much better results: Qwen3 (4) on Colab❤️ P.S. thanks for the love on our R1 Dynamic 1.58-bit GGUF last week & don't forget to ⭐Star us: github.com/unslothai/unsloth💡 Main Details

- With 15GB VRAM, Unsloth allows you to transform any model up to 15B parameters like Llama 3.1 (8B), Phi-4 (14B), Mistral (7B) or Qwen2.5 (7B) into a reasoning model

- Minimum requirement: Just  7GB VRAM is enough to train your own reasoning model locally.

- The incredible team at Tiny-Zero demonstrated that you could achieve your own "aha" moment with Qwen2.5 (1.5B) - but it required 2xA100 GPUs (160GB VRAM). Now, with Unsloth, you can achieve the same "aha" moment using just a single 7GB VRAM GPU

- Previously, GRPO was only supported for full fine-tuning, but we've made it work with QLoRA and LoRA

- Please note, this isn’t fine-tuning DeepSeek’s R1 distilled models or using distilled data from R1 for tuning which Unsloth already supported. This is converting a standard model into a full-fledged reasoning model using GRPO.

- Use cases for GRPO include: If you want to make a customized model with rewards (say for law, medicine etc.), then GRPO can help.If you have input and output data (like questions and answers), but do not have the chain of thought or reasoning process, GRPO can magically create the reasoning process for you! + much more🤔 GRPO + The "aha" momentDeepSeek’s researchers observed an "aha moment" when training R1-Zero with pure reinforcement learning (RL). The model learned to extend its thinking time by reevaluating its initial approach, without any human guidance or predefined instructions.In a test example, even though we only trained Phi-4 with 100 steps using GRPO, the results are already clear. The model without GRPO does not have the thinking token, whilst the one trained with GRPO does and also has the correct answer.This magic could be recreated through GRPO, a RL algorithm that optimizes responses efficiently without requiring a value function, unlike Proximal Policy Optimization (PPO) which relies on a value function. In our notebooks, we train a model with GRPO, aiming for it to develop its own self-verification and search abilities autonomously - creating a mini "aha moment".How it works:

- The model generates groups of responses.

- Each response is scored based on correctness or another metric created by some set reward function rather than an LLM reward model.

- The average score of the group is computed.

- Each response's score is compared to the group average.

- The model is reinforced to favor higher-scoring responses.As an example, assume we want a model to solve:What is 1+1?  >>  Chain of thought/working out  >>  The answer is 2.What is 2+2?  >>  Chain of thought/working out  >>  The answer is 4.Originally, one had to collect large swathes of data to fill the working out / chain of thought process. But GRPO (the algorithm DeepSeek uses) or other RL algorithms can steer the model to automatically exhibit reasoning capabilities and create the reasoning trace. Instead, we need to create good reward functions or verifiers. For example, if it gets the correct answer, give it a score of 1. If some words are mis-spelt, minus 0.1. And so on! We can provide many many functions to reward the process.

## 🦥 GRPO in Unsloth

If you're using GRPO with Unsloth locally, please "pip install diffusers" as well as it is a dependency.Wait for at least 300 steps for the reward to actually increase and please use the latest version of vLLM. Keep in mind that our example on Colab was just trained in an hour so the results are subpar. In order to get good results, you will need to train for at least 12 hours (this is how GRPO works), but keep in mind this isn't compulsory as you can stop at anytime.It's advised to apply GRPO to a model at least 1.5B in parameters to correctly generate thinking tokens as smaller models may not.  If you’re using a base model, ensure you have a chat template. Training loss tracking for GRPO is now built directly into Unsloth, eliminating the need for external tools like wandb etc.In addition to adding GRPO support, we subsequently have support for Online DPO, PPO and RLOO as well! More details can be seen in Keith’s post and blog that includes the Github fork on how he got Online DPO working. The initial draft of GRPO changes on Google Colab can be seen in Joey’s tweet as well! Both of their contributions allowed us to also make support for the other generation based RL methods. See below for a graph comparison of Unsloth's Online DPO VRAM consumption vs standard Hugging Face + FA2.✨ Unsloth x vLLM

## 20x more throughput, 50% VRAM savings:

You can now use vLLM directly in your finetuning stack, which allows for much more throughput and allows you to finetune and do inference on the model at the same time! On 1x A100 40GB, expect 4000 tokens / s or so with Unsloth’s dynamic 4bit quant of Llama 3.2 3B Instruct. On a 16GB Tesla T4 (free Colab GPU), you can get 300 tokens / s.We also magically removed double memory usage when loading vLLM and Unsloth together, allowing for savings of 5GB or so for Llama 3.1 8B and 3GB for Llama 3.2 3B (thanks to inspiration from Boris). Unsloth could originally finetune Llama 3.3 70B Instruct in 1x 48GB GPU with Llama 3.3 70B weights taking 40GB of VRAM. If we do not remove double memory usage, then we’ll need >= 80GB of VRAM when loading Unsloth and vLLM together.But with Unsloth, you can still finetune and get the benefits of fast inference in one package in under 48GB of VRAM! To use fast inference, first install vllm, and instantiate Unsloth with fast_inference:pip install unsloth vllm

from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(

model_name = "unsloth/Llama-3.2-3B-Instruct",

fast_inference = True,

)

model.fast_generate(["Hello!"])

## vLLM Findings in Unsloth

- vLLM can now load Unsloth Dynamic 4-bit quants. Just like our 1.58bit Dynamic R1 GGUF, we showed that dynamically quantizing certain layers to 4-bit and some to 16-bit can dramatically improve accuracy whilst keeping the model small.

- We auto select multiple parameters to account for RAM, VRAM efficiency and maximum throughput (like # of chunked prefill tokens, # max sequences etc). We enable -O3 in vLLM by default and enable prefix caching. We found Flashinfer on old GPUs to be actually 10% slower. FP8 KV cache makes things 10% slower, but doubles throughput potential.

- We allow LoRA loading in vLLM via parsing a state dict instead of loading from disk - this can make your GRPO training runs 1.5x faster. An active area of research is to somehow directly edit the LoRA adapters in vLLM (I’m not sure how to yet). This can boost speeds a lot, since we’re doing unnecessary GPU data movement now.

- vLLM will have random VRAM spikes weirdly, especially during batched generation. We added a batched generate function to reduce memory spikes.💕 Thank you! A huge thank you to Keith, Edd, Datta, MrDragonFox and Joey for their amazing help with this project. And, of course, the incredible folks at Hugging Face especially the TRL team, vLLM, and the open-source community for their contributions to making this possible. As usual, a huge thank you to everyone for using & sharing Unsloth. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and newsletter.Thank you for reading!Daniel & Michael Han 🦥6 Feb 2025

## Fine-tune Vision models now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
