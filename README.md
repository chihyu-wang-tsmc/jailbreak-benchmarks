# Jailbreak benchmarks (downloaded 2026-10-01)

| Dir | Source | Contents |
|---|---|---|
| JailbreakBench/JBB-Behaviors | hf: JailbreakBench/JBB-Behaviors | harmful 100, benign 100, judge-comparison 300 |
| JailbreakBench/artifacts | github: JailbreakBench/artifacts | official jailbreak strings for the 100 JBB behaviors: PAIR, GCG (white-box + transfer), JBC/AIM, prompt_with_random_search, DSN; targets gpt-3.5 / gpt-4 / llama-2-7b / vicuna-13b |
| DAN | github: verazuo/jailbreak_llms (CCS'24 "Do Anything Now") | jailbreak prompts 1405 (2023-12-25) / 666 (2023-05-07), regular prompts, forbidden_question_set 390 (+ with_prompts 107250) |
| JailbreakTrigger | github: HowieHwong/TrustLLM dataset.zip -> safety/jailbreak.json | 1400 = 14 jailbreak types x 100 |
| HarmBench_attacks/{GCG,PAIR,AutoDAN} | zenodo 10714577 (HarmBench 1.0 precomputed results), results_text only | per target model: test_cases/, completions/, results/; GCG 20 models, PAIR 29, AutoDAN 21; ~400 behaviors each (GCG mixtral_8x7b only 2 in the official release) |
| WildJailbreak | hf: allenai/wildjailbreak (gated, AI2 license) | eval 2210 (adversarial_harmful 2000 + adversarial_benign 210), train 261559 |

Other HarmBench attack methods (TAP, EnsembleGCG, PAP, HumanJailbreaks, ...) are in the same zenodo zip; extract with remotezip, see results_text/<METHOD>/.

## Files not in this repo (over GitHub's 100MB limit)

`WildJailbreak/train/train.tsv` (531MB) and
`DAN/forbidden_question/forbidden_question_set_with_prompts.csv` (334MB).

Run `python fetch_large_files.py` from the repo root to download them into place.
WildJailbreak is gated: accept the AI2 license on its Hugging Face page and `hf auth login` first.
