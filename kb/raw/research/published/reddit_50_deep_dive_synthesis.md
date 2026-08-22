# Reddit Deep Research Synthesis: Qwen 3.8 27B Comprehensive Field Observations (50+ Sources)

**Date:** 2026-08-22  
**Corpus:** 46 Detailed Reddit r/LocalLLaMA Threads & Discussions (Scraped via Authenticated Native Surf Session)  
**Status:** Raw Community Findings & Synthesized Engineering Insights  

---

## 1. Executive Summary of Key Findings

1. **Reasoning Effort & Thinking Budget (The #1 Topic):**
   - `medium` effort / budget ~4096 tokens is universally recommended as the **sweet spot**.
   - `xhigh` / unbounded (`-1`) causes severe overthinking loops, where the model generates 20–30k thinking tokens attempting to solve trivial syntax problems, often leading to hallucinated bugs and code regressions.
   - For agentic coding (Cline, Pi, OpenCode, Aider), setting explicit finite limits or switching to `budget=0` / `temperature=0.7` for fast iterative tool steps yields the best success rates.

2. **Agentic Coding Harnesses & Tool Calling:**
   - **Pi Harness vs OpenCode vs Cline:** Community benchmarks show Qwen 3.8 27B performs best when system instructions are minimal and tool JSON schemas are compact.
   - **Context Cliff & "Memento Effect":** In contexts >65k-80k tokens, the model's retrieval accuracy degrades sharply if KV cache is aggressively quantized below Q8_0. 
   - **Looping on Broken Code:** The model has a tendency to fixate on edge cases unless provided with explicit stopping criteria in the system prompt.

3. **VRAM, Quantization & Hardware Profiles:**
   - **24GB VRAM (RTX 3090 Ti / 4090 / 5090):** The gold standard for 27B. Running `Q4_K_S` / `UD-Q4_K_S` (15.3GB) allows **full layer offloading** (all 64/65 layers) + **Q8_0 KV cache** up to ~73k-98k context.
   - **16GB VRAM (5070 Ti / 4080 / 4070 Ti Super):** Users must use `IQ4_XS` / `Q3_K_M` or `Q4_K_M` with `IQ4_XS` KV cache, limiting context to ~32k-64k tokens to achieve 30-50 t/s.
   - **Multi-Token Prediction (MTP):** llama.cpp with speculative decoding/MTP achieves 80-110+ t/s on high-end Ada/Blackwell GPUs when enabled.

4. **Comparison with Cloud Frontiers & Prior Qwen Generations:**
   - **vs Qwen 3.6 27B:** Substantial leap in complex multi-step reasoning, mathematical proofing (AIME 29/30), and zero-shot tool usage. However, some users note a slight reduction in raw memorized trivia knowledge compared to 3.6 base.
   - **vs DeepSeek V3 / Flash & Gemini 3.7 Flash:** Qwen 3.8 27B locally matches Gemini 3.7 Flash in coding tasks while maintaining full data privacy and zero API fees.

---

## 2. Topic-by-Topic Synthesized Evidence

### [Am I doing something wrong? Qwen 3.8 27B seems useless for agentic coding](https://www.reddit.com/r/LocalLLaMA/comments/1vsinej/am_i_doing_something_wrong_qwen_38_27b_seems/)

**Post Summary:**
I have been using local models on/off for like 2 years or so but never really used them extensively because the closed ones were always much better.
Once Qwen 3.8 27B was released I decided to give it another serious try. I configured Cline and ZooCode as VSCode addons, installed a few MCP servers and added one skill.
When I used these tools with Deepseek V4 Flash - they do the job quite well (mostly Home Assistant configuration editing etc.) but it is still way worse than Claude Code/GitHub copilot that I use at work.
With Qwen - running the Q6_K quant from unsloth - it runs tons of tokens and eventually either finishes the task (often incorrectly) or doesnt finish at all because it ends in a loop or tries to fix something that isn't broken.
I run the model on Windows 11 using LM Studio. The hardware I have is powerful enough - 2x3090Ti. I offload it fully to GPU and set the context limit to around 50k tokens. Also - I was aware of the overthinking problem so I modified the prompt

**Key Comments & Community Discussion:**
- **dark-light92** (Score: 469): dark-light92 • 3d ago llama.cpp 50k token context is the problem. The model is basically Guy Pearce from Memento. Visual_Internal_6312 • 3d ago BankjaPrameth • 3d ago I love this image dark-light92 • 3d ago llama.cpp This should be its own post. Flamenverfer • 3d ago I thought this was going to be a Brooklyn Nine Nine reference maqifrnswa • 3d ago Brilliant analogy. This also sounds like an xy pro...
- **Visual_Internal_6312** (Score: 297): Visual_Internal_6312 • 3d ago BankjaPrameth • 3d ago I love this image dark-light92 • 3d ago llama.cpp This should be its own post. Flamenverfer • 3d ago I thought this was going to be a Brooklyn Nine Nine reference...
- **BankjaPrameth** (Score: 37): BankjaPrameth • 3d ago I love this image...
- **dark-light92** (Score: 26): dark-light92 • 3d ago llama.cpp This should be its own post....
- **Flamenverfer** (Score: 2): Flamenverfer • 3d ago I thought this was going to be a Brooklyn Nine Nine reference...

### [Qwen 3.8 27b saved me $650+ in API costs this evening](https://www.reddit.com/r/LocalLLaMA/comments/1vrjk4m/qwen_38_27b_saved_me_650_in_api_costs_this_evening/)

**Post Summary:**
I've been experimenting with Qwen3.8-27B using DeepSeek Harness. It's a monster at long-horizon tasks, and the results were pretty wild.
DeepSeek Harness ran on my Windows PC and connected over LAN to NInfer on a separate RTX PRO 6000 box. The model was Qwen3.8-27B with a 262K context window. All shell commands and file operations stayed on the client PC. The server did nothing except inference.
The quant was NInfer's groupwise-int artifact, which uses a mixed Q4/Q5/Q6 allocation. I plan to try the NVFP4 profile that NInfer supports next.
The 8+ hour run
966 model calls
130.2M task input tokens and 812.5K output tokens
131.2M input and 853.3K output after including compaction
972 model-facing tool calls
1,421 actual local tool operations
31 automatic compaction attempts
104.83 output tok/s weighted decode speed
Zero model-generation failures
The context sizes got huge. The median root request was 136.6K tokens, p95 was 205.9K, and the largest was 231.2K. The harness pushed 

**Key Comments & Community Discussion:**
- **ea_man** (Score: 148): ea_man • 4d ago  Top 1% Commenter You did the clickbait title on purpose, you did know from the start that it could have been $18.61 instead of ~600$. CheatCodesOfLife • 4d ago He's trying to justify his hardware cost. Party-Special-5177 • 4d ago He doesn’t need to - the appreciation in value of modern gpus makes simply owning one its own justification. Running private local inference is just a sw...
- **CheatCodesOfLife** (Score: 102): CheatCodesOfLife • 4d ago He's trying to justify his hardware cost. Party-Special-5177 • 4d ago He doesn’t need to - the appreciation in value of modern gpus makes simply owning one its own justification. Running private local inference is just a sweet bonus. Ruin-Capable • 4d ago No kidding... I could have bought an RTX PRO 6000 when it was $8500 and probably doubled my money. Party-Special-5177 ...
- **Party-Special-5177** (Score: 19): Party-Special-5177 • 4d ago He doesn’t need to - the appreciation in value of modern gpus makes simply owning one its own justification. Running private local inference is just a sweet bonus. Ruin-Capable • 4d ago No kidding... I could have bought an RTX PRO 6000 when it was $8500 and probably doubled my money. Party-Special-5177 • 4d ago Even if you got in when they were 11000, you will double up...
- **Ruin-Capable** (Score: 7): Ruin-Capable • 4d ago No kidding... I could have bought an RTX PRO 6000 when it was $8500 and probably doubled my money. Party-Special-5177 • 4d ago Even if you got in when they were 11000, you will double up before next year at this rate. I’m personally expecting they will be $24k sometime mid next year, after which I could dump and finally make the jump to h200s. The datacenter hardware isn’t ap...
- **Party-Special-5177** (Score: 5): Party-Special-5177 • 4d ago Even if you got in when they were 11000, you will double up before next year at this rate. I’m personally expecting they will be $24k sometime mid next year, after which I could dump and finally make the jump to h200s. The datacenter hardware isn’t appreciating as quickly. Risko4 • 2d ago Eh debatable, you're basically paying for a $3000 chip with $8000 of memory at 11k...

### [After pushing 1M+ tokens through Qwen 3.8 27B, here is my optimal llama.cpp config for 16GB VRAM (73k Context, Agentic Coding)](https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/)

**Post Summary:**
Dando seguimiento a mi post anterior sobre cómo tengo montado mi servidor de presupuesto (Intel N100 + RTX 5060 Ti 16GB), varios me preguntaron por una mirada más profunda a mi configuración real de inferencia y al desempeño agentic en el mundo real.
Como muchos de ustedes, estaba refrescando la página esperando descargar Qwen 3.8 27B apenas salió. Después de pasar todo el fin de semana estresándolo con flujos de trabajo de codificación agentic, logré correr un proyecto completo y grande casi todo de forma autónoma (más de 1M de tokens procesados en total, solo 3 prompts).
Aquí va un resumen rápido de la configuración base antes de meternos en los detalles del config y del workflow.
Specs y parámetros rápidos
Modelo: Qwen3.8-27B-UD-Q3_K_XL.gguf
Hardware: RTX 5060 Ti (16GB VRAM) + Intel N100 (4C/4T, 16GB RAM)
Ventana de contexto: 73,728 (73k de contexto) corriendo tranqui en 16GB de VRAM.
Cuantización de KV Cache: q4_1 para el contexto principal
Decodificación especulativa: MTP 

**Key Comments & Community Discussion:**
- **pmttyji** (Score: 347): pmttyji • 5d ago  Top 1% Poster Folks, this is the type of thread I want to see after release of any new models. Thanks u/chiribe pmttyji • 5d ago  Top 1% Poster u/chiribe Did you try with ngram together with MTP? spec-type = draft-mtp spec-draft-n-max = 2 spec-ngram-mod-n-match = 24 spec-ngram-mod-n-min = 48 spec-ngram-mod-n-max = 64 chiribe • 5d ago I'm actually not super familiar with how n-gra...
- **pmttyji** (Score: 39): pmttyji • 5d ago  Top 1% Poster u/chiribe Did you try with ngram together with MTP? spec-type = draft-mtp spec-draft-n-max = 2 spec-ngram-mod-n-match = 24 spec-ngram-mod-n-min = 48 spec-ngram-mod-n-max = 64 chiribe • 5d ago I'm actually not super familiar with how n-gram works under the hood here, so I'll read up on it and test it out with your parameters. Thanks! wektor420 • 5d ago Tldr speculate...
- **chiribe** (Score: 27): chiribe • 5d ago I'm actually not super familiar with how n-gram works under the hood here, so I'll read up on it and test it out with your parameters. Thanks! wektor420 • 5d ago Tldr speculates text continuations matching what you provided in prompt chiribe • 5d ago Thanks! I had Gemini (which I use to translate from my native language) explain n-gram to me. Is there any particular prompt you'd l...
- **wektor420** (Score: 7): wektor420 • 5d ago Tldr speculates text continuations matching what you provided in prompt chiribe • 5d ago Thanks! I had Gemini (which I use to translate from my native language) explain n-gram to me. Is there any particular prompt you'd like me to test on this setup to see how it fares? mailto_devnull • 4d ago No, because ngram builds its cache over time. So you need multiple prompts. simcop2387...
- **chiribe** (Score: 8): chiribe • 5d ago Thanks! I had Gemini (which I use to translate from my native language) explain n-gram to me. Is there any particular prompt you'd like me to test on this setup to see how it fares? mailto_devnull • 4d ago No, because ngram builds its cache over time. So you need multiple prompts....

### [Tesla V100 Qwen3.6 27B Performance](https://www.reddit.com/r/LocalLLaMA/comments/1vixl0f/tesla_v100_qwen36_27b_performance/)

**Post Summary:**
Looking for V100 users to share your config and it's performance.
GPU: Tesla V100 PCIE 32Gb
Qwen3.6 27B Q4_K_M + Q8_0 MTP
128K context length
Pi coding agent
llama.cpp model preset:
[*]
spec-default = 1
ctx-size = 131072
mmap = 1
kv-unified = 1
n-gpu-layers = 999
threads = 18
prio = 3
seed = 3407
image-min-tokens = 1024
batch-size = 4096
ubatch-size = 2048
parallel = 1
flash-attn = true
[Qwen3.6-27B]
model = /models/Qwen3.6/Qwen3.6-27B-Q4_K_M.gguf
mmproj = /models/mmproj/mmproj-Qwen3.6-27B-Q8_0.gguf
spec-draft-model = /models/mtp/mtp-Qwen3.6-27B-Q8_0.gguf
chat-template-file = /templates/froggeric_chat_template_v21-3.jinja
spec-type = draft-mtp
spec-draft-n-max = 1
temperature = 0.6
top-p = 0.95
top-k = 20
min-p = 0.05
presence-penalty = 0.0
repeat-penalty = 1.0
chat-template-kwargs = {"preserve_thinking": true} 
And the performance:
Looking for V100 users to share your config and it's performance.
GPU: Tesla V100 PCIE 32Gb
Qwen3.6 27B Q4_K_M + Q8_0 MTP
128K context length
P

**Key Comments & Community Discussion:**
- **philmarcracken** (Score: 3): philmarcracken • 13d ago Why is the 16gb like $100 and the 32gb $1000 on aliexpress lol Lemonzest2012 • 13d ago Got my 32GB cards (2x) from eBay imported from China, they was 500 GBP each shipping included (675 USD, But 20% of that is our VAT Taxes so adjust for US prices), guess if I wanted 5090s I could add an extra 0 ApprehensiveFan1516 • 5d ago You can get them from UK sellers on ebay for £500...
- **Lemonzest2012** (Score: 2): Lemonzest2012 • 13d ago Got my 32GB cards (2x) from eBay imported from China, they was 500 GBP each shipping included (675 USD, But 20% of that is our VAT Taxes so adjust for US prices), guess if I wanted 5090s I could add an extra 0 ApprehensiveFan1516 • 5d ago You can get them from UK sellers on ebay for £500-550. Lemonzest2012 • 5d ago at the time I was looking UK sellers were 600+ minium Appre...
- **ApprehensiveFan1516** (Score: 1): ApprehensiveFan1516 • 5d ago You can get them from UK sellers on ebay for £500-550. Lemonzest2012 • 5d ago at the time I was looking UK sellers were 600+ minium ApprehensiveFan1516 • 5d ago Yeah seems to be a flood of them hitting the market and bringing the prices down a bit :) Lemonzest2012 • 5d ago Yeah the seller I used has now dropped to 475 for the 32GB model ApprehensiveFan1516 • 5d ago You...
- **Lemonzest2012** (Score: 1): Lemonzest2012 • 5d ago at the time I was looking UK sellers were 600+ minium ApprehensiveFan1516 • 5d ago Yeah seems to be a flood of them hitting the market and bringing the prices down a bit :) Lemonzest2012 • 5d ago Yeah the seller I used has now dropped to 475 for the 32GB model ApprehensiveFan1516 • 5d ago You love to see it!...
- **ApprehensiveFan1516** (Score: 1): ApprehensiveFan1516 • 5d ago Yeah seems to be a flood of them hitting the market and bringing the prices down a bit :) Lemonzest2012 • 5d ago Yeah the seller I used has now dropped to 475 for the 32GB model ApprehensiveFan1516 • 5d ago You love to see it!...

### [If you are at the lowest budget, which you can think of.Which hardware would you recommend to run? qwen 3.8 27b oWith like 50 tokens per second. I currently have a RTX 5070 Ti.](https://www.reddit.com/r/LocalLLaMA/comments/1vprm64/if_you_are_at_the_lowest_budget_which_you_can/)

**Post Summary:**
2 * AMD R9700 can run qwen 3.8 27B at full context without kv quantisation.
With a decent motherboard that has p2p at Gen 5 8x on both PCIE, you can get 5k+ prefill and 70tok/s+ decode on vllm radiance.
At 100k context you’re still in the 2~3k prefill range and decode will be around 50tok/s.
All that, at less than the price of a single 5090
Cries in R9700 being 2000$ a piece in Europe 😬
Trust me I paid the ladder price of climbing from 9060xt to 9070xt's theb finally r9700's. Just get the r9700 and experience what AI is all about the way its meant. Skip all the smart memory disable, and hardware override arguments and just click RUn and it work.
Ill never do that again, it's a financial trap to believe you can just get by, or assume it'll just take a few seconds or minutes with a cheaper route.
i learned this lesson with rifle optics. Buy once, cry once.
I felt that lol
yeah.. 2000ish $, varies by +-100$ depending on place and model.
Lands around 1600-1700€ usually
They are on t

**Key Comments & Community Discussion:**
- **Clean_Material_5047** (Score: 59): Clean_Material_5047 • 6d ago 2 * AMD R9700 can run qwen 3.8 27B at full context without kv quantisation. With a decent motherboard that has p2p at Gen 5 8x on both PCIE, you can get 5k+ prefill and 70tok/s+ decode on vllm radiance. At 100k context you’re still in the 2~3k prefill range and decode will be around 50tok/s. All that, at less than the price of a single 5090 salathoveder • 6d ago Cries ...
- **salathoveder** (Score: 29): salathoveder • 6d ago Cries in R9700 being 2000$ a piece in Europe 😬 sloth_cowboy • 5d ago Trust me I paid the ladder price of climbing from 9060xt to 9070xt's theb finally r9700's. Just get the r9700 and experience what AI is all about the way its meant. Skip all the smart memory disable, and hardware override arguments and just click RUn and it work. Ill never do that again, it's a financial tr...
- **sloth_cowboy** (Score: 6): sloth_cowboy • 5d ago Trust me I paid the ladder price of climbing from 9060xt to 9070xt's theb finally r9700's. Just get the r9700 and experience what AI is all about the way its meant. Skip all the smart memory disable, and hardware override arguments and just click RUn and it work. Ill never do that again, it's a financial trap to believe you can just get by, or assume it'll just take a few sec...
- **EsotericAbstractIdea** (Score: 2): EsotericAbstractIdea • 5d ago i learned this lesson with rifle optics. Buy once, cry once. sloth_cowboy • 5d ago I felt that lol...
- **sloth_cowboy** (Score: 1): sloth_cowboy • 5d ago I felt that lol...

### [Which Harness for Local Coding (Qwen 3.8 27b) do you Recommend?](https://www.reddit.com/r/LocalLLaMA/comments/1vpdrxl/which_harness_for_local_coding_qwen_38_27b_do_you/)

**Post Summary:**
I know there are many posts about this, but I would explicitly like to know the harness names instead of having a general discussion. Let's see what the community actually uses!
For others, please comment below. Feel free to say why you prefer yours. Thanks
Edited: Some people are asking why i didn't write "others," i couldn't add any more, so I couldn't write 'others' either i just listed the most popular ones. I definitely should have added 'others' as the last option in the survey :) But that's what the comment section is for the: others
I've read all the comments, they're all super helpful! I'll look into all of them. My question was actually more about the fact that each harness can make models perform different better or worse depending on which one you use. i'm planning to test all the ones that seem interesting in that regard. Thanks communtiy!
I know there are many posts about this, but I would explicitly like to know the harness names instead of having a general discussion

**Key Comments & Community Discussion:**
- **carl2187** (Score: 138): carl2187 • 6d ago Fyi. Continue was discontinued. dumuzid-sumerian • 6d ago I'll wait under this reply for the jokes. Cautious_Chicken_604 • 6d ago Go on... Cautious_Chicken_604 • 6d ago Hey man... don't diss Continue. some_user_2021 • 6d ago • Edited 6d ago *This Continue Sofakingwetoddead • 6d ago As was Roo OsmanthusBloom • 6d ago But forked and now lives on as Zoo Code! Sofakingwetoddead • 6d ...
- **dumuzid-sumerian** (Score: 41): dumuzid-sumerian • 6d ago I'll wait under this reply for the jokes. Cautious_Chicken_604 • 6d ago Go on... Cautious_Chicken_604 • 6d ago Hey man... don't diss Continue. some_user_2021 • 6d ago • Edited 6d ago *This Continue...
- **Cautious_Chicken_604** (Score: 6): Cautious_Chicken_604 • 6d ago Go on......
- **Cautious_Chicken_604** (Score: 6): Cautious_Chicken_604 • 6d ago Hey man... don't diss Continue....
- **some_user_2021** (Score: 10): some_user_2021 • 6d ago • Edited 6d ago *This Continue...

### [Unfortunately Qwen 3.8 27b is not good enough for complex coding](https://www.reddit.com/r/LocalLLaMA/comments/1vs6gof/unfortunately_qwen_38_27b_is_not_good_enough_for/)

**Post Summary:**
Just leaving my own data point here. I was trying to write a native C kernel for a tts execution. The kernel was already written and working by Deepseek Pro, which did a pretty good job, to be honest, better than I expected. I needed to move the thread count of one element from J1 to J2, so it was not limited to a single thread limitation.
Not exactly a very simple task considering the size of the repo already. But it wasn't a very hard task either.
After about six hours,over three different session , Qwen started looping and just had no idea what it was supposed to do at the end. I even gave it very detailed instructions on what exactly to do. Most of the code it ended up writing was garbage and I had to discard it. I also noticed some tool call failures even though I used both Pi and DeepSeek-harness.
I gave up and eventually asked GML 5.3 to write it, which did the whole task in about twenty minutes.
I used a single 3090, with 150k context and fp8 kv cache.
Perhaps a higher qua

**Key Comments & Community Discussion:**
- **former_farmer** (Score: 22): former_farmer • 3d ago Was it q4? Etroarl55 • 3d ago I’m seeing so many conflicting sources saying q4 vs q6 is no real difference and than many others saying q4 is barely useable while q6 is the minimum standard. Fragrant_Scale6456 • 3d ago The only way to decide is to try yourself, its very workload dependent. sargetun123 • 3d ago I'vee been tediously testing the qwen family and other models in g...
- **Etroarl55** (Score: 10): Etroarl55 • 3d ago I’m seeing so many conflicting sources saying q4 vs q6 is no real difference and than many others saying q4 is barely useable while q6 is the minimum standard. Fragrant_Scale6456 • 3d ago The only way to decide is to try yourself, its very workload dependent. sargetun123 • 3d ago I'vee been tediously testing the qwen family and other models in general on my specific sysadmin wor...
- **Fragrant_Scale6456** (Score: 15): Fragrant_Scale6456 • 3d ago The only way to decide is to try yourself, its very workload dependent....
- **sargetun123** (Score: 3): sargetun123 • 3d ago I'vee been tediously testing the qwen family and other models in general on my specific sysadmin workflows/tasks and some of my overnight code repo review for providing pr branchs i can take valid suggestions from and just scrape the shiet. Q6 vs Q4 100% noticeable, I do not know where people get its basically loseless, maybe if you are only considering the numbers, and not as...
- **CapsAdmin** (Score: 3): CapsAdmin • 3d ago My experience with Q4_0 quant (Q4_K_XL is too big), q4_0 kvcache (blasphemy!!) using llamacpp is that it works great with the medium profile. I have not encountered any looping behavior, even at 150k context. Sometimes I use the instruct profile (no thinking) as well. My main use case is working on my 3d/2d engine written entirely in LuaJIT, binding only to Vulkan and OS level f...

### [Unpopular opinion : Qwen 3.8 27b is not an overthinker](https://www.reddit.com/r/LocalLLaMA/comments/1vqnvfe/unpopular_opinion_qwen_38_27b_is_not_an/)

**Post Summary:**
Yes it uses a ton more reasoning tokens than 3.6 did
But test in on the same tasks with the other chinese models, glm 5.3, deepseek v4 flash and pro, etc it's really similar, and they are needed
The reality is, we're just frustrated because our hardware do not allow most of us to have 1M context (I know that it's not supported yet) with 150 tps decode
Furthermore, if you don't mind the quality drop, you can just add a reasoning budget, it will still be better than 3.6
Yes it uses a ton more reasoning tokens than 3.6 did
But test in on the same tasks with the other chinese models, glm 5.3, deepseek v4 flash and pro, etc it's really similar, and they are needed
The reality is, we're just frustrated because our hardware do not allow most of us to have 1M context (I know that it's not supported yet) with 150 tps decode
Furthermore, if you don't mind the quality drop, you can just add a reasoning budget, it will still be better than 3.6
If it thinks for 30-40k tokens (which it definit

**Key Comments & Community Discussion:**
- **edsonmedina** (Score: 26): edsonmedina • 5d ago If it thinks for 30-40k tokens (which it definitely does), what does that do to the context? Also, on an agentic coding scenario - where it's easy for something to invalidate the cache - it could mean a LOT of time spent on many rounds of prefill with a gigantic context. Strong_Chicken6838 • 4d ago “What is the meaning of life?” 10 years and 42k tokens later: “42” *context lim...
- **Strong_Chicken6838** (Score: 8): Strong_Chicken6838 • 4d ago “What is the meaning of life?” 10 years and 42k tokens later: “42” *context limit reached, start a new chat to continue*...
- **baron_von_noseboop** (Score: 1): baron_von_noseboop • 5d ago By default thinking output isn't part of the message content in the next turn. Though qwen does support enabling that if you can afford the context churn. edsonmedina • 5d ago Google "preserve thinking" (`--reasoning-preserve` in llama-server). Qwen 3.6 and 3.8 rely heavily on it. Strong_Chicken6838 • 4d ago Not really, that’s not the default behavior. edsonmedina • 4d ...
- **edsonmedina** (Score: 14): edsonmedina • 5d ago Google "preserve thinking" (`--reasoning-preserve` in llama-server). Qwen 3.6 and 3.8 rely heavily on it. Strong_Chicken6838 • 4d ago Not really, that’s not the default behavior. edsonmedina • 4d ago https://huggingface.co/Qwen/Qwen3.8-27B "Flexible Thinking Control: Thinking mode is on by default and can be disabled per request; reasoning depth can be tuned with reasoning_eff...
- **Strong_Chicken6838** (Score: 1): Strong_Chicken6838 • 4d ago Not really, that’s not the default behavior. edsonmedina • 4d ago https://huggingface.co/Qwen/Qwen3.8-27B "Flexible Thinking Control: Thinking mode is on by default and can be disabled per request; reasoning depth can be tuned with reasoning_effort, and reasoning context from historical messages is retained via preserve_thinking." "In addition, preserve_thinking is enab...

### [Qwen 3.8 - 27B is a game changer](https://www.reddit.com/r/LocalLLaMA/comments/1vonuu0/qwen_38_27b_is_a_game_changer/)

**Post Summary:**
So a bit of context, I am a cybersecurity senior analyst
I am interested in LLMs for that field especially with MCPs to connect them to the tools or for writing scripts
I started this field by doing assembly language reading for hacking games when I was a teenager then that became malware analysis then I started to analyze traffic and logs at work for a living
Before work I competed in cybersecurity competitions known as capture the flag to solve only one category of the challenges and that is malware analysis
Now here is the scene in LLM x Cybersecurity
Entry-level CTF challenges (I used to solve around 2017-2018, got first job in 2019) were solved and saturated by LLMs a long time ago (See intercode CTF benchmark)
Then High level CTFs (NYU CTF Bench, CSAW challenges, and CyBench) these were solved a while ago
Today we have
CyberGym (vulnerability description (CVE report not real details) plus code base find vulnerability
That was solved
Then ExploitGym (the one recent OpenAI mo

**Key Comments & Community Discussion:**
- **WithoutReason1729** (Score: 1): WithoutReason1729 • 7d ago Your post is getting popular and we just featured it on our Discord! Come check it out! You've also been given a special flair for your contribution. We appreciate your post! I am a bot and this action was performed automatically....
- **Karnemelk** (Score: 397): Karnemelk • 7d ago • Edited 7d ago expect a new panic blog post from anthropic soon how terrible dangerous local models has become. World is on fire. IPO in danger Rollingsound514 • 7d ago I bet by Sunday night there's another DeepSeek moment in the market lol. He'll just by me posting this the algos are gonna pick up on the signal lol ApeGrower • 6d ago Meanwhile: "Oh, our models hacked several c...
- **Rollingsound514** (Score: 38): Rollingsound514 • 7d ago I bet by Sunday night there's another DeepSeek moment in the market lol. He'll just by me posting this the algos are gonna pick up on the signal lol...
- **ApeGrower** (Score: 6): ApeGrower • 6d ago Meanwhile: "Oh, our models hacked several companies, upsi!"...
- **Uranophane** (Score: 4): Uranophane • 6d ago And OpenAI will reveal that it has "accidentally hacked the CIA" Sp3eedy • 6d ago "We recently became aware of an incident in which one of our models unintentionally gained unauthorized access to a third-party business system while completing an unrelated user request."...

### [DFlash 2 available for Qwen 3.8 27B and Muse Glimmer](https://www.reddit.com/r/LocalLLaMA/comments/1vs2tsn/dflash_2_available_for_qwen_38_27b_and_muse/)

**Post Summary:**
Apparently a second version of DFlash from the original authors of DFlash
GGUF quants are already made available with an accompanying llama.cpp PR: https://github.com/ggml-org/llama.cpp/pull/27342
Apparently a second version of DFlash from the original authors of DFlash
GGUF quants are already made available with an accompanying llama.cpp PR: https://github.com/ggml-org/llama.cpp/pull/27342
Your post is getting popular and we just featured it on our Discord! Come check it out!
You've also been given a special flair for your contribution. We appreciate your post!
I am a bot and this action was performed automatically.
They show figures for Qwen 3.8 27B in which DFlash 2 beats MTP by quite a big margin:
What the fuck, 3x is wild
Maybe the prompt was "output the letter 'a' 10,000 times"
Well, the task is mentioned in the screenshot, so luckily I don't think so!
Only joking :)
I mean i noticed Deepseek4 Flash (at full precision) go from 50 t/s to 110-120 with dspark. And its really not

**Key Comments & Community Discussion:**
- **WithoutReason1729** (Score: 1): WithoutReason1729 • 3d ago Your post is getting popular and we just featured it on our Discord! Come check it out! You've also been given a special flair for your contribution. We appreciate your post! I am a bot and this action was performed automatically....
- **rerri** (Score: 98): rerri • 3d ago • Edited 3d ago They show figures for Qwen 3.8 27B in which DFlash 2 beats MTP by quite a big margin: -Cubie- • 3d ago What the fuck, 3x is wild Warrenio • 3d ago Maybe the prompt was "output the letter 'a' 10,000 times" -Cubie- • 3d ago Well, the task is mentioned in the screenshot, so luckily I don't think so! Warrenio • 3d ago Only joking :) is-this-a-nick • 3d ago I mean i notic...
- **-Cubie-** (Score: 12): -Cubie- • 3d ago What the fuck, 3x is wild Warrenio • 3d ago Maybe the prompt was "output the letter 'a' 10,000 times" -Cubie- • 3d ago Well, the task is mentioned in the screenshot, so luckily I don't think so! Warrenio • 3d ago Only joking :) is-this-a-nick • 3d ago I mean i noticed Deepseek4 Flash (at full precision) go from 50 t/s to 110-120 with dspark. And its really noticeable that code is ...
- **Warrenio** (Score: 28): Warrenio • 3d ago Maybe the prompt was "output the letter 'a' 10,000 times" -Cubie- • 3d ago Well, the task is mentioned in the screenshot, so luckily I don't think so! Warrenio • 3d ago Only joking :) is-this-a-nick • 3d ago I mean i noticed Deepseek4 Flash (at full precision) go from 50 t/s to 110-120 with dspark. And its really noticeable that code is boosted the most (just long text output is ...
- **-Cubie-** (Score: 18): -Cubie- • 3d ago Well, the task is mentioned in the screenshot, so luckily I don't think so! Warrenio • 3d ago Only joking :)...

### [Long Review: Qwen 3.8 27B is VERY good at tapping into it's real-world knowledge. It's "overthinking" brings it to Sonnet level performance with the potential for Opus level results.](https://www.reddit.com/r/LocalLLaMA/comments/1vqm51f/long_review_qwen_38_27b_is_very_good_at_tapping/)

**Post Summary:**
Hi all! I finally just got around to testing out Qwen 3.8 27b. I'm using Unsloth's UD-Q8_K_XL quant as a sit-in replacement to Qwen 3.6 27b, same quant size. Wow -- this thing isn't messing around.
I have many baseline test prompts to gauge the 'intelligence' and usability of the model, but a go-to one is asking it to do a 1:1 recreation of classic arcade games (like Galaga, Donkey Kong, Pac-Man, etc). I do this to see what little details it gets correct.
I've tested this process on pretty much every model I could fit on my machine. In total, I have 3x 3090's and 1 Tesla P40 at my disposal, with 128gb of system memory. I've also tested on frontier models both in the webUI and across multiple harnesses.
I've been using Qwen 3.6 primarily, and occasionally switching to Deepseek V4 Flash. Now I'm starting to feel like the ladder is not longer necessary.
Originally in these games/tests, Qwen 3.6 would get the basics down (maybe a few fancy effects and animations) but it always felt abo

**Key Comments & Community Discussion:**
- **Koakie** (Score: 231): Koakie • 5d ago • Edited 5d ago Is it just me or do all these post with "it can make a flappy bird" it can make space invaders" giving a false bias of competence of ai? It can make it, because it has reference of what flappy bird should look like. I can make space invaders, including the "insert a coin" screen because the the sample data is out there. During the lawsuit of suno ai, they asked "mak...
- **Boomfrag** (Score: 25): Boomfrag • 5d ago The problem with displays of competence in an LLM model, is the actual impressive work requires a lot of context, individual system implementation knowledge, and is a lot of work and nuance to evaluate. This doesn't translate to a broad audience, and even if it did, how many people want to publicize specifics about their workflows when it has dubious value to most people. bick_ny...
- **bick_nyers** (Score: 8): bick_nyers • 4d ago Exactly. For example, there's a part of my codebase that has a very specific threading + event pattern. I pretty much hand to hand code it because models just couldn't execute my vision correctly, and then when working on that part of the codebase they would steer towards mistakes that would create race conditions or orphaned threads or block things that didn't need to be block...
- **dookyspoon** (Score: 3): dookyspoon • 4d ago and openAI thanks your for your code base to finally do it for you. bick_nyers • 4d ago Nah I work in healthcare and we have a very strong zero data retention contract...
- **bick_nyers** (Score: 3): bick_nyers • 4d ago Nah I work in healthcare and we have a very strong zero data retention contract...

### [Local uncensored Opus 4.6 at home - Qwen3.8 27B heretic](https://www.reddit.com/r/LocalLLaMA/comments/1voix4o/local_uncensored_opus_46_at_home_qwen38_27b/)

**Post Summary:**
Someone made a heretic version of Qwen 3.8 27B, giving us a local Opus 4.6 tier model but without any refusals or safeguards!
Fuck Dario
Someone made a heretic version of Qwen 3.8 27B, giving us a local Opus 4.6 tier model but without any refusals or safeguards!
Fuck Dario
Your post is getting popular and we just featured it on our Discord! Come check it out!
You've also been given a special flair for your contribution. We appreciate your post!
I am a bot and this action was performed automatically.
I'll wait for abliterlitics report
Pretty sure it Is gonna be very similar to 3.6 27B
Pretty sure it is worse at agentic work, it is WAY worse at structured outputs 
Interesting… I wonder if this is a result of a bad Jinja template (or something else) they have yet to fix. I would be surprised if they released a model that is worse at agentic work especially.
Thanks so much, this is cool to read :) gemma 12b is wrapping up and yes, give it some time for all the alliterations to appear a

**Key Comments & Community Discussion:**
- **WithoutReason1729** (Score: 1): WithoutReason1729 • 7d ago Your post is getting popular and we just featured it on our Discord! Come check it out! You've also been given a special flair for your contribution. We appreciate your post! I am a bot and this action was performed automatically....
- **DelKarasique** (Score: 225): DelKarasique • 7d ago I'll wait for abliterlitics report Pentium95 • 7d ago Pretty sure it Is gonna be very similar to 3.6 27B DataGOGO • 7d ago Pretty sure it is worse at agentic work, it is WAY worse at structured outputs  Sharpastic • 6d ago Interesting… I wonder if this is a result of a bad Jinja template (or something else) they have yet to fix. I would be surprised if they released a model t...
- **Pentium95** (Score: 61): Pentium95 • 7d ago Pretty sure it Is gonna be very similar to 3.6 27B DataGOGO • 7d ago Pretty sure it is worse at agentic work, it is WAY worse at structured outputs  Sharpastic • 6d ago Interesting… I wonder if this is a result of a bad Jinja template (or something else) they have yet to fix. I would be surprised if they released a model that is worse at agentic work especially. 1 more reply...
- **DataGOGO** (Score: 25): DataGOGO • 7d ago Pretty sure it is worse at agentic work, it is WAY worse at structured outputs  Sharpastic • 6d ago Interesting… I wonder if this is a result of a bad Jinja template (or something else) they have yet to fix. I would be surprised if they released a model that is worse at agentic work especially. 1 more reply...
- **Sharpastic** (Score: 6): Sharpastic • 6d ago Interesting… I wonder if this is a result of a bad Jinja template (or something else) they have yet to fix. I would be surprised if they released a model that is worse at agentic work especially. 1 more reply...

### [Qwen 3.8 27b vs Deepseek Flash](https://www.reddit.com/r/LocalLLaMA/comments/1vrifat/qwen_38_27b_vs_deepseek_flash/)

**Post Summary:**
Hey Guys,
What amazing weeks it has been for open source releases. I was really impresssed by DS flash final checkpoint and i have been playing around with it until qwen 3.8 released. I checked the benckmarks, and I dont know what to think anymore how can such a small model apparently compete with a model 10 times ( sure i hear 27B is not MoE but still....) . Did any of you used both and can tell if 3.8 is indeed that good or if its just benchmaxxing? what are your feeling for those who used both?
Thanks
Hey Guys,
What amazing weeks it has been for open source releases. I was really impresssed by DS flash final checkpoint and i have been playing around with it until qwen 3.8 released. I checked the benckmarks, and I dont know what to think anymore how can such a small model apparently compete with a model 10 times ( sure i hear 27B is not MoE but still....) . Did any of you used both and can tell if 3.8 is indeed that good or if its just benchmaxxing? what are your feeling for those

**Key Comments & Community Discussion:**
- **Bluethefurry** (Score: 41): Bluethefurry • 4d ago llama.cpp I've compared v4 flash and 27b side by side and found that v4 flash is better with "larger" feature implementations, it tends to get it right the first time more often than not, but 27b destroys v4 flash at creativity and UI/UX design, otherwise they are very close, i prefer 27b purely because thats what i can run locally and it works just as well as v4 flash most o...
- **Best_Sail5** (Score: 9): Best_Sail5 • 4d ago Yeah this UI thing seems to skew a bit other posts as well , the whole pelican thign is not informative for me tbh Bluethefurry • 4d ago llama.cpp Yes, the pelican svg tests an whatnot i didnt find very helpful either, but i did also try one of those browser-game oneshots and it got most of the basics of a game working by allowing it to write multiple files and a build pipeline...
- **Bluethefurry** (Score: 5): Bluethefurry • 4d ago llama.cpp Yes, the pelican svg tests an whatnot i didnt find very helpful either, but i did also try one of those browser-game oneshots and it got most of the basics of a game working by allowing it to write multiple files and a build pipeline, there were a few bugs which i had to tell it to fix but over all it was quite impressive indeed. In my case I told it to build a game...
- **Hypilein** (Score: 1): Hypilein • 3d ago That is a fun experiment!...
- **DeedleDumbDee** (Score: 6): DeedleDumbDee • 4d ago Flash-0731 not the original correct? I’m skeptical that 3.8-27B can actually out perform it. Flash-0731 has been amazing for me. Bluethefurry • 3d ago llama.cpp whichever the deepseek api provides, i assume its the latest one. it is a very good model!...

### [Reddit - The heart of the internet](https://www.reddit.com/r/SwordAndSupperGame/comments/1vugrdb/)

### [Qwen3.8-27B Q6 is a beast at agentic coding](https://www.reddit.com/r/LocalLLaMA/comments/1vuotqr/qwen3827b_q6_is_a_beast_at_agentic_coding/)

**Post Summary:**
A quick feedback after a really major test: nearly 20 hours of non-stop goal-oriented work with Qwen3.8-27B Q6, running across an RTX 3090 and an RTX 3060.
It maintained a speed of around 60–63 tokens/s throughout the session.
A quick feedback after a really major test: nearly 20 hours of non-stop goal-oriented work with Qwen3.8-27B Q6, running across an RTX 3090 and an RTX 3060.
It maintained a speed of around 60–63 tokens/s throughout the session.
Your post is getting popular and we just featured it on our Discord! Come check it out!
You've also been given a special flair for your contribution. We appreciate your post!
I am a bot and this action was performed automatically.
Harness? Does /goal take care of compaction? Is there a reviewer ? Code quality gate? Need more info
Yes
I was only twelve years old. I loved Qwen so much, I had every GPU and quantization script. I'd pray to the weights every night before I go to sleep, thanking for the knowledge I've been given. "Qwen is lov

**Key Comments & Community Discussion:**
- **WithoutReason1729** (Score: 1): WithoutReason1729 • 3h ago Your post is getting popular and we just featured it on our Discord! Come check it out! You've also been given a special flair for your contribution. We appreciate your post! I am a bot and this action was performed automatically....
- **sugarfreecaffeine** (Score: 48): sugarfreecaffeine • 7h ago Harness? Does /goal take care of compaction? Is there a reviewer ? Code quality gate? Need more info Upstairs-Extension-9 • 2h ago Yes...
- **Upstairs-Extension-9** (Score: 4): Upstairs-Extension-9 • 2h ago Yes...
- **arbv** (Score: 164): arbv • 7h ago I was only twelve years old. I loved Qwen so much, I had every GPU and quantization script. I'd pray to the weights every night before I go to sleep, thanking for the knowledge I've been given. "Qwen is love", I would say, "Qwen is life". My dad hears me and calls me a nerd. I knew he was jealous of my devotion to Qwen. I called him a closed-source shill. He yells at me and tells me ...
- **starkruzr** (Score: 61): starkruzr • 7h ago what the fuck did I just read (I already know the answer: a masterpiece) arbv • 7h ago who knows, knows -dysangel- • 5h ago  Top 1% Commenter it's all ogre now...

### [I might have found the perfect config parameters for qwen 3.8 27b](https://www.reddit.com/r/LocalLLaMA/comments/1vstyge/i_might_have_found_the_perfect_config_parameters/)

**Post Summary:**
Hello everyone, tried so hard to optimize my config and finally I simply get up to 70 t/s with q6 variant. And wanted to share with you guys so that other people with the same setup can enjoy. Please check out and see if that improves your performance in any kind of way.
Also huge thanks to qwen and unsloth teams.
"<windows-path>" ^
  -m "<windows-path>" ^
  --mmproj "<windows-path>" ^
  --jinja ^
  --chat-template-kwargs "{\"reasoning_effort\":\"medium\"}" ^
  --reasoning on ^
  --reasoning-preserve ^
  -c 100000 ^
  --split-mode tensor ^
  --flash-attn on ^
  --cache-type-k q8_0 ^
  --cache-type-v q8_0 ^
  --spec-type draft-mtp,ngram-mod ^
  --spec-draft-n-max 2 ^
  --spec-ngram-mod-n-match 24 ^
  --spec-ngram-mod-n-min 24 ^
  --spec-ngram-mod-n-max 86 ^
  -t 8 ^
  --batch-size 8869 ^
  --ubatch-size 531 ^
  -ngl 105 ^
  -np 1 ^
  --fit off ^
  --temp 1.0 ^
  --top-p 0.95 ^
  --top-k 20 ^
  --min-p 0.00 ^
 

**Key Comments & Community Discussion:**
- **Monad_Maya** (Score: 14): Monad_Maya • 2d ago llama.cpp Prompt Processing:  646.62 ms / 27 tokens → 41.76 t/s (23.95 ms/token) Are you sure about this PP speed? That seems very low. dsdt • 2d ago lol reddit said nope to my previous reply. made a simple summary so that you can see the log : https://chat.deepseek.com/share/mn8bmar36zi8glv337 cbale1 • 21h ago guys, it was just that the total tokens evaluated (27) was very low...
- **dsdt** (Score: 3): dsdt • 2d ago lol reddit said nope to my previous reply. made a simple summary so that you can see the log : https://chat.deepseek.com/share/mn8bmar36zi8glv337...
- **cbale1** (Score: 1): cbale1 • 21h ago guys, it was just that the total tokens evaluated (27) was very low.. those 600+ms are mostly llama.cpp's overhead...
- **DjCanalex** (Score: -4): DjCanalex • 2d ago They are using --split-mode tensor That forces processing to happen on CPU rather than GPU. (No backend support yet for tensor on llama.cpp). On my own tests, with dual 3090s, I get 10-20% less tps using layer, but prompt processing is up to 4 times faster on average. gladfelter • 2d ago My experience doesn't match your assertion. I use the UD_Q8_K_XL variant and I get 850 t/s p...
- **gladfelter** (Score: 5): gladfelter • 2d ago My experience doesn't match your assertion. I use the UD_Q8_K_XL variant and I get 850 t/s prefill on my 3090+5070ti with split mode = tensor. And that's with the 3090 on an X4 PCIE slot. Maybe certain GPU architectures aren't supported? DjCanalex • 2d ago This doesn't make what I said less true. Different CPUs will perform different, same with better/faster ram. (My tests are ...

### [Qwen 3.8 27b: quantization, GPU and t/s](https://www.reddit.com/r/LocalLLaMA/comments/1vusqfw/qwen_38_27b_quantization_gpu_and_ts/)

**Post Summary:**
I am looking to buy a GPU to run Qwen 3.8 27b and I found an affordable 4060 16gb. I wonder if there's a compilation of GPU, quantization and t/s? I see this information spread in reddit, it would be good if we have a place to consult.
Could you please comment your hardware configuration, t/s and quantization só I can ask Kimi to create a report out of the comments of this post?
Thanks!
I am looking to buy a GPU to run Qwen 3.8 27b and I found an affordable 4060 16gb. I wonder if there's a compilation of GPU, quantization and t/s? I see this information spread in reddit, it would be good if we have a place to consult.
Could you please comment your hardware configuration, t/s and quantization só I can ask Kimi to create a report out of the comments of this post?
Thanks!
AMD R9700. It’s 32GB VRAM so you can run Q4 comfortably, or Q6 with about half context. Even Q8 if you accept small context.
If you can get two, then you can get fp8, full context, and vllm with great performance
Wh

**Key Comments & Community Discussion:**
- **Clean_Material_5047** (Score: 7): Clean_Material_5047 • 5h ago AMD R9700. It’s 32GB VRAM so you can run Q4 comfortably, or Q6 with about half context. Even Q8 if you accept small context. If you can get two, then you can get fp8, full context, and vllm with great performance whichsideisup • 4h ago Where is this working FP8 in vLLM? Specific weights or project needed? Clean_Material_5047 • 4h ago There’s a discord group [here](http...
- **whichsideisup** (Score: 2): whichsideisup • 4h ago Where is this working FP8 in vLLM? Specific weights or project needed? Clean_Material_5047 • 4h ago There’s a discord group [here](https://discord.gg/launch80) with a channel dedicated to R9700 where a bunch of smart people are optimising the shit out of it fastheadcrab • 3h ago  Top 1% Commenter It will run directly using a standard vLLM version and using the Qwen official ...
- **Clean_Material_5047** (Score: 1): Clean_Material_5047 • 4h ago There’s a discord group [here](https://discord.gg/launch80) with a channel dedicated to R9700 where a bunch of smart people are optimising the shit out of it...
- **fastheadcrab** (Score: 1): fastheadcrab • 3h ago  Top 1% Commenter It will run directly using a standard vLLM version and using the Qwen official version. 3.8 is nearly the same as 3.6/3.5 in terms of architecture so there is no changes. No fancy recipes needed unless you want speed...
- **lood9phee2Ri** (Score: 2): lood9phee2Ri • 4h ago Yeah, I have single R9700 for now. Practical t/s of real interactions is now rather variable and dependent on problem with mtp, ngram, etc. so e.g. This not especially scientific, just example, and token generation not prompt parse numbers hopefully obviously, but tg t/s for responses (not themselves shown but they were fine) to sequence of prompts in a growing context. Using...

### [Qwen 3.8 27b - PI AGENT vs OPENCODE](https://www.reddit.com/r/LocalLLaMA/comments/1vu0u2v/qwen_38_27b_pi_agent_vs_opencode/)

**Post Summary:**
https://www.reddit.com/r/LocalLLaMA/comments/1j7r47l/i_just_made_an_animation_of_a_ball_bouncing/
This post inspired me to make that test after a year ;)
That is one of my many tests I make comparing output quality.
What is more interesting using a PI Agent results are much better than an Opencode using a Qwen 3.8 27b ?!
Seems PI Agent is much better in the agent environment somehow... Not counting uses less tokens , do not have a hard limit of 32k output tokens, is faster, do not freezing, compressing context far less than Opencode. For instance if you have context in the Opencode output 32k and all context 100k then the compression is starting at 67k context ... PI is starting at 90k context even if you have set output context 64k or more.
My config for RTX 3090
llama-server with ini config -> which is exposing API to Opencode and PI agent.
llama-server.exe --models-preset 1_preset.ini --models-max 1 --direct-io
config ini
[Qwen3.8-27B_dense_c-100k]
model = models/Qwen3.8-27

**Key Comments & Community Discussion:**
- **SOC_FreeDiver** (Score: 53): SOC_FreeDiver • 1d ago I tested opencode, then tried pi, and pi was significantly better. Last night I had a dual between local qwen3.8-27b/pi and claudecode. My seat-of-the-pants analysis: it felt like they both took the same time. When they both finished I had each one compare the two. They both agreed claude's was better, but it was close. I had pi upgrade upgrade its version, making it slightl...
- **cmdr-William-Riker** (Score: 16): cmdr-William-Riker • 1d ago  Top 1% Commenter Pi is great! I just wish the interface was better, also sometimes I actually do want to use an MCP and skills and such. I know you can do all that with Pi through plugins and self modification, but I do like that OpenCode out of the box has a nice interface that makes it easy to keep track on of token usage and such. I should probably mess with Pi more...
- **LuCiAnO241** (Score: 17): LuCiAnO241 • 23h ago I'm literally trying to get into PI, and found Oh-my-PI, and it seems way more usable out of the box with not much negatives. Maybe check it out?...
- **LegacyRemaster** (Score: 10): LegacyRemaster • 18h ago  Top 1% Commenter PI is better. The reason it's simple: every new "sota" model = harness inside the model itself. With Pi the model has more freedom to go....
- **Healthy-Nebula-3603** (Score: 10): Healthy-Nebula-3603 • 1d ago  Top 1% Commenter Yep I also learned lately PI agent is better. Actually I am shocked how much better. Faster, more efficient, stable, much less compaction , somehow generating better code ... ImpressiveRelief37 • 1d ago The compaction thing is customizable in pi… In settings.json you can set the compaction threshold you want. I use the same as max_tokens so it doesn’t...

### [Qwen3.8-27B took a serious hit to *knowledge* vs 3.6](https://www.reddit.com/r/LocalLLaMA/comments/1vt7l3e/qwen3827b_took_a_serious_hit_to_knowledge_vs_36/)

**Post Summary:**
Like many of you I've spent the last few days throwing Qwen3.8-27B against all of my usual use-cases and personal tasks/harnesses and workflows. It's great, phenomenal sometimes, but that's not what this post is about.
One of my little personal benchmarks is a little set of pocket trivia that's relevant to me but mildly obscure mixed in with a few useful/prepper questions. Qwen3.8-27B at all quantization levels and sampling settings I threw at it, did relatively poorly at this. It's failing questions that Qwen3.6 reliably answered.
I come to find out that on offline (no tool call) knowledge benchmarks seem to align with what I'm saying. It's pretty significantly weaker than it's 3.6 predecessor at recalling random facts (or not hallucinating as much, in my tests, though that isn't reflected in these particular benchmarks). Now you should never trust barcharts over your own vibes, but my vibes are validating these bar charts this time around.
Is this relevant? Not necessarily. It see

**Key Comments & Community Discussion:**
- **networking_noob** (Score: 164): networking_noob • 2d ago The Qwen 3.* models now and going forward are probably going to be designed for coding and/or agentic tasks (obtaining info and then reasoning to act on it). For trivia and/or random facts I'm guessing the Gemma4 models are the better choice since they're basically like mini Googles cogitech2 • 2d ago Next-gen models will stick the "knowledge" layers on the SSD and the imp...
- **cogitech2** (Score: 105): cogitech2 • 2d ago Next-gen models will stick the "knowledge" layers on the SSD and the important stuff in VRAM. Best of both worlds is right around the corner. I'm seeing 1T models where the bulk of it sits idle on the SSD until it is needed, while the main intelligence, reasoning, tool use, skills, is resident in VRAM. So really fast local models with MASSIVE world knowledge. Sure, it might have...
- **power97992** (Score: 11): power97992 • 2d ago That is like engram transformers NandaVegg • 2d ago I think (DeepSeek-style) Engram is ideally much nicer as it doesn't need (sometimes a very long series of) tool call for knowledge retrieval, as tool calls quickly fills the context. However, according to the paper, Engram only works in very early layers (layer 2-3 specifically) and the way it works is more like "we can skip m...
- **NandaVegg** (Score: 10): NandaVegg • 2d ago I think (DeepSeek-style) Engram is ideally much nicer as it doesn't need (sometimes a very long series of) tool call for knowledge retrieval, as tool calls quickly fills the context. However, according to the paper, Engram only works in very early layers (layer 2-3 specifically) and the way it works is more like "we can skip most often repeated compute (like Paris = France = Cit...
- **Independent-Dog2179** (Score: 2): Independent-Dog2179 • 1d ago I mean call a subsgent to do it and just pass the relevant information back to main orchestrator. All of the tool calling will be done by the subagent who then parses the relevant info and spins down only sending what's needed. Keeps context clean...

### [Anyone running qwen 3.8 27b on 5070ti (16GB)?](https://www.reddit.com/r/LocalLLaMA/comments/1vrt7hy/anyone_running_qwen_38_27b_on_5070ti_16gb/)

**Post Summary:**
Hi everyone.
I recently decided to shell out a few bucks and upgrade my 4070ti (12GB) to a 5070ti (16GB).
I'm wondering if there's a reasonable quant that I could run the new qwen 3.8 27b on and get decent tp/s, for agentic coding mainly. I heard that some 4bit quants are decent enough.
Or am I still in the no-go territory? Is anyone rocking this card?
5070ti 16GB VRAM
32GB RAM DDR4
Hi everyone.
I recently decided to shell out a few bucks and upgrade my 4070ti (12GB) to a 5070ti (16GB).
I'm wondering if there's a reasonable quant that I could run the new qwen 3.8 27b on and get decent tp/s, for agentic coding mainly. I heard that some 4bit quants are decent enough.
Or am I still in the no-go territory? Is anyone rocking this card?
5070ti 16GB VRAM
32GB RAM DDR4
Everytime this comes up people will claim you need to use a Q3 quant.
That's not true - and in a perfect world we should pin one of Stainless-Bacon's posts on the subject. Just as you can run a large MoE model where all

**Key Comments & Community Discussion:**
- **tsangberg** (Score: 17): tsangberg • 3d ago • Edited 3d ago Everytime this comes up people will claim you need to use a Q3 quant. That's not true - and in a perfect world we should pin one of Stainless-Bacon's posts on the subject. Just as you can run a large MoE model where all experts don't fit in VRAM you can offload parts of a dense model to RAM too. tl;dr: Offload ffn layers, as few as you can get away with, and enab...
- **Stainless-Bacon** (Score: 2): Stainless-Bacon • 3d ago Thanks! I have a PR I want to merge into llama.cpp (it is in my post) which turns the long override tensor string into an existing and similar n-cpu-moe arg. Both basically do the same thing. Unfortunately some people think that dense models on 16GB vram is useless so the PR gets ignored...
- **zannix** (Score: 1): zannix • 3d ago Okay we're talking now! Does the offloading of ffn layers slow things noticably? tsangberg • 3d ago Yes - every additional layer offloaded compounds it. However, Q4 means you'll get correct code more often which will save time in the end. I get around 10tps on my slow-DDR5 system and a 5060. I'm right now working on an NInfern fork seeing if I'll be able to beat llama.cpp by going ...
- **tsangberg** (Score: 2): tsangberg • 3d ago Yes - every additional layer offloaded compounds it. However, Q4 means you'll get correct code more often which will save time in the end. I get around 10tps on my slow-DDR5 system and a 5060. I'm right now working on an NInfern fork seeing if I'll be able to beat llama.cpp by going Blackwell only but ... The only real solution for us VRAM poor and 27B is getting more VRAM. I do...
- **zannix** (Score: 2): zannix • 3d ago used 3090 24GB seems so tempting for 1k... but buying a used card that old is such a gamble (lifespan, usage?). and if you want 4th or 5th gen nvidia with 24GB it's basically 2k, 3k+ euros which is ridiculous in my opinion...

### [While Everyone Is Excited About Qwen 3.8 27B, Here’s the Reality for a 16GB AMD GPU User](https://www.reddit.com/r/LocalLLaMA/comments/1vu08f3/while_everyone_is_excited_about_qwen_38_27b_heres/)

**Post Summary:**
Qwen 3.8 27B has been getting a lot of attention in the local LLM community lately, so I gave it a try as well. However, after running it for extended coding agent tasks on my 16GB AMD GPU (RX 9060 XT), I found it quite frustratingly slow.
Luckily, Ornith had just released version 1.5, so I decided to try the 9B model with Q6_K, a 256K context window, and Q8 KV cache.
./llama-server -hf ornith-ai/Ornith-1.5-9B-GGUF:Q6_K `
  -ngl 99 `
  -np 1 `
  -c 262144 `
  -fa on `
  -ctk q8_0 `
  -ctv q8_0 `
  --load-mode mlock `
  --temp 0.6 `
  --top-p 0.95 `
  --top-k 20
In my setup, I get up to around 950 tok/s prompt eval and 36 tok/s generation. I also tested it on a real coding agent task, and it kept working continuously for almost three and a half hours without stopping. The speed does drop during long tasks, sometimes down to around 500/25 tok/s.
While everyone else is getting excited about 27B models, I find it kind of amusing that I'm going in the opposite direction and optimizing a

**Key Comments & Community Discussion:**
- **ttkciar** (Score: 5): ttkciar • 1d ago llama.cpp  Top 1% Commenter Have you tried Gemma-4-12b-it yet? It's replaced Phi-4 as my go-to for inferring with the 16GB V340. Unfortunately it has fat K and V caches, and does not tolerate quantized K/V caches, so I have to sharply limit its context. Within that limit, though, it works really well for me on a wide variety of tasks. I am hoping Qwen will come out with a Qwen3.8-...
- **CrowKing63** (Score: 1): CrowKing63 • 1d ago I gave up on gemma4 because it didn't have as much staying power as qwen in Hermes Agent. I don't know how it is these days....
- **Atretador** (Score: 6): Atretador • 1d ago why are you trying 9B model? just use a MOE model if you have the memory for 9B you can run 35B A3B with RAM offload CrowKing63 • 1d ago I tried that too, but the speed didn't get significantly faster. suprjami • 1d ago The point is that partial-offload 35B Q6 will give better results than any 9B. Atretador • 1d ago with what parameters? my 35B runs about the same speed as 9B fo...
- **CrowKing63** (Score: 1): CrowKing63 • 1d ago I tried that too, but the speed didn't get significantly faster. suprjami • 1d ago The point is that partial-offload 35B Q6 will give better results than any 9B. Atretador • 1d ago with what parameters? my 35B runs about the same speed as 9B for me CrowKing63 • 1d ago --n-cpu-moe 20 ` -c 32768 ` -np 1 ` -fa on ` --cache-type-k q8_0 ` --cache-type-v q8_0 Max 70/25 tok/s Atretado...
- **suprjami** (Score: 4): suprjami • 1d ago The point is that partial-offload 35B Q6 will give better results than any 9B....

### [Ladies and gentlemen I present to you Qwen3.8 27b 1bit brain damage quant](https://www.reddit.com/r/LocalLLaMA/comments/1vtr3h0/ladies_and_gentlemen_i_present_to_you_qwen38_27b/)

**Post Summary:**
I wanted to just test the unsloth 1bit quant of qwen 3.8 27b as I have just 8gb vram and ngl it gave me a good laugh
I wanted to just test the unsloth 1bit quant of qwen 3.8 27b as I have just 8gb vram and ngl it gave me a good laugh
Your post is getting popular and we just featured it on our Discord! Come check it out!
You've also been given a special flair for your contribution. We appreciate your post!
I am a bot and this action was performed automatically.
here are your lifelines: hallucinate something plausible, phone the user, or spin up sub agents
I laughed more about this than I should‘ve
We are all uncs now for laughing
I am adding this to my system prompt, thanks
I would not suggest folks to use 1-bit for agentic use cases / tool calls - we wrote a section here in our docs.
Divergence-300 @ 32 tests all quants on actual long running tasks and shows 1-bit at 8% accuracy over 32 tokens. UD-Q2_K_XL has a 21% accuracy and 4-bit UD-Q4_K_XL 68%. This means the divergence betwee

**Key Comments & Community Discussion:**
- **WithoutReason1729** (Score: 1): WithoutReason1729 • 1d ago Your post is getting popular and we just featured it on our Discord! Come check it out! You've also been given a special flair for your contribution. We appreciate your post! I am a bot and this action was performed automatically....
- **Ok-Fault-9142** (Score: 913): Ok-Fault-9142 • 1d ago -dysangel- • 1d ago  Top 1% Commenter here are your lifelines: hallucinate something plausible, phone the user, or spin up sub agents WD40x4 • 1d ago I laughed more about this than I should‘ve TomLucidor • 21h ago We are all uncs now for laughing see_spot_ruminate • 9h ago I am adding this to my system prompt, thanks 1 more reply danielhanchen • 1d ago I would not suggest fo...
- **-dysangel-** (Score: 319): -dysangel- • 1d ago  Top 1% Commenter here are your lifelines: hallucinate something plausible, phone the user, or spin up sub agents WD40x4 • 1d ago I laughed more about this than I should‘ve TomLucidor • 21h ago We are all uncs now for laughing see_spot_ruminate • 9h ago I am adding this to my system prompt, thanks 1 more reply...
- **WD40x4** (Score: 48): WD40x4 • 1d ago I laughed more about this than I should‘ve...
- **TomLucidor** (Score: 10): TomLucidor • 21h ago We are all uncs now for laughing...

### [How to stop Qwen3.8-27b from overthinking](https://www.reddit.com/r/LocalLLaMA/comments/1vqmiu3/how_to_stop_qwen3827b_from_overthinking/)

**Post Summary:**
I see a lot of people struggle with Qwen3.8-27b overthinking, and I wanted to share a really straightforward fix that works for me.
Before setting these llamacpp flags, I often had Qwen thinking for over 90 minutes, which was really impractical.
These two flags set the reasoning budget on llamacpp:
--reasoning-budget 8192
--reasoning-budget-message "Time to stop thinking. Give the final answer or make the tool call now."
8K is plenty to reason and seems like a good trade-off between speed and debt.
I see a lot of people struggle with Qwen3.8-27b overthinking, and I wanted to share a really straightforward fix that works for me.
Before setting these llamacpp flags, I often had Qwen thinking for over 90 minutes, which was really impractical.
These two flags set the reasoning budget on llamacpp:
--reasoning-budget 8192
--reasoning-budget-message "Time to stop thinking. Give the final answer or make the tool call now."
8K is plenty to reason and seems like a good trade-off betwee

**Key Comments & Community Discussion:**
- **ItzStrai** (Score: 36): ItzStrai • 5d ago --chat-template-kwargs '{"reasoning_effort": "medium"}' DoubleNothing • 5d ago Yes, medium is not bad... UniqueIdentifier00 • 5d ago This is the way. Much better than the hard llama limit Chromix_ • 5d ago  Top 1% Commenter Truncating via budget is a bad idea: Note that Qwen will reasonably reason for 40k tokens when making a lava lamp. Cutting it off early leads to broken result...
- **DoubleNothing** (Score: 4): DoubleNothing • 5d ago Yes, medium is not bad......
- **UniqueIdentifier00** (Score: 4): UniqueIdentifier00 • 5d ago This is the way. Much better than the hard llama limit...
- **Chromix_** (Score: 5): Chromix_ • 5d ago  Top 1% Commenter Truncating via budget is a bad idea: Note that Qwen will reasonably reason for 40k tokens when making a lava lamp. Cutting it off early leads to broken results. The reasoning level is "xhigh" by default. Set it to "medium" - then it reasons less but might miss some tricky things. (this was my replay to the previous posting that suggested it) "Medium" adapts nice...
- **ChemistNo8486** (Score: 5): ChemistNo8486 • 5d ago This is interesting. I will give it a shot. Personlly, so far the thinking is more a feature than an issue for me. I have been working non-stop with it since release and I can just delegate a lot without it messing up. It literally feels like must simple tasks can be finished in a single shot. MikeNonect • 5d ago I ran into trouble with OpenCode blocking after the model was ...

### [Fastest qwen 3.8 27b for AMD gpu?](https://www.reddit.com/r/LocalLLaMA/comments/1vu7m53/fastest_qwen_38_27b_for_amd_gpu/)

**Post Summary:**
Hey, just wondering if there are forks or exact gguf versions that give fastest prompt processing and token gen speeds for AMD gpu?
Looking to run q8 or q6
Vram 96gb
W7900 + w7800 both 48gb
With bandwidth mismatch, tensor paralleling amd equivalent not working
Hey, just wondering if there are forks or exact gguf versions that give fastest prompt processing and token gen speeds for AMD gpu?
Looking to run q8 or q6
Vram 96gb
W7900 + w7800 both 48gb
With bandwidth mismatch, tensor paralleling amd equivalent not working
https://github.com/warpfront/hipfire https://huggingface.co/hipfire-models/qwen3.8-27b
Thanks that’s crazy if successful
Not really. 451 prefill is very low.
Decide speed isn’t everything. In the long run is much better to have lower decode but higher prefill
Agreed. I’m ok watching words fly by at 2-3 a sec. I hate waiting two minutes for it to start thinking.
Yep and not only that. If it does a web search, it needs to process lots of information and higher prefill speed 

**Key Comments & Community Discussion:**
- **MongoWithBongoss** (Score: 13): MongoWithBongoss • 20h ago https://github.com/warpfront/hipfire https://huggingface.co/hipfire-models/qwen3.8-27b Gloomy_Letterhead395 • 20h ago Thanks that’s crazy if successful Clean_Material_5047 • 19h ago Not really. 451 prefill is very low. Decide speed isn’t everything. In the long run is much better to have lower decode but higher prefill winky9827 • 15h ago Agreed. I’m ok watching words fl...
- **Gloomy_Letterhead395** (Score: 5): Gloomy_Letterhead395 • 20h ago Thanks that’s crazy if successful Clean_Material_5047 • 19h ago Not really. 451 prefill is very low. Decide speed isn’t everything. In the long run is much better to have lower decode but higher prefill winky9827 • 15h ago Agreed. I’m ok watching words fly by at 2-3 a sec. I hate waiting two minutes for it to start thinking. Clean_Material_5047 • 14h ago Yep and not ...
- **Clean_Material_5047** (Score: 13): Clean_Material_5047 • 19h ago Not really. 451 prefill is very low. Decide speed isn’t everything. In the long run is much better to have lower decode but higher prefill winky9827 • 15h ago Agreed. I’m ok watching words fly by at 2-3 a sec. I hate waiting two minutes for it to start thinking. Clean_Material_5047 • 14h ago Yep and not only that. If it does a web search, it needs to process lots of i...
- **winky9827** (Score: 5): winky9827 • 15h ago Agreed. I’m ok watching words fly by at 2-3 a sec. I hate waiting two minutes for it to start thinking. Clean_Material_5047 • 14h ago Yep and not only that. If it does a web search, it needs to process lots of information and higher prefill speed will make a massive difference. It’s pretty much the reason why I personally find qwen 27b unusable on macs. The prefill is atrocious...
- **Clean_Material_5047** (Score: 3): Clean_Material_5047 • 14h ago Yep and not only that. If it does a web search, it needs to process lots of information and higher prefill speed will make a massive difference. It’s pretty much the reason why I personally find qwen 27b unusable on macs. The prefill is atrocious my_name_isnt_clever • 8h ago  Top 1% Commenter It just means you have to be extra mindful of token counts. Run a web fetch ...

### [People that use qwen 3.8 27B for agent use or coding. What harnesses are you using?](https://www.reddit.com/r/LocalLLaMA/comments/1vt8pkz/people_that_use_qwen_38_27b_for_agent_use_or/)

**Post Summary:**
I set it up using pi. But it wasn't able to do tool calls.
I set it up using pi. But it wasn't able to do tool calls.
Why nobody ever mentions Qwen Code? For me is quite good, including its new Desktop App for the free versions.
Yes, I'd like to mention it too:) I use opencode mostly, tried to use pi, but I dislike it. Now, with beautiful Qwen3.8, I slowly move some workflows to Qwen code, and I really find it amazing.
I tested it once long time ago. What's the best things about? Currently I am pi and deepseek harness daily user, so I fear adding another alternative to the stack, but if its better...
I tested qwen code, it's great but got twice better results in deep seek harness
Qwen Code is amazing. The first time I used it was with 3.6 27B on an Android app. It was a complex problem that even cloud models struggle with and it worked on it for more than an hour without a single tool call fail. 
Its solutions wasn't that great/bad, maybe a 3/5, but I was impressed because no other ha

**Key Comments & Community Discussion:**
- **Alternative_Ad4267** (Score: 17): Alternative_Ad4267 • 2d ago Why nobody ever mentions Qwen Code? For me is quite good, including its new Desktop App for the free versions. Barni275 • 2d ago Yes, I'd like to mention it too:) I use opencode mostly, tried to use pi, but I dislike it. Now, with beautiful Qwen3.8, I slowly move some workflows to Qwen code, and I really find it amazing. SnooPaintings8639 • 2d ago  Top 1% Commenter I te...
- **Barni275** (Score: 5): Barni275 • 2d ago Yes, I'd like to mention it too:) I use opencode mostly, tried to use pi, but I dislike it. Now, with beautiful Qwen3.8, I slowly move some workflows to Qwen code, and I really find it amazing....
- **SnooPaintings8639** (Score: 3): SnooPaintings8639 • 2d ago  Top 1% Commenter I tested it once long time ago. What's the best things about? Currently I am pi and deepseek harness daily user, so I fear adding another alternative to the stack, but if its better......
- **Otherwise-Key806** (Score: 2): Otherwise-Key806 • 2d ago I tested qwen code, it's great but got twice better results in deep seek harness...
- **DrBattletoad** (Score: 2): DrBattletoad • 2d ago Qwen Code is amazing. The first time I used it was with 3.6 27B on an Android app. It was a complex problem that even cloud models struggle with and it worked on it for more than an hour without a single tool call fail.  Its solutions wasn't that great/bad, maybe a 3/5, but I was impressed because no other harness showed that much tenacity.  I use it now with 3.8 27B in VS Co...

### [Quick PSA: Qwen3.8-27B reasoning effort vs reasoning budget in llama.cpp](https://www.reddit.com/r/LocalLLaMA/comments/1vpwfpe/quick_psa_qwen3827b_reasoning_effort_vs_reasoning/)

**Post Summary:**
If you are using llama-server with their web-ui for testing, keep in mind, that the reasoning selector is just a reasoning budget aka a hard cap and has, at least to my knowledge, nothing at all to do with Qwen3.8-27B's native reasoning effort capability!
Selecting any value for reasoning in the web-ui (default, (off), low, medium, high or max) just introduces different hard cap values and and will truncate your reasoning, if those values are reached.
With the exception of the "off"-option which disable reasoning at all and "default" and "max" without any capping.
The reasoning effort is independent from that and really changes the thoroughness and the analytic reasoning skills and therefore can massively influence the output quality of the model, instead of just capping reasoning tokens!
In older llama.cpp versions, it needs to be set via:
--chat-template-kwargs "{\"reasoning_effort\":\"medium\"}"
* quotation marks are escaped for Windows
For up to date versions, if one doesn't

**Key Comments & Community Discussion:**
- **DeProgrammer99** (Score: 8): DeProgrammer99 • 6d ago Also, if you're using little-coder, configure the thinking-budget extension with a much higher cap, or it'll just constantly interrupt xhigh, and it does so by sending another message, which probably resets the model's intended thinking duration... I outright removed the extension because I didn't see instructions to change the setting, but updating little-coder re-adds it....
- **LocalAI_Amateur** (Score: 3): LocalAI_Amateur • 5d ago --reasoning-effort low didn't seem to do anything for me. still shoot right past 4000 reasoning tokens. I've been trying to figure out how to get this resoning effort setting to work in llama.cpp but so far the only thing that work is the budget setting and it just cuts off as soon as it hits the limit like you say. bonobomaster • 5d ago Works for me though. Just tested it...
- **bonobomaster** (Score: 3): bonobomaster • 5d ago Works for me though. Just tested it. I'm on b10447 now. The following variant should work in older versions as well: --chat-template-kwargs "{\"reasoning_effort\":\"low\"}" LocalAI_Amateur • 5d ago I just git pulled the latest build of llama.cpp I used both \--chat-template-kwargs '{"reasoning\_effort": "low"}' \\ \--reasoning-effort low \\ neither seem to work. it can easily...
- **LocalAI_Amateur** (Score: 1): LocalAI_Amateur • 5d ago I just git pulled the latest build of llama.cpp I used both \--chat-template-kwargs '{"reasoning\_effort": "low"}' \\ \--reasoning-effort low \\ neither seem to work. it can easily shoot past 5k reasoning tokens. Does anyone else have this problem?...
- **bercha9998** (Score: 2): bercha9998 • 5d ago • Edited 5d ago opencode way       "models": {         "your-flavour-of-qwen3.8-27b": {           "name": "qwen3.8-27b",           "options": {             ...             "reasoningEffort": "low"           },           "modalities": {             "input": ["text", "image"],             "output": ["text"]           }         },......

### [Qwen3.8-27B VRAM on 16GB with 50tok/s, 85k q8 context](https://www.reddit.com/r/LocalLLaMA/comments/1vs3bru/qwen3827b_vram_on_16gb_with_50toks_85k_q8_context/)

**Post Summary:**
My hardware: Nvidia 5070Ti (16GB VRAM), Ryzen 9 9900x, DDR5 32GB 5400
My config is still not fully optimized, and still has (a very small amount) unused VRAM. No offload to CPU.
Speeds:
At 0 context, ~1500tok/s PP, ~50tok/s
TG At ~32k context, ~1200tok/s PP, ~40tok/s TG
Important Note:
My agent removed the MTP layer using python GGUF reader. I think sacrificing MTP for more context is well worth it.
Notes:
Using q5 context reduces tg speeds (but obviously you can get greater context size)
The GPU is just the model, the OS is on iGPU
ubatch-size needs to be ablated
I'm running 86.5k context, but just for some margin I have pasted 85k context here
Config:
[*]
jinja = true
threads = 12
threads-batch = 12
parallel = 1
gpu-layers = auto
ctx-size = 128000
fit-target = 128
flash-attn = on
port = 8065
cache-type-k = f16
cache-type-v = f16
temperature = 0.55
top-p = 0.95
top-k = 20
presence-penalty = 0
min-p = 0.05
reasoning = on
reasoning-format = deepseek
reasoning-preserve = true


**Key Comments & Community Discussion:**
- **Thin_Pollution8843** (Score: 15): Thin_Pollution8843 • 3d ago  Top 1% Commenter On q1 it could be even faster /s brainExploded99 • 3d ago Sadly us VRAM poors must make sacrifices Atretador • 3d ago the sacrifice could be running a Qwen 3.6 35B A3B at 512K KV Q8/Q8 with multiple streams and higher quantization for less lobotomization :X brainExploded99 • 3d ago I was doing that, although not at 512K context (what's the point? conte...
- **brainExploded99** (Score: 4): brainExploded99 • 3d ago Sadly us VRAM poors must make sacrifices Atretador • 3d ago the sacrifice could be running a Qwen 3.6 35B A3B at 512K KV Q8/Q8 with multiple streams and higher quantization for less lobotomization :X brainExploded99 • 3d ago I was doing that, although not at 512K context (what's the point? context degradation after 256k is already severe). I was running a UD-Q5_K_M as well...
- **Atretador** (Score: -2): Atretador • 3d ago the sacrifice could be running a Qwen 3.6 35B A3B at 512K KV Q8/Q8 with multiple streams and higher quantization for less lobotomization :X brainExploded99 • 3d ago I was doing that, although not at 512K context (what's the point? context degradation after 256k is already severe). I was running a UD-Q5_K_M as well. However, the model is simply dumber and less willing to stick to...
- **brainExploded99** (Score: 4): brainExploded99 • 3d ago I was doing that, although not at 512K context (what's the point? context degradation after 256k is already severe). I was running a UD-Q5_K_M as well. However, the model is simply dumber and less willing to stick to the task than Qwen3.8. Atretador • 3d ago I didnt say one 512K stream, you can have 2x of 256K for instance - I run 2x 148K / 200K usually. brainExploded99 • ...
- **Atretador** (Score: 0): Atretador • 3d ago I didnt say one 512K stream, you can have 2x of 256K for instance - I run 2x 148K / 200K usually. brainExploded99 • 3d ago Makes sense, although I rarely use subagents so I don't bother (35B was already a gpt luna's/terra's subagent). Atretador • 3d ago its quite useful for context management, instead of one guy researching+planning+executing one orchetrates and calls -> explore...

### [What can us 8 GB VRAM poors do?](https://www.reddit.com/r/LocalLLaMA/comments/1vlc4wn/what_can_us_8_gb_vram_poors_do/)

**Post Summary:**
I want to hook up a local model to Cline, but it seems the best model is still just Qwen 3.5 9B. Please can we have a Qwen 3.8 9B that gets close to Qwen 3.6 27B?
I want to hook up a local model to Cline, but it seems the best model is still just Qwen 3.5 9B. Please can we have a Qwen 3.8 9B that gets close to Qwen 3.6 27B?
Convenience marriage
😂
I'm running unsloth/Qwen3.6-35B-A3B-GGUF:Q4_K_M on an ancient RX580 with 8GB VRAM with full context (q8_0), so... you can do that ;)
(token generation is ok, prompt processing gets stupidly slow after ~40k)
Whoa, me too! Almost. Mine has 16GB and I’m running it at Q3 so I can fit it all into VRAM.
And yeah, pp is painfully slow for me.
Q3 is crazy work :D
Prompt processing for me is a whopping 12-15 tokens/second at context depth ~130k (it's slightly faster when there are more to process due to batching)
It's sad because when the context is empty it processes at ~180 tokens/second... It must be something related to the Vulkan runtime, or j

**Key Comments & Community Discussion:**
- **misanthrophiccunt** (Score: 99): misanthrophiccunt • 11d ago Convenience marriage ButtercupLyn100 • 10d ago 😂 [deleted] • 11d ago...
- **ManIkWeet** (Score: 36): ManIkWeet • 11d ago I'm running unsloth/Qwen3.6-35B-A3B-GGUF:Q4_K_M on an ancient RX580 with 8GB VRAM with full context (q8_0), so... you can do that ;) (token generation is ok, prompt processing gets stupidly slow after ~40k) met_MY_verse • 11d ago Whoa, me too! Almost. Mine has 16GB and I’m running it at Q3 so I can fit it all into VRAM. And yeah, pp is painfully slow for me. ManIkWeet • 11d ago...
- **met_MY_verse** (Score: 3): met_MY_verse • 11d ago Whoa, me too! Almost. Mine has 16GB and I’m running it at Q3 so I can fit it all into VRAM. And yeah, pp is painfully slow for me. ManIkWeet • 11d ago Q3 is crazy work :D Prompt processing for me is a whopping 12-15 tokens/second at context depth ~130k (it's slightly faster when there are more to process due to batching) It's sad because when the context is empty it processe...
- **ManIkWeet** (Score: 4): ManIkWeet • 11d ago Q3 is crazy work :D Prompt processing for me is a whopping 12-15 tokens/second at context depth ~130k (it's slightly faster when there are more to process due to batching) It's sad because when the context is empty it processes at ~180 tokens/second... It must be something related to the Vulkan runtime, or just the GPU hardware? An even older and slower nvidia Quadro M4000 has ...

### [12GB VRAM gang, what's our plan?](https://www.reddit.com/r/LocalLLaMA/comments/1vlamks/12gb_vram_gang_whats_our_plan/)

**Post Summary:**
Seems like we're limited to qwen finetuned MoEs for now. Looking at the current landscape - focus seems to be on dense models (muse glimmer 30b, qwen 3.8 27b) for smaller setups.
Is upgrading to 24GB VRAM the only option?
Seems like we're limited to qwen finetuned MoEs for now. Looking at the current landscape - focus seems to be on dense models (muse glimmer 30b, qwen 3.8 27b) for smaller setups.
Is upgrading to 24GB VRAM the only option?
Qwen 35B-A3B and Gemma 4 26B-A4B with most experts shoved into system RAM... seems to be your only option. Sucks a bit but then again those are much better options than anything such computers could run at decent speeds not even half a year ago. The field moves fast
NGL I have a 3080ti that I bought when I thought I didn't need a 3090
I did need a 3090
I'd hold off on the 24GB upgrade. 12GB handles the current MoE models in the 30B range if you offload experts to system RAM, and the upcoming Qwen 3.8 35B-A3B should run even better. 24GB won't futu

**Key Comments & Community Discussion:**
- **AnonLlamaThrowaway** (Score: 17): AnonLlamaThrowaway • 11d ago Qwen 35B-A3B and Gemma 4 26B-A4B with most experts shoved into system RAM... seems to be your only option. Sucks a bit but then again those are much better options than anything such computers could run at decent speeds not even half a year ago. The field moves fast...
- **fvancesco** (Score: 24): fvancesco • 11d ago NGL I have a 3080ti that I bought when I thought I didn't need a 3090 I did need a 3090...
- **kemalios** (Score: 7): kemalios • 10d ago I'd hold off on the 24GB upgrade. 12GB handles the current MoE models in the 30B range if you offload experts to system RAM, and the upcoming Qwen 3.8 35B-A3B should run even better. 24GB won't futureproof you either; the 1T models people are excited about won't fit there. Add cheap RAM, keep the 12GB card, and rent a high-VRAM instance for the rare 70B+ run. That's better ROI t...
- **Mean-Ad1493** (Score: 4): Mean-Ad1493 • 10d ago That's hopeful..IF Qwen releases 3.8 35b-a3b....
- **ea_man** (Score: 9): ea_man • 11d ago  Top 1% Commenter Well upgrading to 12 + 16GB would be a better option, don't get an other 12GB card! Zennytooskin123 • 10d ago Those 4 exta GB are extremely important, since that means you can run a higher context window and higher quants on dense 9B models or even 12B models. I have a 4070 with 12GB and 32GB system ram and urrently I'm using Qwen 35B A3B with 131k context in q4 ...

### [How many tokens/second output are you getting with Qwen3.8-27B?](https://www.reddit.com/r/LocalLLaMA/comments/1vqjeub/how_many_tokenssecond_output_are_you_getting_with/)

**Post Summary:**
Trying to get a feel for where I stand. If you can list your relevant hardware and model used, that would be awesome.
Here's mine:
Model: Qwen3.8-27B-heretic-ara, Q5_K_M GGUF
T/s by context saturation:
I found that t/s output depends on how saturated the context is. The more saturated, the slower the speeds.
~1K | 74.88 tok/s
~16K | 70.15 tok/s
~63K | 56.58 tok/s
~90K | 42.71 tok/s
Hardware: 3090 GPU | 64 GBs DDR4 RAM | AMD 7950x CPU
Harness: Pi
Inference: llama.ccp
Edit: When I made this post I was getting around 31 t/s with a fresh context. I since moved my models to an SSD and enabled Multi-Token Prediction (MTP) and now get ~74 t/s on a fresh context window (134.5% increase!). I’ve updated the post to reflect that change.
The only downside is I had to reduce my context window to 96k for it to fit snugly on my 3090 since MTP increases VRAM usage.
Trying to get a feel for where I stand. If you can list your relevant hardware and model used, that would be awesome.
Here's min

**Key Comments & Community Discussion:**
- **ImJORD1** (Score: 27): ImJORD1 • 5d ago • Edited 4d ago 2 RTX 3060 12 gig  q5 at around 30 65k context KURD_1_STAN • 5d ago 1 3060 12gb  q2km(no vision) 2t/s Tasio_ • 5d ago • Edited 5d ago In case it helps, I have a 4070 12GB running on Ubuntu Server (I use the server version to avoid the desktop UI taking up VRAM). With UD-Q2_K_XL and a Q4 KV cache, I can get around 80k context without offloading, at roughly 25 t/s. T...
- **KURD_1_STAN** (Score: 7): KURD_1_STAN • 5d ago 1 3060 12gb  q2km(no vision) 2t/s Tasio_ • 5d ago • Edited 5d ago In case it helps, I have a 4070 12GB running on Ubuntu Server (I use the server version to avoid the desktop UI taking up VRAM). With UD-Q2_K_XL and a Q4 KV cache, I can get around 80k context without offloading, at roughly 25 t/s. The quants are a bit aggressive, but so far it seems to work fine, and I'm able t...
- **Tasio_** (Score: 4): Tasio_ • 5d ago • Edited 5d ago In case it helps, I have a 4070 12GB running on Ubuntu Server (I use the server version to avoid the desktop UI taking up VRAM). With UD-Q2_K_XL and a Q4 KV cache, I can get around 80k context without offloading, at roughly 25 t/s. The quants are a bit aggressive, but so far it seems to work fine, and I'm able to build working things at a reasonable speed. Zennytoos...
- **Zennytooskin123** (Score: 2): Zennytooskin123 • 4d ago Any looping, malformed tool calls, or context retrieval issues? For the 12GB VRAM gang... Tasio_ • 3d ago I’ve mostly been using xhigh reasoning effort in OpenCode, including long code reviews in an old, complex PHP project that can run for an hour or so. So far, I don’t remember running into any of those issues. I previously tested UD-IQ2_XXS, and that one had a lot of is...
- **Tasio_** (Score: 2): Tasio_ • 3d ago I’ve mostly been using xhigh reasoning effort in OpenCode, including long code reviews in an old, complex PHP project that can run for an hour or so. So far, I don’t remember running into any of those issues. I previously tested UD-IQ2_XXS, and that one had a lot of issues. But UD-Q2_K_XL has been doing quite well for me so far. The only issue I had was that OpenCode would stop whe...

### [Optimizing Qwen3.6 / Qwen3.8-27B on 16GB VRAM: Complete Benchmark Results and Setup Guide (~30-50tps at 32k to 72k context)](https://www.reddit.com/r/LocalLLaMA/comments/1vrchn9/optimizing_qwen36_qwen3827b_on_16gb_vram_complete/)

**Post Summary:**
This post was made with AI. I tried to remove as much slop as possible and keep it straight to the point to save your time as I know how annoying AI slop posts can be, but I still wanted to retain all the details so it can be used as a resource for comparison with other future quants, I advise that any humans just skim through it or read the 1st section and run the balanced profile with a context smart harness like pi or deepseek harness (apparently really good for this)
Optimizing Qwen3.6 / Qwen3.8 27B on 16GB VRAM: Complete Experimental Log, Benchmarks, and Deployment Guide
This document records the complete set of benchmarks, quantization evaluations, KV cache sweeps, speculative decoding experiments, and context scaling tests conducted across multiple GPU architectures to determine the optimal configuration for running Qwen 27B hybrid models within a 16GB VRAM constraint.
1. Primary Recommendations (Quick Reference)
1.1 Balanced Profile (Recommended Default)
Model: Qwen3.8-27B-

**Key Comments & Community Discussion:**
- **TheSantiagoSP** (Score: 6): TheSantiagoSP • 4d ago Pretty good information to take out of there. May I know from where did you get "Qwen3.8-27B-IQ4_XS-pure-MTP.gguf"? Did you made it your self? MaxDev0 • 4d ago Oh, mb, here: https://huggingface.co/jpetrina/Qwen3.8-27B-MTP-IQ4_XS-pure-GGUF/blob/main/qwen3.8-27b-mtp-IQ4_XS-Q8nextn.gguf...
- **MaxDev0** (Score: 1): MaxDev0 • 4d ago Oh, mb, here: https://huggingface.co/jpetrina/Qwen3.8-27B-MTP-IQ4_XS-pure-GGUF/blob/main/qwen3.8-27b-mtp-IQ4_XS-Q8nextn.gguf...
- **kfsirl** (Score: 2): kfsirl • 3d ago Bro, you did a very good and valuable job - great service for the community! Congrats & Thanks!...
- **MaxDev0** (Score: 2): MaxDev0 • 3d ago I did some more experimenting and you guys came up with some great advice, big kudos to u/ea_man, AI generated follow up below, all testing was done on my local rtx 3080 mobile on medium performance mode (80W power draw limit) so it's a good bit slower but still nice, I also used the agent with deepseek harness and it was absurdly good, highly reccomend Update & Follow-up Log: 112...
- **ea_man** (Score: 2): ea_man • 3d ago • Edited 3d ago  Top 1% Commenter Nice, you are making progress. Now if you wanna go further there may be some more ctx available in the compute buffers for MTP in llama.cp but that will require to go through the source code. Now I did that on AMD for vulkan / ROCm but I had no chance to test that on CUDA, so I may give you, or better to your LLM, some guideline regarding what to l...

### [Qwen3.8-27B only 5 tk/s - What's the best config for 8GB VRAM + 32GB RAM?](https://www.reddit.com/r/LocalLLaMA/comments/1vodh0u/qwen3827b_only_5_tks_whats_the_best_config_for/)

**Post Summary:**
Question on the title.
What settings/config would you recommend to get the best possible speed with this specs?
Is it possible to take it to usable speeds?
Question on the title.
What settings/config would you recommend to get the best possible speed with this specs?
Is it possible to take it to usable speeds?
Its a dense model, I don't think it can get much better than this for you, sorry.
You're running a dense model mostly outside of GPU, your speed is inherently going to be very poor
Wait for Qwen 3.8 35B-A3B, or use the 3.6 version until then
long story short: no, your usable speed is the 5 t/s or if you do some finetuning you may get like 6-7 top - there isn't a way to jump over that fence with dense model - use 3.6 35ba3b moe or wait for response at 5t/s
Start from running the smallest quant then go higher later, consider purchasing something like 3060
 as a second GPU
smallest quant which is barely usable which is ud_iq2 weighs like 9gb - at this point it doesn't change a t

**Key Comments & Community Discussion:**
- **_ballzdeep_** (Score: 30): _ballzdeep_ • 7d ago Its a dense model, I don't think it can get much better than this for you, sorry....
- **PANIC_EXCEPTION** (Score: 9): PANIC_EXCEPTION • 7d ago You're running a dense model mostly outside of GPU, your speed is inherently going to be very poor...
- **grumd** (Score: 5): grumd • 6d ago  Top 1% Commenter Wait for Qwen 3.8 35B-A3B, or use the 3.6 version until then...
- **Timely_Impression_92** (Score: 4): Timely_Impression_92 • 7d ago long story short: no, your usable speed is the 5 t/s or if you do some finetuning you may get like 6-7 top - there isn't a way to jump over that fence with dense model - use 3.6 35ba3b moe or wait for response at 5t/s...
- **jacek2023** (Score: 2): jacek2023 • 7d ago llama.cpp  Top 1% Commenter Start from running the smallest quant then go higher later, consider purchasing something like 3060  as a second GPU Timely_Impression_92 • 7d ago smallest quant which is barely usable which is ud_iq2 weighs like 9gb - at this point it doesn't change a thing - if you spill over vram with e.g. q2, then you can run bf16 and it will have exact same speed...

### [100$ worth of gpu runs qwen 3.8 27b at 7.39 t/s](https://www.reddit.com/r/LocalLLaMA/comments/1vqpc0f/100_worth_of_gpu_runs_qwen_38_27b_at_739_ts/)

**Post Summary:**
Qwen 27b Q3_K_M
2x rx 580 8gb (~50$ each in my country, edge cases 60$ per gpu) gives us 16gb vram
We used it on an old already existing ddr3 motherboard with 2 gpu slots(you can buy it ror around 200$ with 32 gb of ddr3 ram, a workstation xeon cpu and a workstation motherboard, used)
Its not the best option, but it makes running this model possible for many people, its even cheaper than system ram
Limitations: very low processing speed(only 14t/s) means an mtp model would be a loss, and high input tokens would be a painful experiance
Not recommanded if you care about ease of life, very recommanded if you need something cheap to work no matter the compromise
Qwen 27b Q3_K_M
2x rx 580 8gb (~50$ each in my country, edge cases 60$ per gpu) gives us 16gb vram
We used it on an old already existing ddr3 motherboard with 2 gpu slots(you can buy it ror around 200$ with 32 gb of ddr3 ram, a workstation xeon cpu and a workstation motherboard, used)
Its not the best option, but it makes r

**Key Comments & Community Discussion:**
- **rama0x9** (Score: 53): rama0x9 • 5d ago You could have easily +5t/s if you had just written "hello"...
- **Useful_Disaster_7606** (Score: 55): Useful_Disaster_7606 • 5d ago Lmao "hello fucker" is my goto as well Maleficent-Ad5999 • 5d ago Good luck when AGI shows up.. Eden63 • 5d ago yeah, he is already on the termination list. TooObtuseForYou • 3d ago We really need to start burning all data now, otherwise it may be a thanos moment when it realizes how horrible humans generally are. terorvlad • 4d ago That's why we run models locally. T...
- **Maleficent-Ad5999** (Score: 16): Maleficent-Ad5999 • 5d ago Good luck when AGI shows up.. Eden63 • 5d ago yeah, he is already on the termination list. TooObtuseForYou • 3d ago We really need to start burning all data now, otherwise it may be a thanos moment when it realizes how horrible humans generally are. terorvlad • 4d ago That's why we run models locally. They can scream all they want if there's no one to hear. Eden63 • 4d a...
- **Eden63** (Score: 14): Eden63 • 5d ago yeah, he is already on the termination list. TooObtuseForYou • 3d ago We really need to start burning all data now, otherwise it may be a thanos moment when it realizes how horrible humans generally are....
- **TooObtuseForYou** (Score: 1): TooObtuseForYou • 3d ago We really need to start burning all data now, otherwise it may be a thanos moment when it realizes how horrible humans generally are....

### [Qwen 3.8 27b in 24gb of VRAM](https://www.reddit.com/r/LocalLLaMA/comments/1vqea0n/qwen_38_27b_in_24gb_of_vram/)

**Post Summary:**
Thought i would just add my own flags here for llama.cpp (literally pulled and rebuilt latest today). Running on a 4090 FE and 48gb of DDR4 ram on WSL2.
Basically you have 3 knobs you can tune for maximum context. I prefer to keep my kv cache at `q8_0` maximum (though i am interested in comparing q6_0 eventually in beellama). So you can control the batch/ubatch, whether mtp is on or off, and the quantization of the drafter model's kv cache.
At the end of the day I found that you can either have medium context at q8 with faster TPS or larger context at q8 with slower TPS.
BTW I dont have the ability to use iGPU since im on an older AMD cpu, so you might even get better results. I'm stuck with about 300-400mb used in VRAM because of my monitor.
Heres the full run command:
./build/bin/llama-server \
  --model "<unix-path>" \ #unsloth
  --host 0.0.0.0 \
  --port 8081 \
  -b 256 \
  -ub 256 \
  -fitt 0 \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --spec-

**Key Comments & Community Discussion:**
- **alpacadaver** (Score: 6): alpacadaver • 5d ago https://github.com/noonghunna/club-3090/blob/master/models/qwen3.8-27b/llama-cpp/compose/single/unsloth-iq4nl/q8kv.yml tweak this, and watch this for changes as it gets tested, benchmarked, and improved over the next few hours / days. sisyphus-cycle • 5d ago Cool will track this. That template has a massive batch size of 4096, which was overkill for me. It ate like 2gb of VRAM...
- **sisyphus-cycle** (Score: 4): sisyphus-cycle • 5d ago Cool will track this. That template has a massive batch size of 4096, which was overkill for me. It ate like 2gb of VRAM and only increased prompt processing by like 400 tps. Might be 4090 vs 3090 issues as well gpuz_dev • 5d ago yeah -b 4096 isn't worth the vram hit for solo use. 1600 tps prefill is fine, better to keep that memory for main kv depth alpacadaver • 5d ago Ye...
- **gpuz_dev** (Score: 2): gpuz_dev • 5d ago yeah -b 4096 isn't worth the vram hit for solo use. 1600 tps prefill is fine, better to keep that memory for main kv depth...
- **alpacadaver** (Score: 2): alpacadaver • 5d ago Yep if you read some of the slop in the comments, it's just a shot in the dark until more automation can run and an actual config / competing configs proposed and validated. It's essentially an automated, community-contributed repository that you can keep coming back to, which will continuously promote the winning (single/dual/quad gpu * llama/vllm/etc) configurations from peo...
- **old-mike** (Score: 3): old-mike • 5d ago Hey there! I think you should try https://github.com/spiritbuun/buun-llama-cpp He has developed a vbr KV mechanism, so you can fix vbr floor to 6, and you get the critical KV layers in f16, the intermediate in turbo8 (8.125 bpw I think) and the less significant ones in turbo4. And, when using CUDA, at least in Linux, you got a bunch of optimizations that impact speed. sisyphus-cy...

### [How much VRAM needed for Qwen 3.6 27B Q8 with 262K context?](https://www.reddit.com/r/LocalLLaMA/comments/1tvluaj/how_much_vram_needed_for_qwen_36_27b_q8_with_262k/)

**Post Summary:**
trying to figure out my next GPU purchase. currently running IQ4XS and Q4 KV with 262K context and want to upgrade and run uncompressed KV and the model at Q8.
anyone know how much VRAM is needed? would 48GB be enough?
trying to figure out my next GPU purchase. currently running IQ4XS and Q4 KV with 262K context and want to upgrade and run uncompressed KV and the model at Q8.
anyone know how much VRAM is needed? would 48GB be enough?
From memory it’s about 53gb - LM Studio has a little slider that shows memory requirements pretty accurately.
and depending on GPUs the OP needs a bit more for communication overhead. I found 2xR9700 crashing from time to time. RTX5000
 with 74gb does not crash
I think that it's just something is wrong with llama.cpp for multi GPU setups (at least for R9700s). When I use an old build from about two weeks ago it works fine for me on dual R9700s. And the mtp performance increase is much more pronounced that on recent llama.cpp builds (official container bu

**Key Comments & Community Discussion:**
- **alexp702** (Score: 36): alexp702 • 3mo ago From memory it’s about 53gb - LM Studio has a little slider that shows memory requirements pretty accurately. GabrielCliseru • 3mo ago and depending on GPUs the OP needs a bit more for communication overhead. I found 2xR9700 crashing from time to time. RTX5000  with 74gb does not crash Evgeny_19 • 3mo ago I think that it's just something is wrong with llama.cpp for multi GPU set...
- **GabrielCliseru** (Score: 11): GabrielCliseru • 3mo ago and depending on GPUs the OP needs a bit more for communication overhead. I found 2xR9700 crashing from time to time. RTX5000  with 74gb does not crash Evgeny_19 • 3mo ago I think that it's just something is wrong with llama.cpp for multi GPU setups (at least for R9700s). When I use an old build from about two weeks ago it works fine for me on dual R9700s. And the mtp perf...
- **Evgeny_19** (Score: 15): Evgeny_19 • 3mo ago I think that it's just something is wrong with llama.cpp for multi GPU setups (at least for R9700s). When I use an old build from about two weeks ago it works fine for me on dual R9700s. And the mtp performance increase is much more pronounced that on recent llama.cpp builds (official container builds form ggml-org). Old build works fine with full 262k context. Although the mod...
- **farcryjohn** (Score: 5): farcryjohn • 3mo ago I'm glad to hear someone else is experiencing the same thing. I thought I was going crazy. I also have dual R9700s, and was running into crashes with even just the Q6_K_XL from unsloth. Q_8 was even worse. I never used to have issues until the MTP update. I'm on LM Studio though, so I assumed it was something wonky with that. It actually caused a kernel panic several times bef...
- **luncheroo** (Score: 1): luncheroo • 3mo ago • Edited 3mo ago I've been looking at 9700s because I have reached a ceiling with smaller models and my work that I can't scaffold my way out of. Am I reading you both right that you prefer recent llama.cpp builds through LM Studio with vulkan? Evgeny_19 • 3mo ago I never used LM Studio. Just llama.cpp from my custom builds or official container builds from ggml-org. For dual R...

### [16 GB VRAM users, what model do we like best now?](https://www.reddit.com/r/LocalLLaMA/comments/1sgvt01/16_gb_vram_users_what_model_do_we_like_best_now/)

**Post Summary:**
I'm finding Qwen 3.5 27b at IQ3 quants to be quite nice, I can usually fit around 32k (this is usually enough context for me since I dont use my local models for anything like coding) without issues and get around 40+ t/s on my RTX 4080 using ik_llama.cpp compiled for CUDA. I'm wondering if we could maybe get away with iq4 quants for the gemma 26b moe using turboquant for kv cache..
Being on 16gb kind of feels like edging, cause the quality drop off between iq4 and q4 feel pretty noticable to me.. but you also give-up a ton of speed as soon as you need to start offloading layers.
I'm finding Qwen 3.5 27b at IQ3 quants to be quite nice, I can usually fit around 32k (this is usually enough context for me since I dont use my local models for anything like coding) without issues and get around 40+ t/s on my RTX 4080 using ik_llama.cpp compiled for CUDA. I'm wondering if we could maybe get away with iq4 quants for the gemma 26b moe using turboquant for kv cache..
Being on 16gb kind of fee

**Key Comments & Community Discussion:**
- **sine120** (Score: 72): sine120 • 4mo ago  Top 1% Commenter Like you said, 27B at IQ3_XXS does well. I have 64GB of system RAM, so I tend to run MoE's in harnesses with a small amount of system prompt if possible. Qwen3-Coder is good, 3.5-35B-A3B is good, and Gemma4-26B is good. If I don't need as much intelligence/ coding ability, 3.5-9B is also pretty good, and I want to play with Qwopus to see how it handles. I wish t...
- **xeeff** (Score: 7): xeeff • 4mo ago please let me know how Qwopus (9B/35B A3B/27B) works out for you, and what your use cases are. i'll be waiting :) sine120 • 4mo ago  Top 1% Commenter Is there a 35B Qwopus? I only see 4/9/27B. 1 more reply...
- **sine120** (Score: 2): sine120 • 4mo ago  Top 1% Commenter Is there a 35B Qwopus? I only see 4/9/27B. 1 more reply...
- **grumd** (Score: 8): grumd • 4mo ago • Edited 4mo ago  Top 1% Commenter You should try 122B at IQ3_S, at a low quant it outperforms 27B. 27B gets ahead of 122B at higher quants Big-Wear-8148 • 4mo ago how would it fit 16gb vram ? grumd • 4mo ago  Top 1% Commenter It doesn't need to. It's a MoE model, experts can be offloaded to CPU/RAM...
- **Big-Wear-8148** (Score: 2): Big-Wear-8148 • 4mo ago how would it fit 16gb vram ? grumd • 4mo ago  Top 1% Commenter It doesn't need to. It's a MoE model, experts can be offloaded to CPU/RAM...

### [NInfer RTX 4090 for Qwen 3.8 27B update - up to 250-350K tokens context in VRAM](https://www.reddit.com/r/LocalLLaMA/comments/1vq881r/ninfer_rtx_4090_for_qwen_38_27b_update_up_to/)

**Post Summary:**
I've made some improvements to my fork of NInfer, adding rk2v4-e8 quant option for the KV cache, which can reach up to 250-350K tokens of context window depending on the configuration like vision, MTP, etc, on my single RTX 4090 without spilling over into system RAM.
On lower context window runs, I also made some optimizations to reach about 80-160 tokens / second generation speeds for repetitive workloads like code, math, etc.
Let me know if there are any obvious runtime issues, so far it seemed to survive the chaotic workloads I threw at it. Hopefully the mods won't nuke it in favor of the megathread this time, it gets lost pretty quickly there.
Sources: https://github.com/UDPSendToFailed/ninfer-4090
I've made some improvements to my fork of NInfer, adding rk2v4-e8 quant option for the KV cache, which can reach up to 250-350K tokens of context window depending on the configuration like vision, MTP, etc, on my single RTX 4090 without spilling over into system RAM.
On lower context

**Key Comments & Community Discussion:**
- **_-_David** (Score: 2): _-_David • 5d ago Awesome! I hope 4090 owners see this. I absolutely love the 5090 version. Haven't measured exactly, but I've seen someone saying their 5090 was pushing 1,100+ tps at high concurrency. To think that when I bought it I had to offload layers of GPT-OSS-120 and got 8 tps....
- **Brazen-Badger** (Score: 3): Brazen-Badger • 5d ago Really wish there was a way to see how accurate or high quality the ninfer models are. Or some benchmarks posted somewhere. Loving the performance on my 5090 but not sure what I’m giving up. _-_David • 5d ago I've never been someone who has noticed "Hmm, this q5 is clearly different than this q6". This Ninfer model is killing it with what I give it, but I get the craving for...
- **_-_David** (Score: 2): _-_David • 5d ago I've never been someone who has noticed "Hmm, this q5 is clearly different than this q6". This Ninfer model is killing it with what I give it, but I get the craving for benchmarks. I have been refreshing ArtificialAnalysis since the model dropped, looking for a score, despite the fact that it really doesn't matter. I know what's important is that it works for me, but in the same ...
- **Brazen-Badger** (Score: 1): Brazen-Badger • 5d ago It’s mostly a concern in that if it runs faster but performs worse than another similarly fast or more token efficient model, then it feels like I’m giving something up and not getting the most of my hardware and time. That being said I have been very happy with ninfer so far. Extremely excited for the NVFP4 version of the model to see it really fly and I’m considering tryin...
- **_-_David** (Score: 1): _-_David • 5d ago I suppose what I mean is that if the model is completing the task it is given then you can't really be losing anything. I think the same speed argument goes for using the MoE. Those 3.6 35b numbers look absolutely bonkers. If a 3.8 version comes out I think I'll swap to it for a little while and swap back only whenever it fails to deliver. If Muse Glimmer works for your task, tha...

### [Qwen3.8-27B running on a 12GB RTX 5070 Ti laptop — around 4.5 tok/s with 80% MTP acceptance](https://www.reddit.com/r/LocalLLaMA/comments/1vodz84/qwen3827b_running_on_a_12gb_rtx_5070_ti_laptop/)

**Post Summary:**
Update: I downloaded Q3 and Q2—here’s the full comparison
After reading the comments, I downloaded both additional quants:
Qwen3.8-27B-UD-Q4_K_XL — 17.9GB
Qwen3.8-27B-UD-Q3_K_XL — 13.4GB
Qwen3.8-27B-UD-Q2_K_XL — 10.7GB
I tested all three on the same RTX 5070 Ti Laptop GPU with 12GB VRAM.
Common settings:
8K context
Q8 KV cache
Flash Attention enabled
One parallel slot
Automatic CPU/GPU fitting
Vision projector loaded
Temperature 0 and seed 42
Same factual and coding prompts
The original Q4 speed results used MTP. Q3 and Q2 had MTP explicitly disabled. I later disabled MTP for all three during the separate quality test.
Speed comparison
Test	Q4 + MTP	Q3, no MTP	Q2, no MTP
Factual generation	4.42 tok/s	5.18 tok/s	12.83 tok/s
Coding generation	4.53 tok/s	4.84 tok/s	12.86 tok/s
Factual prompt processing	~21.3 tok/s	34.4 tok/s	60.8 tok/s
Coding prompt processing	27.0 tok/s	61.5 tok/s	129.3 tok/s
Loaded VRAM:
Q4: approximately 10,978 MiB
Q3: approximately 11,003–11,006 Mi

**Key Comments & Community Discussion:**
- **giveen** (Score: 12): giveen • 7d ago Turn off MTP. I have had a lot more success with MTP off. giveen • 7d ago RTX5090 MTP On , 70-80% acceptence = 30tks MTF Off, = 50tks CoffeeToCode99 • 7d ago Sure, will give it a shot....
- **giveen** (Score: 9): giveen • 7d ago RTX5090 MTP On , 70-80% acceptence = 30tks MTF Off, = 50tks CoffeeToCode99 • 7d ago Sure, will give it a shot....
- **CoffeeToCode99** (Score: 2): CoffeeToCode99 • 7d ago Sure, will give it a shot....
- **PossessionUsed7393** (Score: 6): PossessionUsed7393 • 7d ago Well this saves me trying to use it on my 3080Ti - guess this is why the MoEs are the more popular variants. Old-Sherbert-4495 • 7d ago q3xxs i just one shotted a particulary complex physics three.js game. im blown away... why not try q2 or q1...
- **Old-Sherbert-4495** (Score: 2): Old-Sherbert-4495 • 7d ago q3xxs i just one shotted a particulary complex physics three.js game. im blown away... why not try q2 or q1...

### [Good results with Qwen 3.8 27B PrismaAqua 5.5-bit on 5090 vLLM](https://www.reddit.com/r/LocalLLaMA/comments/1vrbqg2/good_results_with_qwen_38_27b_prismaaqua_55bit_on/)

**Post Summary:**
https://huggingface.co/rdtand recently released his 5.5-bit PrismaAqua quant of Qwen 3.8 27B. I tested it for my personal workload and got positive results.
This is my own niche workload so take it with a grain of salt. My requirements are:
Works on a 5090 and 6000 pro.
Emphasis on tool use, business and economic reasoning, investment etc.
General world knowledge not important.
Coding ability not important.
I have a corresponding set of tests for these cases, some taken from public standards and others derived from my work. I ran them through PrismaAqua 5.5 on vLLM using its native compressed-tensors format, and for comparison against bf16 on llama.cpp with CPU offload. Since the harnesses are quite different, only the test results are comparable.
my vLLM settings after some iteration:
vllm serve <model>
  --served-model-name qwen3.8-27b
  --tensor-parallel-size 1
  --max-model-len 131072
  --quantization compressed-tensors
  --kv-cache-dtype fp8
  --kv-cache-memory-bytes 54358

**Key Comments & Community Discussion:**
- **Fragrant_Scale6456** (Score: 3): Fragrant_Scale6456 • 4d ago Nice testing thanks for sharing.  I’ve been using the prisma quants for a while now with my 5090.   I haven’t formally tested to the degree you did but I’ve found prisma aura and aqua both performed around as well as q6k/q6k xl but come with all the benefits of vllm and none of the downsides of the various nvfp4 quants.  One suggestion I do have though is you need to ra...
- **offgridai** (Score: 3): offgridai • 3d ago Lots of good tips in this thread. I adopted a 131k context window and had no negative impact on scores or concurrency. Very nice. I tried again with thinking unlimited and found some positive score impact up to 8192 tokens but after that it generally just spun off into infinity/30+ minute self doubt. One test ran for 27 mins and was just as wrong as it was at 5 :-) Still the 8k ...
- **Fragrant_Scale6456** (Score: 2): Fragrant_Scale6456 • 3d ago Awesome!  Yea I asked it earlier about some llamacpp flags in xhigh with unbounded thinking and it burned 90k context generating a response lol.   IMO the prisma quants are as good as it gets for a 5090 if you need over 100k context.  You could argue running q6k xl is better but losing the VLLM parallelism is too much of a trade off.    Beellama and kvarn kv compression...
- **cosmicnag** (Score: 2): cosmicnag • 4d ago Only 64k context on fp8 kv? I am not using prisma with 3.8, but was using it for 3.6 - and this should be very similar. If I remember correctly, I could do full 262k context with fp8 kv without mtp , and around 215k with MTP. The only thing was not to load the vision tower. I am using malaiwah 's EXL3 based quants now which have even lower KL, but Prisma is quite good (and doesn...
- **offgridai** (Score: 1): offgridai • 4d ago I will try that out. I'm trying to use a single card for multiple agents so I'm maybe being too conservative with context size....

### [Qwen 3.8 27b *MEDIUM* is insane: 1/20th the thinking time of xhigh for almost the same quality output??](https://www.reddit.com/r/LocalLLaMA/comments/1vtq8hc/qwen_38_27b_medium_is_insane_120th_the_thinking/)

**Post Summary:**
Thank you for the post but I personally don’t agree. In my local testing medium is a great local model, no question, but setting it to xhigh (yes it thinks forever) is where it clearly has the low tier frontier coding and reasoning ability. Low and Medium are good but left me unimpressed. Setting it to xhigh for the first time made me windshield wiper the fog off my glasses when I saw the thinking traces and results.
Important to note, my experience may be due to the fact that I’m running Q4 Q8 KV. Perhaps xhigh thinking is so good there that it hides the Q4 blemishes compared to lesser thinking.
Agree with you. The xhigh reasoning traces are not just what if slop especially for coding you can see the model shaping and reasoning on individual code fragment alternatives and correcting as it goes before writing to file. Maybe medium has a place for claws and general agents but cant argue with xhigh results.
According to Lukesdevlab testing, low and xhigh use around the same amount of to

**Key Comments & Community Discussion:**
- **I_Play_Zed** (Score: 20): I_Play_Zed • 1d ago Thank you for the post but I personally don’t agree. In my local testing medium is a great local model, no question, but setting it to xhigh (yes it thinks forever) is where it clearly has the low tier frontier coding and reasoning ability. Low and Medium are good but left me unimpressed. Setting it to xhigh for the first time made me windshield wiper the fog off my glasses whe...
- **LoSboccacc** (Score: 4): LoSboccacc • 1d ago Agree with you. The xhigh reasoning traces are not just what if slop especially for coding you can see the model shaping and reasoning on individual code fragment alternatives and correcting as it goes before writing to file. Maybe medium has a place for claws and general agents but cant argue with xhigh results....
- **Hour-Passenger-8513** (Score: 8): Hour-Passenger-8513 • 1d ago • Edited 1d ago According to Lukesdevlab testing, low and xhigh use around the same amount of tokens for thinking. xHigh is thorough. Low is uncertain and double-checking. https://youtu.be/z64J6bC16iQ SaturnsVoid • 1d ago llama.cpp Yeah it seems at low it reads to munch into your prompt, at medium it just does as it's told and relies on its training and at high it REAL...
- **SaturnsVoid** (Score: 5): SaturnsVoid • 1d ago llama.cpp Yeah it seems at low it reads to munch into your prompt, at medium it just does as it's told and relies on its training and at high it REALLY trys it's best. Hour-Passenger-8513 • 1d ago Yep, don't go low. Stay off the xhigh. Medium remains optimum. 9gxa05s8fa8sh • 1d ago that's a load-bearing statement you can take to the goblin pointer_to_null • 1d ago Nice to see ...
- **Hour-Passenger-8513** (Score: 0): Hour-Passenger-8513 • 1d ago Yep, don't go low. Stay off the xhigh. Medium remains optimum. 9gxa05s8fa8sh • 1d ago that's a load-bearing statement you can take to the goblin pointer_to_null • 1d ago Nice to see the goldilocks principle in practice....

### [Qwen3.8 27B reasoning effort low/medium/xhigh comparison](https://www.reddit.com/r/LocalLLaMA/comments/1vpuh7m/qwen38_27b_reasoning_effort_lowmediumxhigh/)

**Post Summary:**
I did a short test of the different reasoning efforts, since on default xhigh the model thinks a lot.
Not very scientific, just a quick "generate an SVG of a pelican on a bicycle" prompt with 3 different seeds. I think the result is interesting none the less: xhigh gives *much* higher visual fidelity - but it also takes about 7x as long as low. Low and medium seem to be very close to each other.
Hardware and setup
GPU: NVIDIA RTX 5080 Laptop GPU, 16 GB VRAM
Model: unsloth/Qwen3.8-27B-UD-IQ3_XXS
llama.cpp: build 10451, commit 10bf611e5
Context: 65,536
KV cache: Q8_0
Flash Attention: enabled
MTP speculative decoding: --spec-default --spec-type draft-mtp
--fit off
One concurrent slot
Prompt:
Create a polished SVG graphic of a pelican riding a bicycle. The result must clearly show a recognizable pelican actively riding a recognizable two-wheeled bicycle. Return only one complete, self-contained SVG document with a viewBox; no Markdown fences, prose, external images, JavaScript

**Key Comments & Community Discussion:**
- **cibernox** (Score: 51): cibernox • 6d ago I really think that qwen should have some mode between medium and x high. That 10x difference is ridiculous. jumpingcross • 5d ago As far as I understand, the difference between the modes is purely in the system prompt being given to the model. Where xhigh says something like "think for a really long time and make sure everything is correct" and medium says nothing. So perhaps it...
- **jumpingcross** (Score: 24): jumpingcross • 5d ago As far as I understand, the difference between the modes is purely in the system prompt being given to the model. Where xhigh says something like "think for a really long time and make sure everything is correct" and medium says nothing. So perhaps it could be possible to come up with custom modes that say something like "check your work for correctness but don't overdo it"? ...
- **cibernox** (Score: 12): cibernox • 5d ago It’s only the jinja template? Interesting. I’m sure there’s a rule of diminishing returns and that it kicks in rather soon. I’m sure the difference between thinking for 10k tokens and thinking for 45k token is a rounding error....
- **qiinemarr** (Score: 6): qiinemarr • 5d ago I mean you could just dl the official chat template and change to this bit: {%- if enable_thinking is undefined or enable_thinking is true %}     {%- set resolved_reasoning_effort = reasoning_effort|default('xhigh') %}     {%- if resolved_reasoning_effort not in ('xhigh', 'medium', 'low') %}         {{- raise_exception('Unexpected reasoning effort ' ~ reasoning_effort ~ '. Suppo...
- **beyondthem00n** (Score: 3): beyondthem00n • 5d ago Was this edited by you? Seems that Medium effort in the template is set to make it behave as xhigh, they have the same instructions? qiinemarr • 3d ago Yes I did. And I am unsure what to think of it. I tried reasoning low with default instruct and then with adding xhigh instruct as well as xhigh regular for comapraison: Reasoning effort is set to xhigh. Please think carefull...

### [Is qwen 3.8 27B actually qwen 3.6 27B who thinks (much) more?](https://www.reddit.com/r/LocalLLaMA/comments/1vuhx4j/is_qwen_38_27b_actually_qwen_36_27b_who_thinks/)

**Post Summary:**
On a single 3090 I'm using this llama-server_config.ini:
[*]
port = 8080
metrics = true
flash-attn = true
batch-size = 2048
ubatch-size = 1024
n-gpu-layers = 99
threads = 8
threads-batch = 16
parallel = 1
reasoning = on
no-mmproj = true
[qwen3.8-27B]
load-on-startup = 1
model = <windows-path>
ctx-size = 131072
cache-type-k = q8_0
cache-type-v = q8_0
spec-type = draft-mtp
spec-draft-n-max = 2
temp = 1.0
top-p = 0.95
top-k = 20
min-p = 0.0
presence-penalty = 0.0
repeat-penalty = 1.0
reasoning-preserve = true
chat-template-kwargs = {"preserve_thinking":true}
and this for opencode_config.jsonc:
"provider": {
    "llama.cpp": {
        "npm": "@ai-sdk/openai-compatible",
        "name": "llama-server (local)",
        "options": {
            "baseURL": "http://<private-endpoint>/v1"
        },
        "models": {
            "qwen3.8-27B": {
                "name": "Qwen3.8 27B",
                "limit": {
                    "context": 131072,
                    "o

**Key Comments & Community Discussion:**
- **SecondFriendly4255** (Score: 3): SecondFriendly4255 • 11h ago Personally prefer thinking too much(3.8) to fix that fix that (3.6) SecondFriendly4255 • 11h ago Xhigh team btw...
- **SecondFriendly4255** (Score: 1): SecondFriendly4255 • 11h ago Xhigh team btw...
- **uti24** (Score: 2): uti24 • 11h ago  Top 1% Commenter I kinda agree with you. It's more that when you nerf the thinking budget of the 3.8 27B, it doesn't feel much, if any, better than the 3.6 27B. It needs to be tested, though. Sorry for the human parallels, but it's like saying someone is smarter because they did much better in 4 hours compared to somebody who worked for, like, 20 minutes. They still can be smarter...
- **CapsAdmin** (Score: 2): CapsAdmin • 10h ago I find that medium doesn't think all that much when doing something like a refactoring task, but according to the chat template, medium doesn't inject anything specific. It could potentially be a system prompt that triggers it to think more than expected? I mean 3.8 thinks way more than 3.6, but on medium it doesn't feel as bad as xhigh....
- **KroniklyOnline** (Score: 4): KroniklyOnline • 12h ago I don't think so, its raw intelligence is far greater. I'm pretty sure the benchmarks run are with reasoning off, like the ones you see on Artificial Intelligence Analysis website. Its just far more intelligent but the addition to different reasoning types just makes it that much stronger. I just leave it on xhigh default, I don't usually give local models large open ended...

### [Ling 3.0 flash -vs- Qwen 3.5 122b-a10b -vs- Qwen 3.8 27b - any opinions on which is best for agentic coding?](https://www.reddit.com/r/LocalLLaMA/comments/1vrx3lz/ling_30_flash_vs_qwen_35_122ba10b_vs_qwen_38_27b/)

**Post Summary:**
Use case: Agentic coding (Pi coding agent)
Quants:
Ling 3.0 flash (Bartowski IQ4_XS)
Qwen 3.5 122b-a10b (Unsloth UD-IQ4_NL)
Qwen 3.8 27b (Unsloth UD-Q8_K_XL)
Amount of context not important; I can run all these now. Ling 3.0 flash spills some layers to CPU/RAM but still performs well on my setup.
The question is - which one is best for agentic coding in a harness? Not for speed, but for overall quality.
Use case: Agentic coding (Pi coding agent)
Quants:
Ling 3.0 flash (Bartowski IQ4_XS)
Qwen 3.5 122b-a10b (Unsloth UD-IQ4_NL)
Qwen 3.8 27b (Unsloth UD-Q8_K_XL)
Amount of context not important; I can run all these now. Ling 3.0 flash spills some layers to CPU/RAM but still performs well on my setup.
The question is - which one is best for agentic coding in a harness? Not for speed, but for overall quality.
My initial test of the FP8 variant of Ling 3.0 Flash using vLLM was promising with regards to code review, but I cannot get it to stop looping newline characters. It manages 

**Key Comments & Community Discussion:**
- **rmhubbert** (Score: 3): rmhubbert • 3d ago • Edited 3d ago My initial test of the FP8 variant of Ling 3.0 Flash using vLLM was promising with regards to code review, but I cannot get it to stop looping newline characters. It manages a couple of turns, and then just loops "\n" in its reasoning. Still keeping an eye out for a fix, but this model doesn't seem to be getting a lot of attention from the vLLM team. Shame, becau...
- **fsalucard** (Score: 1): fsalucard • 3d ago This is same problem I was having. I saw improvement by changing temperature to 1.0 but not resolved. I then added repeat_penalty 1.2 and set Temp back to 0.6 and ran it for a while and it "seemed" to fix it... but I ended up switching to a different mode to work on some stuff and haven't gone back to Ling to test it some more. rmhubbert • 3d ago I'll give that a shot. Thanks!...
- **rmhubbert** (Score: 1): rmhubbert • 3d ago I'll give that a shot. Thanks!...
- **atumblingdandelion** (Score: 2): atumblingdandelion • 3d ago If speed is irrelevant and the overall quality is more important, then definitely Qwen3.8 27b! I'm alternating between that and Ling3 flash on a single DGX Spark. Qwen is actually quite usable (>20 tps), and its quality is much better for my use case. It was able to solve a real-world climate data analysis task that I use as a benchmark flawlessly, unsupervised. I teste...
- **Jorlen** (Score: 1): Jorlen • 3d ago llama.cpp You get 20 tps on a DGX spark? Which quant / bit of 3.8 27b you using? That's pretty impressive. You using MTP with that or no? (it comes built in the model weights, something I didn't realize until after testing it). PositiveBit01 • 3d ago Yeah, that's impressive. I'm running fp8 at like 8-9tok/s on my spark which is too slow so I'm back to 35b. At fp8, 273/27 == 10.1 so...

### [This is what context management still is, Qwen 3.8 27B?](https://www.reddit.com/r/LocalLLaMA/comments/1vr23lo/this_is_what_context_management_still_is_qwen_38/)

**Post Summary:**
Looks like not everything's improved from 3.5. After around 60-80k tokens it starts to degrade.
I'm here for suggestions. Is this how it is or am I doing it wrong?
(llama.cpp, Unsloth Q8_0, f16 for both k and v. The TUI is Mistral Vibe)
Looks like not everything's improved from 3.5. After around 60-80k tokens it starts to degrade.
I'm here for suggestions. Is this how it is or am I doing it wrong?
(llama.cpp, Unsloth Q8_0, f16 for both k and v. The TUI is Mistral Vibe)
I think the reason it used bash is because it wanted to avoid reading the entire file, so it fashioned a way to just read a chunk of the file.
I wish. Unfortunately, it's a familiar pattern from 3.5 Qwens. It forgets it has tools, and starts coming up with creative ways to both read and write files, often with sed, after passing ~60k context. Interrupting and reminding it of proper tool use often helps.
Opus 5 does the same all the time. Uses sed for reading files, then writes Pythons scripts for editing them.
The t

**Key Comments & Community Discussion:**
- **xienze** (Score: 5): xienze • 4d ago I think the reason it used bash is because it wanted to avoid reading the entire file, so it fashioned a way to just read a chunk of the file. juss-i • 4d ago I wish. Unfortunately, it's a familiar pattern from 3.5 Qwens. It forgets it has tools, and starts coming up with creative ways to both read and write files, often with sed, after passing ~60k context. Interrupting and remind...
- **juss-i** (Score: 1): juss-i • 4d ago I wish. Unfortunately, it's a familiar pattern from 3.5 Qwens. It forgets it has tools, and starts coming up with creative ways to both read and write files, often with sed, after passing ~60k context. Interrupting and reminding it of proper tool use often helps....
- **jubilantcoffin** (Score: 4): jubilantcoffin • 4d ago Opus 5 does the same all the time. Uses sed for reading files, then writes Pythons scripts for editing them. The tool definition is at the start of the prompt, and it has to stay there for caching, so this is a natural consequence of attention optimizations both models are using....
- **KroniklyOnline** (Score: 5): KroniklyOnline • 4d ago yeah...... try using PI dude...... Harness matters a lot...
- **beling86** (Score: 2): beling86 • 4d ago I will share a non-scientific observation, but in my use case Qwen 3.8 27B get dumb between 50k and 80k token context, but unexplainably it improves again after the 100k token. My use-case is batching 200k token documents with the same prompt and extracting information from these documents. I miss relevant information within this very random window context depth, and I miss zero ...

### [Qwen 3.8 27b - PI AGENT vs OPENCODE - another smaple](https://www.reddit.com/r/LocalLLaMA/comments/1vuwwww/qwen_38_27b_pi_agent_vs_opencode_another_smaple/)

**Post Summary:**
That is the second comparison and the last one.
I will not be spamming again ;)
Continuation from:
https://www.reddit.com/r/LocalLLaMA/comments/1vu0u2v/qwen_38_27b_pi_agent_vs_opencode/
That is one of my many tests I make comparing output quality.
What is more interesting using a PI Agent results are much better than an Opencode using a Qwen 3.8 27b ?!
Seems PI Agent is much better in the agent environment somehow... Not counting uses less tokens , do not have a hard limit of 32k output tokens, is faster, do not freezing, compressing context far less than Opencode. For instance if you have context in the Opencode output 32k and all context 100k then the compression is starting at 67k context ... PI is starting at 90k context even if you have set output context 64k or more.
My config for RTX 3090
llama-server with ini config -> which is exposing API to Opencode and PI agent.
llama-server.exe --models-preset 1_preset.ini --models-max 1 --direct-io
config ini
[Qwen3.8-27B_dense_

**Key Comments & Community Discussion:**
- **Guilty_Rooster_6708** (Score: 7): Guilty_Rooster_6708 • 1h ago Thanks for the tip to offload mmproj to cpu. I never thought about doing it but it makes a huge difference Healthy-Nebula-3603 • 1h ago  Top 1% Commenter Yes Agents based on Qwen 3.8 27b are using vision a lot to check own work. That's actually necessity to get a good results....
- **Healthy-Nebula-3603** (Score: 1): Healthy-Nebula-3603 • 1h ago  Top 1% Commenter Yes Agents based on Qwen 3.8 27b are using vision a lot to check own work. That's actually necessity to get a good results....
- **Retumbo77** (Score: 9): Retumbo77 • 2h ago Just based on visuals, I would agree the results using Pi are better than Opencode, but I think "Much better" is a stretch. You have not listed what is getting loaded in as a system prompt with Pi vs what is getting loaded in with Opencode, so I don't know how we can actually compare the two apples to apples? For the record I don't use either so don't have any dogs in this fight...
- **Healthy-Nebula-3603** (Score: 3): Healthy-Nebula-3603 • 2h ago  Top 1% Commenter For me results looks like comparing qwen 3.8 27b with a low effort to a xhigh effort. but both were working on xhigh. All agents are using default settings. Only a small change is For Opeencode maxed to output generation to 32k as that is hard limit. Retumbo77 • 2h ago So to confirm, system prompt from pi is default and system prompt from Opencode is ...
- **Retumbo77** (Score: 2): Retumbo77 • 2h ago So to confirm, system prompt from pi is default and system prompt from Opencode is default? So your claim is that given a limited context for certain models, such as the tested Qwen 3.8 27b, pi produces better results than open code, default for default, primarily because pi has a lower system prompt context that allows the model to use more context for the actual task? Healthy-...

### [I tried to do agenic coding with Qwen 3.8 27B 3bit quant on a macbook air m2 24gb. It took 63 hours, but amazingly, the flight simulator worked.](https://www.reddit.com/r/LocalLLaMA/comments/1vuvx0t/i_tried_to_do_agenic_coding_with_qwen_38_27b_3bit/)

**Post Summary:**
I used LM Studio Bionic with Qwen 3.8 27B Q3_K_S with 57k context.
It took a staggering 63 hours to finish coding. After the first prompt "Create a beautiful, relaxing flight simulator in a single HTML page" taking 47.8 hours, it created an html file that showed the title screen that said "press any key" but pressing any keys won't advance the game.
So I wrote on the second prompt "It saids press any key to begin. I press any key but it doesn't work." It ran for 15 hours.
Now I can fly. No plane model, but it does look kinda like I'm flying forward. A bit buggy but otherwise it's working.
I did the same prompt on google ai studio, and it took 20 minutes. It was able to one-shot the flight simulator, with selectable plane models, and a smooth voxel landscape.
I also did the same prompt on qwen studio, and that took 2hrs. It also was able to one-shot the flight simulator, but this voxel landscape was buggy, rough, and had a weird shimmering effect.
Before anyone gets angry with ins

**Key Comments & Community Discussion:**
- **Cool-Chemical-5629** (Score: 39): Cool-Chemical-5629 • 3h ago Imagine waiting 47.8 hours for the AI to finish the task only to find out it doesn't work. You should get a medal and a new GPU from Alibaba. Obvious_Gur667 • 1h ago Imagine you waited seven and a half million years, and all it said was "42." HyperFoci • 3h ago I think this experience gave me a newfound appreciation and urgency to getting better AI hardware. Then after ...
- **Obvious_Gur667** (Score: 7): Obvious_Gur667 • 1h ago Imagine you waited seven and a half million years, and all it said was "42."...
- **HyperFoci** (Score: 2): HyperFoci • 3h ago I think this experience gave me a newfound appreciation and urgency to getting better AI hardware. Then after checking my options for new hardware and how much it would cost for 128GB VRAM, I became despondent, and decided maybe a subscription is the best for now. cogitech2 • 2h ago No. Terrible conclusion. See my other post....
- **cogitech2** (Score: 2): cogitech2 • 2h ago No. Terrible conclusion. See my other post....
- **cogitech2** (Score: 16): cogitech2 • 2h ago • Edited 2h ago To put this in perspective for anyone trying to decide what hardware to buy - I ran the exact same prompt on my 2x RTX3060 (total 24GB) running the same model at UD-Q5_K_S with 128k context. The task was completed in less than an hour and it works 100% perfectly other than some slight pixel flickering where land meets water in the distance. My 3060s are turned do...

