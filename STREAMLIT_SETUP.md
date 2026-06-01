# 🚀 LLM Quantization Benchmark Streamlit App

Comprehensive Streamlit dashboard for analyzing INT8 quantization performance on Large Language Models.

## 📋 Features

✅ **Interactive Dashboard**
- Overview of all models and configurations
- Key metrics display
- Performance radar charts
- Real-time comparisons

✅ **Model Rankings**
- Complete ranking by composite score
- Best/runner-up highlights
- Detailed recommendations

✅ **Detailed Metrics Analysis**
- Throughput, BLEU, ROUGE metrics
- Statistical summaries
- Distribution analysis
- GPU comparisons

✅ **Use Case Recommendations**
- Real-time chat applications
- Code generation API
- Document summarization
- Mobile/edge deployment
- Configuration examples for each use case

✅ **Comprehensive Documentation**
- Research methodology
- Scoring framework explanation
- Dataset information
- Referenced research (Oprea & Bâra 2026)

## 🛠 Installation

### Local Setup

```bash
# Clone or navigate to project directory
cd presentasi\ kelompok

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements_streamlit.txt

# Run the app
streamlit run app.py
```

### Hugging Face Spaces Setup

1. **Create a new Space**
   - Go to: https://huggingface.co/spaces
   - Click "Create new Space"
   - Name: `llm-quantization-benchmark`
   - Space type: **Streamlit**
   - Visibility: Public

2. **Upload Files**
   ```
   llm-quantization-benchmark/
   ├── app.py
   ├── requirements.txt
   └── best_model_selection/
       └── results_summary.csv
   ```

3. **Configure Files**
   - Add `app.py` to root
   - Rename `requirements_streamlit.txt` to `requirements.txt`
   - Copy `best_model_selection/results_summary.csv` to app directory

4. **Deploy**
   - Push to repo or upload files
   - Hugging Face auto-deploys!
   - Share URL: `https://huggingface.co/spaces/[YOUR_USERNAME]/llm-quantization-benchmark`

## 📦 Project Structure

```
presentasi_kelompok/
├── app.py                                    # Streamlit app
├── requirements_streamlit.txt                # Python dependencies
├── best_model_selection/
│   ├── results_summary.csv                   # Main data file
│   ├── index.html                            # Bilingual HTML dashboard
│   ├── styles.css                            # Styling
│   ├── script-bilingual.js                   # Functionality
│   └── [other files]
├── dataset/
│   └── [analysis data files]
└── notebooks/
    └── [jupyter notebooks]
```

## 📊 Data Files Required

The app expects `best_model_selection/results_summary.csv` with columns:

```
Model,GPU,Composite_Score,Throughput_tok_s,BLEU,ROUGE_1,ROUGE_L,Recommendation
GPT-2,RTX4080,0.7234,127.36,0.22,0.629,0.415,"Best overall..."
...
```

## 🎯 Dashboard Pages

### 1. 📊 Dashboard
- Key metrics cards
- Overall comparison charts
- Performance radar visualization
- Best vs runner-up analysis

### 2. 🏆 Model Rankings
- Complete leaderboard
- Ranking by composite score
- Top 3 highlights
- Detailed recommendations

### 3. 📈 Detailed Metrics
- Metric-specific analysis
- Statistical summaries
- Distribution by model/GPU
- Box plot comparisons

### 4. 💡 Use Case Recommendations
- Real-time chat: GPT-2 INT8
- Code generation: Qwen1.5-1.8B
- Document summarization: LLaMA-2-7B
- Mobile/edge: Qwen on RTX4070
- Configuration examples for each

### 5. ℹ️ About
- Research objectives
- Evaluation metrics explanation
- Methodology details
- Dataset summary

## 🔧 Customization

### Add More Use Cases
Edit the `use_cases` dictionary in `app.py`:

```python
use_cases = {
    "Your Use Case": {
        "icon": "🎯",
        "requirements": [...],
        "recommended_model": "...",
        "metrics": {...},
        "performance": {...},
        "use_cases": [...]
    }
}
```

### Modify Dashboard Layout
- Adjust colors in CSS
- Change chart types in Plotly
- Modify metric weights
- Add new visualizations

### Update Data
- Replace `results_summary.csv` with new results
- App auto-reloads with new data
- Add new model configurations

## 🚀 Deployment

### Option 1: Hugging Face Spaces (Recommended)
```bash
# Push to Hugging Face
huggingface-cli login
huggingface-cli upload [username]/llm-quantization-benchmark .
```

### Option 2: Streamlit Cloud
```bash
# Deploy to Streamlit Cloud
# https://streamlit.io/cloud
```

### Option 3: Docker
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements_streamlit.txt .
RUN pip install -r requirements_streamlit.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

Deploy with:
```bash
docker build -t llm-benchmark .
docker run -p 8501:8501 llm-benchmark
```

## 📈 Performance

- **Load Time**: < 2 seconds
- **Chart Rendering**: Interactive & responsive
- **Data Update**: Real-time (< 1 second)
- **Mobile Friendly**: Fully responsive design

## 🔐 Security

- No external data calls
- Static CSV data only
- No sensitive information
- Safe for public sharing

## 📝 License

Based on Oprea & Bâra (2026) Research

## 🤝 Support

For issues or questions:
1. Check data format in `results_summary.csv`
2. Verify all required columns present
3. Ensure `requirements_streamlit.txt` installed
4. Clear Streamlit cache: `streamlit cache clear`

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Hugging Face Spaces Guide](https://huggingface.co/docs/hub/spaces)
- [Plotly Visualization](https://plotly.com/python)
- [Original Research: Oprea & Bâra (2026)](https://example.com)

---

**Built with ❤️ for LLM Quantization Research**

**Deployment:** Hugging Face Spaces | **Visualization:** Plotly | **Framework:** Streamlit
