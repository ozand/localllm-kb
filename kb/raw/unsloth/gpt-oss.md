---
source_url: https://unsloth.ai/blog/gpt-oss
slug: gpt-oss
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: gpt-oss

Blog

# Fine-tune gpt-oss with Unsloth

## Aug 8, 2025 • By Daniel & Michael

## Aug 8, 2025

## •

## By Daniel & Michael

OpenAI's new gpt-oss open models, achieves SOTA performance in text, reasoning, math and code. gpt-oss-120b rivals o4-mini and gpt-oss-20b rivals o3-mini and both models outperform o1 and GPT-4o.We’ve managed to make gpt-oss train on just 14GB of VRAM, making it possible to work on free Colab. We also did some chat template fixes for the model which you can view below.

- Fine-tune gpt-oss-20b for free using our Colab notebook

- Unsloth gpt-oss fine-tuning is 1.5x faster, uses 70% less VRAM, and supports 10x longer context lengths. gpt-oss-20b LoRA training fits on a 14GB VRAM, and gpt-oss-120b works on 65GB VRAM.

- We uploaded all versions of gpt-oss, including Dynamic GGUFs, 4-bit, and 16-bit versions, on Hugging Face here.

- Go to our docs to read a detailed guide on How to Run & Fine-tune gpt-oss here.

## 🦥 Unsloth fixes for gpt-oss

OpenAI released a standalone parsing and tokenization library called Harmony which allows one to tokenize conversations to OpenAI's preferred format. The official OpenAI cookbook article provides many more details on how to use the Harmony library. Appendix 1 in the Model Card for gpt-oss also provides some insights.Inference engines generally use the jinja chat template, and we found a few issues with them after using Harmony directly. If you see below, the top is the correct rendered from as from Harmony. The below is the one rendered by the current jinja chat template.We made some functions to directly allow you to use OpenAI's Harmony library directly without a jinja chat template if you desire - you can simply use normal conversations like below:`messages = [    {"role" : "user", "content" : "What is 1+1?"},    {"role" : "assistant", "content" : "2"},    {"role": "user",  "content": "What's the temperature in San Francisco now? How about tomorrow? Today's date is 2024-09-30."},    {"role": "assistant",  "content": "User asks: 'What is the weather in San Francisco?' We need to use get_current_temperature tool.", "thinking" : ""},    {"role": "assistant", "content": "", "tool_calls": [{"name": "get_current_temperature", "arguments": '{"location": "San Francisco, California, United States", "unit": "celsius"}'}]},    {"role": "tool", "name": "get_current_temperature", "content": '{"temperature": 19.9, "location": "San Francisco, California, United States", "unit": "celsius"}'},]`Then use the encode_conversations_with_harmony function from Unsloth.`from unsloth_zoo import encode_conversations_with_harmonydef encode_conversations_with_harmony(    messages,    reasoning_effort = "medium",    add_generation_prompt = True,    tool_calls = None,    developer_instructions = None,    model_identity = "You are ChatGPT, a large language model trained by OpenAI.",)`The harmony format includes multiple interesting things:

- reasoning_effort = "medium" You can select low, medium or high, and this changes gpt-oss's reasoning amount.

- developer_instructions is like a system prompt which you can add.

- model_identity is best left alone - you can edit it, but we're unsure if custom ones will function.We find multiple issues with the current jinja chat template:

- Function and tool calls are rendered with tojson, which is fine it's a dict, but if it's a string, speech marks and other symbols become backslashed.

- There are some extra new lines in the jinja template on some boundaries.

- Tool calling thoughts from the model should have the analysis tag and not final tag.Our chat templates for the GGUF, our uploads and all versions are fixed! For example when comparing both ours and Harmony's format, we get no different characters:✨ gpt-oss Fine-tuning with UnslothYou may have noticed in our newest update in July, that every single model now trains faster while also utilizing even less VRAM. Our latest algorithmic changes allows for 10 to 25% less VRAM consumption for all models, no matter the type (mamba, TTS) etc. Also you'll experience faster compiling and less errors making Unsloth more stable!

## 💾  Making efficient gpt-oss fine-tuning work:

We found that the gpt-oss' MXFP4 format while being efficient, doesn't support training. So, we had to implement custom training functions for the layers that use MXFP4 to make it work while ensuring we do not compromise on speed.We utilized OpenAI's Triton Kernels library directly to allow MXFP4 inference. For finetuning / training however, the MXFP4 kernels do not yet support training, since the backwards pass is not yet implemented. We're actively working on implementing it in Triton! There is a flag called W_TRANSPOSE as mentioned , which should be implemented. The derivative can be calculated by the transpose of the weight matrices, and so we have to implement the transpose operation.As a result, if you want to train gpt-oss with any library other than Unsloth, you’ll need to upcast the weights to bf16 before training. This approach, however, significantly increases both VRAM usage and training time by as much as 300% more memory usage! ALL other training methods will require a minimum of 65GB VRAM to train the 20b model while Unsloth only requires 14GB VRAM (-80%).Explanation: Both models are Mixture of Experts (MoE), and the smaller 20B model choses top 4 experts out of 32 total experts, its bigger brother, the 120B activates 4 experts per token out of the total 128 experts. During training (and release), the MoE is set to use MXFP4 format for its weights. On top of that, the weights are stored as Parameter (nn.Paramter) instead of being stored as linear layers (nn.Linear) like it is generally done. This makes quantisation hard. Especially since this is MoE and MLP/Experts contributes to approximately 19B of the total 20B parameters. So quantising this and performing the operations efficiently becomes crucial.To make quantization with BitsandBytes, we converted the weights and the architecture from the aforementioned Parameter format to the Linear format.Thus, gpt-oss-20b finetuning is able to fit in under 14GB of VRAM with Unsloth!

## Performance benchmarks

ModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer contextStandard + FA2gpt-oss-20b14GB1.5x>50%5xlongerOOMgpt-oss-120b65GB1.5x>50%5xlongerOOMWe tested using the Alpaca  Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down).

## Other amazing model support

We also worked with the Falcon (TII) and LiquidAI teams to support their latest models so please let us know how they are! GLM 4.5 models are also now supported.

- Falcon hybrid Mamba arch: 0.5B Conversational notebook

- LiquidAI's hybrid convolutional arch: 1.2B Alpaca notebook

- For the rest of our notebooks, see our docs page💕 Thank you! A huge thank you everyone for using & supporting Unsloth - we really appreciate it. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Thank you for reading!Daniel & Michael Han 🦥Aug 8, 2025

## Fine-tune gpt-oss now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
