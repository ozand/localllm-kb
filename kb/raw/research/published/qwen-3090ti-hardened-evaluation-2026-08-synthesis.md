---
id: "raw-reddit-qwen-3090ti-hardened-evaluation-2026-08-synthesis"
category: "raw-research-synthesis"
title: "Reddit research synthesis: Qwen local LLM deployment and RTX 3090 Ti optimization"
capture_date: "2026-08-22"
run_id: "qwen-3090ti-hardened-evaluation-2026-08"
source_count: 39
evidence_status: "community-synthesis-unverified"
tags: [reddit, deep-research, synthesis]
---

# Reddit research synthesis: Qwen local LLM deployment and RTX 3090 Ti optimization

> This document summarizes community evidence only. It intentionally does not promote observations to verified facts without primary-source or local-validation receipts.

## Coverage

- Selected Reddit sources: `50`
- Successfully captured: `50`
- Included at quality score >= `0.5`: `39`
- Failed or pending selected sources: `0`
- Saturation: `false` — not recorded

## Evidence inventory

The following sources passed the deterministic inclusion threshold. Claims still require manual clustering and verification; the renderer does not infer consensus from raw text.

- [Can you run actually useful LLMs on anything less than 3090 ?](https://www.reddit.com/r/LocalLLaMA/comments/1sl3ztq/can_you_run_actually_useful_llms_on_anything_less/) — quality `0.883`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1sl3ztq-can-you-run-actually-useful-llms-on-anything-less-than-3090.json`
- [After pushing 1M+ tokens through Qwen 3.8 27B, here is my optimal llama.cpp config for 16GB VRAM (73k Context, Agentic Coding)](https://www.reddit.com/r/LocalLLaMA/comments/1vqrt86/after_pushing_1m_tokens_through_qwen_38_27b_here/) — quality `0.883`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vqrt86-after-pushing-1m-tokens-through-qwen-3-8-27b-here-is-my-optimal-llama-cpp-config.json`
- [Luce DFlash: Qwen3.6-27B at up to 2x throughput on a single RTX 3090](https://www.reddit.com/r/LocalLLaMA/comments/1sx8uok/luce_dflash_qwen3627b_at_up_to_2x_throughput_on_a/) — quality `0.883`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1sx8uok-luce-dflash-qwen3-6-27b-at-up-to-2x-throughput-on-a-single-rtx-3090.json`
- [Qwen3.8-27B at 262K context on a Strix Halo + RTX 3090 Ti: 9.5 -> 153 tok/s, and it beats a dual-3090 vLLM box on HumanEval](https://www.reddit.com/r/LocalLLaMA/comments/1vu7yce/qwen3827b_at_262k_context_on_a_strix_halo_rtx/) — quality `0.844`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vu7yce-qwen3-8-27b-at-262k-context-on-a-strix-halo-rtx-3090-ti-9-5-153-tok-s-and-it-bea.json`
- [Computer build using Intel Optane Persistent Memory - Can run 1 trillion parameter model at over 4 tokens/sec](https://www.reddit.com/r/LocalLLaMA/comments/1taeg8h/computer_build_using_intel_optane_persistent/) — quality `0.844`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1taeg8h-computer-build-using-intel-optane-persistent-memory-can-run-1-trillion-parameter.json`
- [RTX 5070 Ti + 9800X3D running Qwen3.6-35B-A3B at 79 t/s with 128K context, the --n-cpu-moe flag is the most important part.](https://www.reddit.com/r/LocalLLaMA/comments/1sor55y/rtx_5070_ti_9800x3d_running_qwen3635ba3b_at_79_ts/) — quality `0.844`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1sor55y-rtx-5070-ti-9800x3d-running-qwen3-6-35b-a3b-at-79-t-s-with-128k-context-the-n-cp.json`
- [Qwen3.8-27B on an RTX 5060 Ti 16GB: IQ4 vs Q8, 64K context, MTP, vision, and agent benchmarks](https://www.reddit.com/r/LocalLLaMA/comments/1vupiyh/qwen3827b_on_an_rtx_5060_ti_16gb_iq4_vs_q8_64k/) — quality `0.844`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vupiyh-qwen3-8-27b-on-an-rtx-5060-ti-16gb-iq4-vs-q8-64k-context-mtp-vision-and-agent-be.json`
- [3 days benchmarking most llama.cpp flags on my weird 40gb vram laptop + tb4 egpu setup. Got +70% generation, +40% prefill, 60k more context, and filed a bug in llama around MTP. What I learned.](https://www.reddit.com/r/LocalLLaMA/comments/1vtc0z7/3_days_benchmarking_most_llamacpp_flags_on_my/) — quality `0.844`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vtc0z7-3-days-benchmarking-most-llama-cpp-flags-on-my-weird-40gb-vram-laptop-tb4-egpu-s.json`
- [I pushed Qwen3.8-27B limits again... Dflash2 - 134 tps on a RTX 3090](https://www.reddit.com/r/LocalLLaMA/comments/1vsy4l2/i_pushed_qwen3827b_limits_again_dflash2_134_tps/) — quality `0.844`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vsy4l2-i-pushed-qwen3-8-27b-limits-again-dflash2-134-tps-on-a-rtx-3090.json`
- [NVFP4 on VOLTA! Despite being built for Blackwell, I made four 2017 V100s run Qwen 3.8 NVFP4 natively and match my $6000 RTX 5090.](https://www.reddit.com/r/LocalLLaMA/comments/1vsq3zg/nvfp4_on_volta_despite_being_built_for_blackwell/) — quality `0.844`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vsq3zg-nvfp4-on-volta-despite-being-built-for-blackwell-i-made-four-2017-v100s-run-qwen.json`
- [RTX 3090 + 27B model performance issues (llama.cpp) what am I doing wrong](https://www.reddit.com/r/LocalLLaMA/comments/1svlnyk/rtx_3090_27b_model_performance_issues_llamacpp/) — quality `0.844`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1svlnyk-rtx-3090-27b-model-performance-issues-llama-cpp-what-am-i-doing-wrong.json`
- [80 tok/sec and 128K context on 12GB VRAM with Qwen3.6 35B A3B and llama.cpp MTP](https://www.reddit.com/r/LocalLLaMA/comments/1t82zxv/80_toksec_and_128k_context_on_12gb_vram_with/) — quality `0.824`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1t82zxv-80-tok-sec-and-128k-context-on-12gb-vram-with-qwen3-6-35b-a3b-and-llama-cpp-mtp.json`
- [45 tok/s Qwen3.8-27B MTP3 on modded RTX 2080 Ti 22GB with my NInfer port](https://www.reddit.com/r/LocalLLaMA/comments/1vu856v/45_toks_qwen3827b_mtp3_on_modded_rtx_2080_ti_22gb/) — quality `0.806`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vu856v-45-tok-s-qwen3-8-27b-mtp3-on-modded-rtx-2080-ti-22gb-with-my-ninfer-port.json`
- [Dual 3090 setup: 400 pp t/s to 1600 pp t/s on Qwen 3.6 27B... with slightly lower tps.](https://www.reddit.com/r/LocalLLaMA/comments/1vhkln6/dual_3090_setup_400_pp_ts_to_1600_pp_ts_on_qwen/) — quality `0.806`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vhkln6-dual-3090-setup-400-pp-t-s-to-1600-pp-t-s-on-qwen-3-6-27b-with-slightly-lower-tp.json`
- [Qwen 3.8 27B i get 34 tp/s on rtx 3090 llama.ccp](https://www.reddit.com/r/LocalLLaMA/comments/1vof310/qwen_38_27b_i_get_34_tps_on_rtx_3090_llamaccp/) — quality `0.806`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vof310-qwen-3-8-27b-i-get-34-tp-s-on-rtx-3090-llama-ccp.json`
- [Got the DGX Spark - ask me anything](https://www.reddit.com/r/LocalLLaMA/comments/1o7gpr8/got_the_dgx_spark_ask_me_anything/) — quality `0.767`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1o7gpr8-got-the-dgx-spark-ask-me-anything.json`
- [Dual Xeon E5-2696v4 + 512GB RAM + RTX 3090 Ti local LLM for ISP sysadmin work — benchmarks + questions](https://www.reddit.com/r/LocalLLaMA/comments/1shhmjg/dual_xeon_e52696v4_512gb_ram_rtx_3090_ti_local/) — quality `0.754`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1shhmjg-dual-xeon-e5-2696v4-512gb-ram-rtx-3090-ti-local-llm-for-isp-sysadmin-work-benchm.json`
- [PC upgrade question](https://www.reddit.com/r/LocalLLaMA/comments/1vu5q6j/pc_upgrade_question/) — quality `0.754`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vu5q6j-pc-upgrade-question.json`
- [Benchmarked Qwen3.8-27B on 4x RTX 3090](https://www.reddit.com/r/LocalLLaMA/comments/1vr56r1/benchmarked_qwen3827b_on_4x_rtx_3090/) — quality `0.728`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vr56r1-benchmarked-qwen3-8-27b-on-4x-rtx-3090.json`
- [5070 Ti (New) vs 3090 (Used) to pair with 4070 for local LLMs?](https://www.reddit.com/r/LocalLLaMA/comments/1spwk7h/5070_ti_new_vs_3090_used_to_pair_with_4070_for/) — quality `0.716`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1spwk7h-5070-ti-new-vs-3090-used-to-pair-with-4070-for-local-llms.json`
- [I really want DeepSeek V4 to work as a local coding agent, but the tool calling keeps falling apart. Has anyone solved this?](https://www.reddit.com/r/LocalLLaMA/comments/1vtu779/i_really_want_deepseek_v4_to_work_as_a_local/) — quality `0.716`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vtu779-i-really-want-deepseek-v4-to-work-as-a-local-coding-agent-but-the-tool-calling-k.json`
- [Qwen3.5-35B-A3B is a gamechanger for agentic coding.](https://www.reddit.com/r/LocalLLaMA/comments/1rdxfdu/qwen3535ba3b_is_a_gamechanger_for_agentic_coding/) — quality `0.677`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1rdxfdu-qwen3-5-35b-a3b-is-a-gamechanger-for-agentic-coding.json`
- [7 Chinese companies are already shipping H100/H200-class AI chips, most IPO'd in the last 6 months. I mapped all of them.](https://www.reddit.com/r/LocalLLaMA/comments/1udkxde/7_chinese_companies_are_already_shipping/) — quality `0.677`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1udkxde-7-chinese-companies-are-already-shipping-h100-h200-class-ai-chips-most-ipo-d-in.json`
- [Kimi K2 Thinking 1-bit Unsloth Dynamic GGUFs](https://www.reddit.com/r/LocalLLaMA/comments/1ortopy/kimi_k2_thinking_1bit_unsloth_dynamic_ggufs/) — quality `0.677`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1ortopy-kimi-k2-thinking-1-bit-unsloth-dynamic-ggufs.json`
- [I pushed Qwen3.8-27B to 381 tps for a single request on a RTX 3090](https://www.reddit.com/r/LocalLLaMA/comments/1vtup5s/i_pushed_qwen3827b_to_381_tps_for_a_single/) — quality `0.677`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vtup5s-i-pushed-qwen3-8-27b-to-381-tps-for-a-single-request-on-a-rtx-3090.json`
- [PFlash: 10x prefill speedup over llama.cpp at 128K on a RTX 3090](https://www.reddit.com/r/LocalLLaMA/comments/1t0vp3w/pflash_10x_prefill_speedup_over_llamacpp_at_128k/) — quality `0.677`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1t0vp3w-pflash-10x-prefill-speedup-over-llama-cpp-at-128k-on-a-rtx-3090.json`
- [You can now do FP8 reinforcement learning locally! (<5GB VRAM)](https://www.reddit.com/r/LocalLLaMA/comments/1p6k0h2/you_can_now_do_fp8_reinforcement_learning_locally/) — quality `0.664`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1p6k0h2-you-can-now-do-fp8-reinforcement-learning-locally-5gb-vram.json`
- [Which GPU for local LLM inference? 3090 or 5070 Ti](https://www.reddit.com/r/LocalLLaMA/comments/1s916kt/which_gpu_for_local_llm_inference_3090_or_5070_ti/) — quality `0.644`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1s916kt-which-gpu-for-local-llm-inference-3090-or-5070-ti.json`
- [8x RTX Pro 6000 server complete](https://www.reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/) — quality `0.638`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1plwgun-8x-rtx-pro-6000-server-complete.json`
- [What would be the best coding setup for me if I have 2x RTX 3090s?](https://www.reddit.com/r/LocalLLaMA/comments/1u7qam0/what_would_be_the_best_coding_setup_for_me_if_i/) — quality `0.638`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1u7qam0-what-would-be-the-best-coding-setup-for-me-if-i-have-2x-rtx-3090s.json`
- [AirLLM - Recent Updates - with Qwen3.8-27B, Kimi-K3 too](https://www.reddit.com/r/LocalLLaMA/comments/1vtfzjc/airllm_recent_updates_with_qwen3827b_kimik3_too/) — quality `0.637`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vtfzjc-airllm-recent-updates-with-qwen3-8-27b-kimi-k3-too.json`
- [Is a $699 RTX 3090 (24GB) a good entry point for running strong local LLMs?](https://www.reddit.com/r/LocalLLaMA/comments/1ronpwd/is_a_699_rtx_3090_24gb_a_good_entry_point_for/) — quality `0.626`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1ronpwd-is-a-699-rtx-3090-24gb-a-good-entry-point-for-running-strong-local-llms.json`
- [Where to start with my 3090](https://www.reddit.com/r/LocalLLaMA/comments/1vqlkb0/where_to_start_with_my_3090/) — quality `0.626`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vqlkb0-where-to-start-with-my-3090.json`
- [Honest take on running 9× RTX 3090 for AI](https://www.reddit.com/r/LocalLLaMA/comments/1s0p28x/honest_take_on_running_9_rtx_3090_for_ai/) — quality `0.587`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1s0p28x-honest-take-on-running-9-rtx-3090-for-ai.json`
- [Finally finished my LLM server: EPYC 9575F, 4× RTX 3090 (96GB VRAM), 768GB ECC RAM](https://www.reddit.com/r/LocalLLaMA/comments/1tx9tf2/finally_finished_my_llm_server_epyc_9575f_4_rtx/) — quality `0.587`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1tx9tf2-finally-finished-my-llm-server-epyc-9575f-4-rtx-3090-96gb-vram-768gb-ecc-ram.json`
- [RTX 3090 vs M1 Max 64 GB](https://www.reddit.com/r/LocalLLaMA/comments/1vszebu/rtx_3090_vs_m1_max_64_gb/) — quality `0.587`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vszebu-rtx-3090-vs-m1-max-64-gb.json`
- [Single 3090 homies, whats your config for Qwen 3.8 ?](https://www.reddit.com/r/LocalLLaMA/comments/1vpuhov/single_3090_homies_whats_your_config_for_qwen_38/) — quality `0.587`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1vpuhov-single-3090-homies-whats-your-config-for-qwen-3-8.json`
- [RTX 3090 in 2026](https://www.reddit.com/r/LocalLLaMA/comments/1r020dz/rtx_3090_in_2026/) — quality `0.567`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1r020dz-rtx-3090-in-2026.json`
- [Poor man's guide to servicing a used RTX 3090 for local LLM inference](https://www.reddit.com/r/LocalLLaMA/comments/1t0jd95/poor_mans_guide_to_servicing_a_used_rtx_3090_for/) — quality `0.536`, comments/capture in `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/raw/1t0jd95-poor-man-s-guide-to-servicing-a-used-rtx-3090-for-local-llm-inference.json`

## Outbound reference verification

- `unverified`: 578

Top outbound domains:

- `redditinc.com`: 117
- `support.reddithelp.com`: 78
- `discord.gg`: 70
- `github.com`: 55
- `x.com`: 42
- `huggingface.co`: 19
- `docs.unsloth.ai`: 11
- `youtube.com`: 5
- `drive.mfoi.dev`: 5
- `0.0.0.0`: 4
- `c-payne.com`: 2
- `glukhov.org`: 2
- `lmstudio.ai`: 2
- `images2.imgbox.com`: 2
- `store.piffa.net`: 2

## Confirmed facts

- None recorded. Add only facts supported by verified primary sources or local receipts.

## Community observations requiring verification

- Review the included source inventory and cluster repeated claims manually; preserve supporting thread URLs for every observation.

## Identified bottlenecks

- Windows cmd.exe argument quoting caused 32 of 36 planned query records to fail before the surf.cmd fix.
- The current extractor captures navigation/repost chrome in post_body on some pages and captured one Reddit error page with an empty body.
- 578 outbound references were discovered but none were manually verified in this evaluation run.
- The keyword quality score is triage-only and can score a technically relevant question below 0.3 or classify a page shell as zero.

## New hypotheses

- A selector or page-readiness check that rejects Reddit shell/error pages will improve capture validity.
- Separating Reddit post content from navigation/repost chrome will improve synthesis quality and quality scoring.
- A bounded outbound-verification queue should prioritize primary GitHub/Hugging Face/vendor links rather than attempting hundreds of sidebar links.

## Targeted follow-up queries

- `Reddit shreddit-post post-text selector repost chrome extraction`
- `Surf CLI Reddit page readiness error page detection`
- `llama.cpp RTX 3090 Ti benchmark GitHub configuration`
- `Qwen 3.8 27B RTX 3090 Ti verified benchmark`

## Reproducibility artifacts

- `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/run.json`
- `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/queries.json`
- `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/threads.json`
- `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/outbound-references.json`
- `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/errors.jsonl`
- `kb/raw/research/runs/qwen-3090ti-hardened-evaluation-2026-08/follow-up.json`
