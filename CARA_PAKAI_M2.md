# Cara Menjalankan Project di MacBook Air M2

## Persiapan (jalankan sekali)

```bash
cd m2-presentation
pip install -r requirements_m2.txt
jupyter notebook
```

## Urutan Notebook

| # | Notebook | Isi | Waktu |
|---|---|---|---|
| 01 | data_preparation | Load & verifikasi 20 CSV jurnal | ~2 menit |
| 02 | inference_analysis | Timing + reproduksi Figure 2 & 3 | ~3 menit |
| 03 | quality_metrics | BLEU/ROUGE + Figure 4 & 5 | ~3 menit |
| 04 | compute_metrics_m2 | **Praktik hitung BLEU & ROUGE sendiri** | ~5 menit |
| 05 | model_selection | Multi-criteria scoring + model terbaik | ~3 menit |
| 06 | **evaluasi_klasifikasi_metrik_dosen** | **SEMUA metrik slide dosen** | ~8 menit |
| 07 | **decision_framework_presentasi** | **Decision tree + checklist final** | ~5 menit |

## Metrik yang Dicakup (sesuai slide dosen Pertemuan 8)

### Kerangka Pemilihan Metrik
| Konteks | Metrik Utama | Metrik Pendukung | Status |
|---|---|---|---|
| Balanced (50/50) | Accuracy, F1 | Confusion Matrix, ROC-AUC | ✅ NB06 |
| Mild Imbalanced | F1, MCC | PR-AUC, Precision, Recall | ✅ NB06 |
| Severe Imbalanced | MCC, PR-AUC | F2, Confusion Matrix | ✅ NB06 |
| Probabilistic | Brier, ECE, Log-Loss | Reliability Diagram | ✅ NB06 |
| Cost-sensitive | F-beta | F-beta curve | ✅ NB06 |
| Multi-class balanced | Accuracy, Macro-F1 | Confusion Matrix, per-class | ✅ NB06 |
| Multi-class imbalanced | Weighted-F1, MCC | Per-class report | ✅ NB06 |

### Take-aways Penting (dari slide dosen)
1. Confusion Matrix adalah FONDASI — semua metrik dari 4 sel (TP,TN,FP,FN)
2. Accuracy bisa menipu pada data imbalanced — selalu dampingi F1, MCC

## Figures yang Dihasilkan (outputs/figures/)

| File | Isi |
|---|---|
| fig2_rtx4070_inference.png | Reproduksi Figure 2 jurnal |
| fig3_rtx4080_inference.png | Reproduksi Figure 3 jurnal |
| fig4_5_quality_scores.png | Reproduksi Figure 4 & 5 jurnal |
| text_vs_code_sensitivity.png | Sensitivitas kode vs teks |
| model_ranking.png | Multi-criteria ranking |
| tradeoff_scatter.png | Speedup vs quality trade-off |
| confusion_matrix_full.png | ← SLIDE DOSEN: Confusion Matrix |
| classification_metrics_bar.png | ← SLIDE DOSEN: Core metrics bar |
| roc_pr_curves.png | ← SLIDE DOSEN: ROC-AUC & PR-AUC |
| probabilistic_metrics.png | ← SLIDE DOSEN: Brier, ECE, Log-Loss |
| fbeta_analysis.png | ← SLIDE DOSEN: F-beta cost-sensitive |
| dashboard_semua_metrik.png | ← Dashboard 9-panel semua metrik |
| tabel_pemilihan_metrik_dosen.png | ← Reproduksi tabel slide dosen |
| decision_framework_dosen.png | ← Reproduksi decision tree slide dosen |
| threshold_sensitivity_all_metrics.png | ← Analisis sensitivitas threshold |
