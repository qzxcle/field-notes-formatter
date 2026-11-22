# More examples

Published items from the October and November 2026 issues, grouped by section. Use them to match the house style; don't copy their wording.

## Open-Source Models

**INKLING 2 SMALL:** Thinking Machines released the open weights for Inkling 2 Small, a general-purpose multimodal model that accepts text and image inputs and generates text outputs. It is now the #1 US open model and #2 among all open models on Agent Arena. It’s also the most steerable open model on the board, with a median cost of $0.26 per task, about 4.7x cheaper than Kimi K3.1 Pro. [[huggingface](https://huggingface.co/thinkingmachines/Inkling-2-Small)] [[ref](https://x.com/arena/status/2121041107220037972?a=MLkfI9jmD5OEeqOL83Y&s=20)] [12 NOV 2026]

**QWEN4 FAMILY:** Alibaba announced that open weights for smaller Qwen4 models are on the way, alongside the launch of its closed-weight flagship, Qwen4-Max. Built on a new MoE architecture with native vision and a 1M-token context window, Qwen4-Max outperforms Qwen3.8-Max with up to ~50% fewer tokens and cuts average cost per task by 62%. [[ref](https://x.com/Alibaba_Qwen/status/2122148127520289151?a=dp69_EblyKEktBmSW4U&s=20)] [15 NOV 2026]

## Tools & Frameworks

**SAIR FOUNDATION:** SAIR Foundation launched Open Math OS, a research environment for mathematicians built entirely on open-weight models currently available for Kimi K3, DeepSeek V4.1 Flash, and GLM 5.3 Flash. Every project gets its own 24/7 cloud machine with 100+ preinstalled tools, and Ultramath mode sets several agents on one problem in parallel while the mathematician decides what holds. [[ref](https://x.com/SAIRfoundation/status/2111106860468285931?s=20)] [[blog](https://sair.foundation/open-math-model)] [16 OCT 2026]

**HUGGING FACE & OPENROUTER:** Hugging Face and OpenRouter partnered to make open models easier to use, with the former handling storage and the latter inference. Hugging Face’s Inference Providers now route language model requests through OpenRouter’s 80+ providers, choosing the best mix of price, speed, and reliability per call. OpenRouter users can also access Hugging Face’s open weights and store agent traces there to inspect, share, or train on. [[ref](https://x.com/ClementDelangue/status/2122392943957078032?a=1-kG54ew26xUDrjwsDg&s=20)] [16 NOV 2026]

## Policy & Security

**EUROPA:** The European Commission is building EUROPA, the EU’s open frontier model for public authorities, researchers, and businesses across all 24 official EU languages. Domyn, the Milan company chosen to develop the model, ran training trials on JUPITER, Europe’s first exascale supercomputer, which made training 14 times faster. Full training is expected to take about four months. [[ref](https://x.com/IntCyberDigest/status/2122288571579289758)] [16 NOV 2026]

**OPENCODE INCIDENT:** OpenCode suffered a security breach from a large-scale distillation attack that affected 1.4% of its Console users. Ironically, the frontier models the team used for defense started refusing to help, because analyzing the attack triggered their safety guardrails. Meanwhile, the attackers found a way to steal OpenCode users’ API keys to access frontier models from OpenAI, Anthropic, and Google. [[ref](https://x.com/opencode/status/2111519637049319818?s=20)] [[ref2](https://x.com/thdxr/status/2111790511409258796?s=20)] [[ref3](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/)] [18 OCT 2026]

## Podcasts & Media

**ALL-IN PODCAST’S JENSEN OUT:** Jason Calacanis, Chamath Palihapitiya, David Friedberg, and David Sacks discuss why Anthropic’s race toward recursive self-improvement to build a monopoly is “the most dangerous thing” in AI, and how Jensen Huang’s exit as Nvidia CEO affects the open-source movement. [[youtube](https://www.youtube.com/watch?v=Uv2w4VTU-iQ&t=2s)] [13 NOV 2026]

**THE PRAGMATIC ENGINEER WITH SATYA NADELLA:** Gergely Orosz talks with Microsoft CEO Satya Nadella about why every company should own its AI stack instead of relying on a single lab. Nadella sees open-weight models as a way for firms to keep control of their knowledge, pushes for swappable models and local “unmetered intelligence” on laptops, and explains how software engineering is changing as code becomes cheap. [[youtube](https://www.youtube.com/watch?v=0NE89Nzfk20)] [16 NOV 2026]

## What's New at Sentient

**JULIE BELIÃO JOINS SENTIENT FOUNDATION:** Julie Belião, a Google veteran who previously led product development at Mozilla.ai, has joined the Sentient Foundation as VP of Product. With more than 15 years in AI, she’ll lead product strategy through Sentient Labs to turn the team’s open-source AI research into tools developers and organizations can use. [[ref](https://sentient.foundation/news/julie-beliao-sentient-foundation-vp-product)] [10 NOV 2026]

**FINGERPRINTING LEADERBOARD:** Sentient Foundation launched the Fingerprinting Leaderboard, an open benchmark for model provenance methods. Models cost millions to train and minutes to copy, but fine-tuning and distillation can erase where they came from. We built the leaderboard to test tradeoffs: model performance v.s. resistance to fingerprint removal or evasion. 15 schemes already evaluated, submit yours. [[SUBMIT](https://fingerprint.sentient.foundation/)] [14 OCT 2026]

**HELP US UNDERSTAND HOW YOU BUILD WITH AI:** Fill out our 2-minute survey to tell us more about your work and what’s frustrating you right now. If you’re open to a call, we’ll suggest a 30-minute slot. No pitch, no demo. Just a conversation. [[SURVEY](https://forms.gle/2kg95Zsd6VSxznsT6)] [19 NOV 2026]
