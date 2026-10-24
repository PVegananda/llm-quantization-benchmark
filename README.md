<div align="center">
  <img src="assets/logo.svg" alt="LLM Quantization Benchmark logo" width="96">
  <h1>LLM Quantization Benchmark</h1>
  <p><strong>Reproducible FP16 vs INT8 evaluation for efficient large language model deployment.</strong></p>
  <p>
    <a href="https://github.com/PVegananda/llm-quantization-benchmark"><img src="https://img.shields.io/github/stars/PVegananda/llm-quantization-benchmark?style=flat-square" alt="GitHub stars"></a>
    <a href="https://github.com/PVegananda/llm-quantization-benchmark"><img src="https://img.shields.io/github/last-commit/PVegananda/llm-quantization-benchmark?style=flat-square" alt="Last commit"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10 or newer"></a>
    <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit dashboard"></a>
  </p>
</div>

## Overview

This project benchmarks the practical trade-offs between FP16 and post-training INT8 quantization for transformer language models on consumer laptop GPUs. It combines reproducible inference measurements, text and code quality metrics, curated source data, and a Streamlit dashboard for exploration.

The benchmark covers:

- **Models:** GPT-2, Llama 2 7B Chat, and Qwen1.5 1.8B Chat
- **Hardware:** NVIDIA RTX 4070 and RTX 4080 laptop GPUs
- **Metrics:** throughput, latency, VRAM use, BLEU, ROUGE-1, ROUGE-L, and code validity
- **Workflow:** data preparation, inference, evaluation, visualization, and model selection

## Key findings

- INT8 can materially reduce memory requirements and improve throughput, especially for larger models.
- Quantization quality trade-offs are measurable with both lexical metrics and code-generation checks.
- Qwen1.5 1.8B provides a practical balance of quality, speed, and memory use in the included results.
- Hardware and offloading behavior strongly affect the observed benefit of quantization.

See the [evaluation report](report/research_report.md) and [model-selection results](best_model_selection/) for the underlying analysis.

## Quick start

```bash
git clone https://github.com/PVegananda/llm-quantization-benchmark.git
cd llm-quantization-benchmark
python -m venv .venv
source .venv/bin/activate
pip install -r requirements_streamlit.txt
streamlit run app/app.py
```

The dashboard reads the published evaluation data from `best_model_selection/results_summary.csv`. GPU-backed inference and notebook workflows may require the platform-specific dependencies in `requirements_m2.txt` or `requirements_streamlit.txt`.

## Repository layout

| Path | Purpose |
| --- | --- |
| [`app/`](app/) | Streamlit dashboard for comparing benchmark configurations |
| [`best_model_selection/`](best_model_selection/) | Scoring methodology, rankings, and deployment recommendations |
| [`dataset/`](dataset/) | Cleaned benchmark tables, prompts, and human references |
| [`dataset_raw/`](dataset_raw/) | Source tables and derived calculations |
| [`notebooks/`](notebooks/) | End-to-end preparation, inference, evaluation, and visualization notebooks |
| [`outputs/`](outputs/) | Exported metrics and figures |
| [`scripts/`](scripts/) | Reusable inference and metric-computation utilities |
| [`report/`](report/) | Research report and interpretation of results |

## Reproducibility

The repository separates raw inputs from derived tables and keeps the evaluation workflow in numbered notebooks. To reproduce the analysis, run the notebooks in order and record the GPU, driver, CUDA, PyTorch, and Transformers versions used for the run.

## Research reference

The benchmark is based on:

> Oprea, S.-V., & Bâra, A. (2026). *Quantized Transformers in Practice: Benchmarking Full- and Low-Precision LLMs across Two Processors*. Computers, Materials & Continua. DOI: [10.32604/cmc.2026.078985](https://doi.org/10.32604/cmc.2026.078985)

## License and model terms

This repository contains research data, analysis code, and derived results. Review the original model licenses before downloading or deploying any model; model terms are separate from the terms of this repository.
