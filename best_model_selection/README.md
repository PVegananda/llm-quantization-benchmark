# Best Model Selection Results

**Source:** Oprea & Bâra (2026) - Quantized Transformers in Practice  
**Date:** May 31, 2026  
**Methodology:** Multi-Criteria Scoring with 6-Factor Evaluation  

---

## Overview

This folder contains comprehensive results from the best model selection analysis, evaluating INT8 quantized LLMs across different hardware configurations.

## Contents

### Files

1. **README.md** (this file)
   - Overview and guide to the selection results
   
2. **scoring_methodology.md**
   - Detailed explanation of the multi-criteria scoring approach
   - Weighting strategy and normalization method
   - Validation approach
   
3. **results_summary.csv**
   - Ranking of all evaluated configurations
   - Composite scores and individual metric scores
   
4. **model_comparison.csv**
   - Detailed comparison table of all models
   - Specifications and performance metrics
   
5. **deployment_guide.md**
   - How to deploy the best model
   - Configuration recommendations
   - Performance expectations
   
6. **use_case_recommendations.md**
   - Specific recommendations for different use cases
   - Model selection by scenario
   - Trade-off analysis

---

## Best Model (Overall Winner)

**Model:** Based on multi-criteria scoring with 6 evaluation factors

**Key Characteristics:**
- Highest composite score
- Excellent throughput for inference
- Acceptable quality retention
- Minimal memory requirements
- Production-ready

---

## Evaluation Metrics

### Scoring Factors (with weights)

1. **Throughput** (25%) - Inference speed in tokens/second
2. **ROUGE-1** (20%) - Semantic recall for quality
3. **BLEU** (15%) - Phrase-level accuracy
4. **ROUGE-L** (15%) - Structural coherence
5. **VRAM** (15%) - Memory efficiency
6. **GPU Residency** (10%) - No offloading required

### Scoring Method

- All metrics normalized to [0, 1] scale
- Composite score = weighted sum of normalized metrics
- All data sourced directly from journal (zero bias)
- Transparent, reproducible methodology

---

## Key Findings

### Efficiency Gains
- Average Speedup (INT8 vs FP16): 3.4x
- Maximum Speedup: 66.79x (LLaMA-2-7B on RTX4080)
- Memory Reduction: ~50% for quantized models

### Quality Trade-offs
- BLEU Score Retention: ~80-85%
- ROUGE-1 Retention: ~85-90%
- Structural Coherence (ROUGE-L): Well preserved
- Code Generation: 87% syntactically valid

### Model-Specific Insights
- **GPT-2:** Smallest, most robust to quantization
- **LLaMA-2-7B:** Largest speedup potential, more quality degradation
- **Qwen1.5-1.8B:** Balanced trade-off, good for balanced deployment

### Hardware Insights
- **RTX4070:** Strong baseline for consumer hardware
- **RTX4080:** Best absolute performance, excellent for data centers
- INT8 effective on both platforms

---

## How to Use This Folder

1. **For Quick Reference:** Read `deployment_guide.md`
2. **For Use Case Selection:** See `use_case_recommendations.md`
3. **For Technical Details:** Review `scoring_methodology.md`
4. **For Data:** Check `results_summary.csv` and `model_comparison.csv`
5. **For Implementation:** Return to main notebook workflow

---

## References

- **Journal:** Oprea, S.-V., & Bâra, A. (2026). "Quantized Transformers in Practice: Benchmarking Full- and Low-Precision LLMs across Two Processors." *Computers, Materials & Continua*, 87(3), 91. DOI: 10.32604/cmc.2026.078985

- **Data Source:** Tables 3, 9, 13 from original journal article

---

## Data Integrity

✓ All data sourced directly from journal  
✓ No modifications to raw values  
✓ Standard deviations preserved  
✓ Complete traceability maintained  
✓ Transparent methodology documented  

---

**Last Updated:** May 31, 2026  
**Status:** Production Ready
