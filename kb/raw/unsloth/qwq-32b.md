---
source_url: https://unsloth.ai/blog/qwq-32b
slug: qwq-32b
captured_date: 2026-08-25
status: raw_capture
provenance: unsloth_blog_first_party
---

# Unsloth Technical Capture: qwq-32b

Blog

# Run QwQ-32B effectively + Bug Fixes

## Mar 7, 2025 • By Daniel & Michael

## Mar 7, 2025

## •

## By Daniel & Michael

Qwen released QwQ-32B, a powerful reasoning model with performance comparable to DeepSeek-R1 across multiple benchmarks. You may have encountered issues such as infinite loops, repetitions, <think> token errors, and fine-tuning challenges, which do not reflect the model’s true quality. We hope this blog will help debug and fix most issues! View TutorialOur model uploads include bug fixes and work for fine-tuning, vLLM and Transformers, however if you're using llama.cpp and engines that use llama.cpp as backend you might have experienced issues. To solve the issues follow our tutorial below or read our detailed guide + analysis in our docs here.See all Unsloth fixed QwQ-32B uploads including GGUF & dynamic 4-bit on here.QwQ-32B Bug Fixes

We found a few issues as well specifically impacting finetuning! The EOS token is correct, but the PAD token should probably rather be "<|vision_pad|>" We updated it in here.

"eos_token": "<|im_end|>",

"pad_token": "<|endoftext|>",⚙️ Official Recommended Settings

According to Qwen, these are the recommended settings for inference:

- Temperature of 0.6Top_K of 40 (or 20 to 40)Min_P of 0.0Top_P of 0.95

- Repetition Penalty of 1.0. (1.0 means disabled in llama.cpp and transformers)

- Chat template: <|im_start|>user\nCreate a Flappy Bird game in Python.<|im_end|>\n<|im_start|>assistant\n<think>\n👍 Recommended settings for llama.cppWe noticed many people use a Repetition Penalty greater than 1.0. For example 1.1 to 1.5. This actually interferes with llama.cpp's sampling mechanisms. The goal of a repetition penalty is to penalize repeated generations, but we found this doesn't work as expected.Turning off Repetition Penalty also works (ie setting it to 1.0), but we found using it to be useful to penalize endless generations.To use it, we found you must also edit the ordering of samplers in llama.cpp to before applying Repetition Penalty, otherwise there will be endless generations. So add this:`--samplers "top_k;top_p;min_p;temperature;dry;typ_p;xtc"`By default, llama.cpp uses this ordering:`--samplers "dry;top_k;typ_p;top_p;min_p;xtc;temperature"`We reorder essentially temperature and dry, and move min_p forward. This means we apply samplers in this order:top_k=40

top_p=0.95

min_p=0.0

temperature=0.6

dry

typ_p

xtc📖 Tutorial: Run QwQ-32B with Fixes

## 1. For llama.cpp & engines that use llama.cpp:

You can read our complete guide in our docs here. Obtain the latest llama.cpp at: github.com/ggml-org/llama.cpp. You can follow the build instructions below as well. Change -DGGML_CUDA=ON to -DGGML_CUDA=OFF if you don't have a GPU or just want CPU inference.

apt-get update

apt-get install build-essential cmake curl libcurl4-openssl-dev -y

git clone https://github.com/ggerganov/llama.cpp

cmake llama.cpp -B llama.cpp/build \

-DBUILD_SHARED_LIBS=ON -DGGML_CUDA=ON -DLLAMA_CURL=ON

cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split

cp llama.cpp/build/bin/llama-* llama.cpp

## 2. Download the model + Test

Download the model via (after installing pip install huggingface_hub hf_transfer ). You can choose Q4_K_M, or other quantized versions (like BF16 full precision). Other variants: huggingface.co/unsloth/QwQ-32B-GGUFThen run Unsloth's Flappy Bird test, which will save the output to Q4_K_M_yes_samplers.txt

# !pip install huggingface_hub hf_transfer

import os

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

from huggingface_hub import snapshot_download

snapshot_download(

repo_id = "unsloth/QwQ-32B-GGUF",

local_dir = "unsloth-QwQ-32B-GGUF",

allow_patterns = ["*Q4_K_M*"], # For Q4_K_M

)

## 3. Test/Evaluate

Edit --threads 32 for the number of CPU threads, --ctx-size 16384 for context length, --n-gpu-layers 99 for GPU offloading on how many layers. Try adjusting it if your GPU goes out of memory. Also remove it if you have CPU only inference.We use --repeat-penalty 1.1 and --dry-multiplier 0.5 which you can adjust.

./llama.cpp/llama-cli \

--model unsloth-QwQ-32B-GGUF/QwQ-32B-Q4_K_M.gguf \

--threads 32 \

--ctx-size 16384 \

--n-gpu-layers 99 \

--seed 3407 \

--prio 2 \

--temp 0.6 \

--repeat-penalty 1.1 \

--dry-multiplier 0.5 \

--min-p 0.01 \

--top-k 40 \

--top-p 0.95 \

-no-cnv \

--samplers "top_k;top_p;min_p;temperature;dry;typ_p;xtc" \

--prompt "<|im_start|>user\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|im_end|>\n<|im_start|>assistant\n<think>\n"  \

2>&1 | tee Q4_K_M_yes_samplers.txt

See example final Python output here. The full input is:

<|im_start|>user

Create a Flappy Bird game in Python. You must include these things:

1. You must use pygame.

2. The background color should be randomly chosen and is a light shade. Start with a light blue color.

3. Pressing SPACE multiple times will accelerate the bird.

4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.

5. Place on the bottom some land colored as dark brown or yellow chosen randomly.

6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.

7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.

8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.

The final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|im_end|>

<|im_start|>assistant

<think>

When running it, we get a runnable game!

## 4. Try without our Fixes:

Now try the same without our fixes! So remove --samplers "top_k;top_p;min_p;temperature;dry;typ_p;xtc" This will save the output to Q4_K_M_no_samplers.txt./llama.cpp/llama-cli \

--model unsloth-QwQ-32B-GGUF/QwQ-32B-Q4_K_M.gguf \

--threads 32 \

--ctx-size 16384 \

--n-gpu-layers 99 \

--seed 3407 \

--prio 2 \

--temp 0.6 \

--repeat-penalty 1.5 \

--repeat-penalty 1.1 \

--dry-multiplier 0.5 \

--min-p 0.1 \

--top-k 40 \

--top-p 0.95 \

-no-cnv \

--prompt "<|im_start|>user\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|im_end|>\n<|im_start|>assistant\n<think>\n"  \

2>&1 | tee Q4_K_M_no_samplers.txtYou will get some looping, but problematically incorrect Python syntax and many other issues. For example the below looks correct, but is wrong! Ie line 39 pipes.clear() ### <<< NameError: name 'pipes' is not defined. Did you forget to import 'pipes'? See our example which shows totally incorrect results hereIf you use --repeat-penalty 1.5, it gets even worse and more obvious, with actually totally incorrect syntax.You might be wondering maybe it's Q4_K_M? B16 ie full precision should work fine right? Incorrect - the outputs again fail if we do not use our fix of --samplers "top_k;top_p;min_p;temperature;dry;typ_p;xtc" when using a Repetition Penalty.💡 <think> token not shown?

Some people are reporting that because <think> is default added in the chat template, some systems are not outputting the thinking traces correctly. You will have to manually edit the Jinja template from:

`{%- if tools %} {{- '<|im_start|>system\n' }} {%- if messages[0]['role'] == 'system' %} {{- messages[0]['content'] }} {%- else %} {{- '' }} {%- endif %} {{- "\n\n# Tools\n\nYou may call one or more functions to assist with the user query.\n\nYou are provided with function signatures within <tools></tools> XML tags:\n<tools>" }} {%- for tool in tools %} {{- "\n" }} {{- tool | tojson }} {%- endfor %} {{- "\n</tools>\n\nFor each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:\n<tool_call>\n{\"name\": <function-name>, \"arguments\": <args-json-object>}\n</tool_call><|im_end|>\n" }} {%- else %} {%- if messages[0]['role'] == 'system' %} {{- '<|im_start|>system\n' + messages[0]['content'] + '<|im_end|>\n' }} {%- endif %} {%- endif %} {%- for message in messages %} {%- if (message.role == "user") or (message.role == "system" and not loop.first) %} {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }} {%- elif message.role == "assistant" and not message.tool_calls %} {%- set content = message.content.split('</think>')[-1].lstrip('\n') %} {{- '<|im_start|>' + message.role + '\n' + content + '<|im_end|>' + '\n' }} {%- elif message.role == "assistant" %} {%- set content = message.content.split('</think>')[-1].lstrip('\n') %} {{- '<|im_start|>' + message.role }} {%- if message.content %} {{- '\n' + content }} {%- endif %} {%- for tool_call in message.tool_calls %} {%- if tool_call.function is defined %} {%- set tool_call = tool_call.function %} {%- endif %} {{- '\n<tool_call>\n{"name": "' }} {{- tool_call.name }} {{- '", "arguments": ' }} {{- tool_call.arguments | tojson }} {{- '}\n</tool_call>' }} {%- endfor %} {{- '<|im_end|>\n' }} {%- elif message.role == "tool" %} {%- if (loop.index0 == 0) or (messages[loop.index0 - 1].role != "tool") %} {{- '<|im_start|>user' }} {%- endif %} {{- '\n<tool_response>\n' }} {{- message.content }} {{- '\n</tool_response>' }} {%- if loop.last or (messages[loop.index0 + 1].role != "tool") %} {{- '<|im_end|>\n' }} {%- endif %} {%- endif %} {%- endfor %} {%- if add_generation_prompt %} {{- '<|im_start|>assistant\n<think>\n' }} {%- endif %}`

to another by removing the <think>\n at the end. The model will now have to manually add <think>\n during inference, which might not always succeed. DeepSeek also edited all models to default add a <think> token to force the model to go into reasoning model.So change {%- if add_generation_prompt %} {{- '<|im_start|>assistant\n<think>\n' }} {%- endif %} to {%- if add_generation_prompt %} {{- '<|im_start|>assistant\n' }} {%- endif %} ie remove <think>\nSee full jinga template with removed <think>\n part here.

🧪 Experimental Results + Notes

We first thought maybe:

- QwQ's context length was not natively 128K, but rather 32K with YaRN extension. We tried overriding llama.cpp's YaRN handling, but nothing changed.  For example in the QwQ-32B readme file we see the below:{

...,

"rope_scaling": {

"factor": 4.0,

"original_max_position_embeddings": 32768,

"type": "yarn"

}

}

- We also thought maybe the RMS Layernorm epsilon was wrong - not 1e-5 but maybe 1e-6. For example this has rms_norm_eps=1e-06, whilst this has rms_norm_eps=1e-05 . We also overrided it, but it did not work:

- We also tested if tokenizer IDs matched between llama.cpp and normal Transformers courtesy of @kalomaze. They matched, so this was not the culprit. We provide our experimental results in our docs.🦥 Dynamic 4-bit Quants

We also uploaded dynamic 4-bit quants which increase accuracy vs naive 4-bit quantizations! We uploaded dynamic 4-bit quants to here. We attached the QwQ quantization error plot analysis for both activation and weight quantization errors below:Since vLLM 0.7.3 (2025 Feb 20), vLLM now supports loading Unsloth dynamic 4-bit quants!

🛠️ Finetuning QwQ-32BQwQ-32B1xL4 24GB13xlonger contextQwQ-32B1xL4 24GB2xfasterQwQ-32B1xL4 24GB>70%less VRAMQwQ-32B finetuning fits with Unsloth in under 20GB of VRAM! It’s also 2x faster, and default uses our dynamic 4-bit quants for superior accuracy for QLoRA.Due to the model size, unfortunately the model does not fit on free Google Colab 16GB VRAM GPUs so you will need a GPU with at least 20GB VRAM. To view the rest of our notebooks and model uploads, please visit our documentation.

## Performance benchmarks

ModelVRAM🦥Unsloth speed🦥 VRAM reduction🦥 Longer context🤗Hugging Face+FA2QwQ-32B24GB2x70%13x longer1xWe tested using the Alpaca  Dataset, a batch size of 2, gradient accumulation steps of 4, rank = 32, and applied QLoRA on all linear layers (q, k, v, o, gate, up, down).💕 Thank you! Thank you to everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our Reddit page and Discord server for help or just to show your support! You can also follow us on Twitter and join our newsletter.Thank you for reading!Daniel & Michael Han 🦥7 Mar 2025

## Fine-tune Phi-4 for free now!

Get started for free  unsloth

[email protected]

### Product

Unsloth DesktopModelsDocumentationDownload

### Company

AboutBlogNewsletterSupport

### Community
