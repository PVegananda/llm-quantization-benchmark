# Deployment Guide: Hugging Face Spaces

## 📱 Quick Setup (5 minutes)

### Step 1: Create Hugging Face Space
```bash
# Visit: https://huggingface.co/spaces
# Click "Create new Space"
# Fill in:
# - Space name: llm-quantization-benchmark
# - Space type: Streamlit
# - Visibility: Public
```

### Step 2: Upload Files
Option A (Web Upload):
1. Go to your space repo
2. Click "Add file" → "Upload files"
3. Upload these files:
   - `app.py`
   - `requirements.txt` (copy from `requirements_streamlit.txt`)
   - Create folder `best_model_selection/`
   - Upload `best_model_selection/results_summary.csv`

Option B (Git Push):
```bash
# Clone your space repo
git clone https://huggingface.co/spaces/[YOUR_USERNAME]/llm-quantization-benchmark
cd llm-quantization-benchmark

# Copy files
cp /path/to/app.py .
cp /path/to/requirements_streamlit.txt requirements.txt
mkdir -p best_model_selection
cp /path/to/best_model_selection/results_summary.csv best_model_selection/

# Push to Hugging Face
git add .
git commit -m "Add LLM Quantization Benchmark Dashboard"
git push
```

### Step 3: Auto-Deploy
- Hugging Face automatically deploys when files are pushed
- Wait 2-3 minutes for build
- Access your deployment at: `https://huggingface.co/spaces/[YOUR_USERNAME]/llm-quantization-benchmark`

## 📊 What's Included

Your Streamlit app features:

### Pages/Tabs:
1. **📊 Dashboard**
   - Key metrics overview
   - Composite score comparison
   - Throughput analysis
   - Performance radar charts

2. **🏆 Model Rankings**
   - Complete leaderboard (6 configurations)
   - Top 3 winners highlighted
   - Composite scores with explanations

3. **📈 Detailed Metrics**
   - Analysis of: Throughput, BLEU, ROUGE-1, ROUGE-L
   - Statistical summaries (mean, median, std, min, max)
   - Performance by model and GPU
   - Box plots and distributions

4. **💡 Use Case Recommendations**
   - Real-Time Chat Application
   - Code Generation API
   - Document Summarization
   - Mobile/Edge Deployment
   - Configuration code for each use case

5. **ℹ️ About**
   - Research objectives and methodology
   - Evaluation metrics explanation
   - Dataset information
   - Referenced research details

## 🎯 Features

✅ **Interactive Visualizations**
- Plotly charts (bar, box, radar, scatter)
- Real-time filtering and selection
- Responsive design

✅ **Data-Driven Insights**
- 6 model configurations analyzed
- Multi-criteria scoring (6 metrics)
- Statistical analysis built-in

✅ **Production-Ready**
- No dependencies on API calls
- Runs entirely on CSV data
- Fast load times (< 2 seconds)

✅ **Professional Design**
- Clean, modern UI
- Bilingual ready (easily add translations)
- Mobile-friendly layout

## 📋 File Structure

```
huggingface-space/
├── app.py                              # Main Streamlit app
├── requirements.txt                    # Dependencies
├── README.md                           # Optional: space info
└── best_model_selection/
    └── results_summary.csv             # Data file
```

## 🔧 Files to Modify

### `requirements.txt`
Copy content from `requirements_streamlit.txt`:
```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
```

### `app.py`
The main dashboard - no modifications needed unless you want to:
- Add new metrics
- Change colors/styling
- Add new use cases
- Modify chart types

### `best_model_selection/results_summary.csv`
Data file - update to add:
- New model configurations
- Different GPU hardware
- Updated results from new experiments

## ✨ Customization

### Add a New Use Case
In `app.py`, find the `use_cases` dictionary and add:

```python
"Your Use Case Name": {
    "icon": "🎯",
    "requirements": [
        "✅ Requirement 1",
        "✅ Requirement 2",
    ],
    "recommended_model": "Model Name on GPU",
    "metrics": {
        "Metric1": "Value/Description",
        "Metric2": "Value/Description",
    },
    "performance": {
        "Expected1": "Value",
        "Expected2": "Value",
    },
    "use_cases": [
        "Real-world use case 1",
        "Real-world use case 2",
    ]
}
```

### Change Dashboard Colors
Modify in `app.py`:
- Color codes: `#667eea` (primary), `#764ba2` (secondary)
- Replace in CSS style tags
- Update Plotly colors in `color_discrete_map`

### Update Data
1. Generate new `results_summary.csv`
2. Upload to `best_model_selection/` folder
3. App automatically reloads with new data

## 🚀 Deploy to Production

### Link Your Domain (Optional)
In Hugging Face Space settings:
1. Go to "Settings" → "Space settings"
2. Add custom domain under "Custom Domain"

### Enable Persistent Storage (Optional)
For storing user interactions:
1. Go to "Settings" → "Space settings"
2. Enable "Persistent Storage"

## 📊 Monitoring

Check if your space is running:
- Visit the live URL
- Space status shown in Hugging Face dashboard
- Auto-restarts on error

## 🔄 Updates

To update after deployment:

**Option 1: Web Upload**
- Go to space files
- Click "Edit" on files
- Make changes and save

**Option 2: Git Push**
```bash
cd llm-quantization-benchmark
# Make changes
git add .
git commit -m "Update dashboard"
git push
```

## 🆘 Troubleshooting

### App doesn't load
- Check `requirements.txt` installed properly
- Verify CSV file path: `best_model_selection/results_summary.csv`
- Check Streamlit error logs in space

### Missing data
- Ensure `results_summary.csv` has all required columns
- Verify CSV format (comma-separated)
- Check no special characters in data

### Slow performance
- Streamlit caches data automatically
- Clear cache: `streamlit cache clear` (local)
- Hugging Face handles optimization

## 📚 Resources

- [Hugging Face Spaces Docs](https://huggingface.co/docs/hub/spaces)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Visualization](https://plotly.com/python)

## 🎉 You're Done!

Your LLM Quantization Benchmark dashboard is now live!

Share the URL with colleagues:
```
https://huggingface.co/spaces/[YOUR_USERNAME]/llm-quantization-benchmark
```

---

**Questions?** Check Streamlit docs or Hugging Face community forums
