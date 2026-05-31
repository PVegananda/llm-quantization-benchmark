# Data Audit Report — What Was Wrong and What Was Fixed

## Summary of Errors Found in Original Files

| File | Error Type | Detail |
|---|---|---|
| `table3_timing_metrics.csv` | WRONG VALUES | GPT-2 RTX4070 FP16 showed 12.45s/45.32 tok/s — journal says 23.21s/11.03 tok/s |
| `table9_text_metrics.csv` | FABRICATED ROWS | Added GPT-2 rows with invented BLEU/ROUGE — GPT-2 is NOT in journal Table 9 |
| `table13_code_metrics.csv` | FABRICATED ROWS | Added FP16 baseline rows that do not exist in journal Table 13 |
| `experimental_setup.csv` | WRONG PARAMS | Max_Tokens=512 (should be 256), Temperature=0.7 (should be 1.0), Top_P=0.9 (NOT USED) |
| `findings_summary.csv` | WRONG CALC | GPT2_RTX4070_Speedup=1.53x (correct is 23.21/17.37=1.34x) |

## Corrected Files in This Package

| File | Journal Source | Status |
|---|---|---|
| `table1_generation_hyperparameters.csv` | Table 1 | ✅ Corrected |
| `table2_model_specifications.csv` | Table 2 | ✅ Corrected |
| `table3_timing_metrics.csv` | Table 3 | ✅ Corrected |
| `table4_qualitative_llama2.csv` | Table 4 | ✅ New |
| `table5_qualitative_qwen.csv` | Table 5 | ✅ New |
| `table6_single_prompt_scores.csv` | Table 6 | ✅ Corrected |
| `table7_llama2_vs_human.csv` | Table 7 | ✅ Corrected |
| `table8_qwen_vs_human.csv` | Table 8 | ✅ Corrected |
| `table9_text_metrics_50prompts.csv` | Table 9 | ✅ Corrected (removed GPT-2 rows) |
| `table10_int8_vs_human_20prompts.csv` | Table 10 | ✅ Corrected |
| `table11_fp16_vs_human_20prompts.csv` | Table 11 | ✅ Corrected |
| `table12_software_environment.csv` | Table 12 | ✅ Corrected |
| `table13_code_metrics.csv` | Table 13 | ✅ Corrected (removed fabricated FP16 rows) |
| `section47_syntactic_validity.csv` | Section 4.7 | ✅ New |
| `appendixA_sample_outputs.csv` | Appendix A | ✅ New |
| `findings_summary.csv` | Derived | ✅ Corrected calculations |
| `gpu_specifications.csv` | Section 4 text | ✅ Corrected |

## Key Rules for This Dataset

1. **Table 9 covers ONLY LLaMA-2 and Qwen** — GPT-2 was not evaluated for BLEU/ROUGE aggregates
2. **Table 13 is INT8 vs FP16 delta only** — no separate FP16 baseline rows exist
3. **Hyperparams**: max_new_tokens=256, temperature=1.0, top-k=OFF, top-p=OFF, greedy decoding
4. **GPT-2 INT8 on RTX4080 is SLOWER than FP16** (0.55x) — this is a real journal finding, not an error
5. **LLaMA-2 FP16 on RTX4070 uses CPU offloading** — the 1244s is real but not a fair GPU comparison
