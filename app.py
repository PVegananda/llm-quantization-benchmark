import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

# Page config
st.set_page_config(
    page_title="LLM Quantization Benchmark",
    page_icon="Q",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
        }
        .metric-value {
            font-size: 2.5em;
            font-weight: bold;
            margin: 10px 0;
        }
        .metric-label {
            font-size: 1em;
            opacity: 0.9;
        }
        .use-case-box {
            background: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.markdown("# LLM Quantization Benchmark Analysis")
st.markdown("### INT8 Quantization Performance Analysis on Consumer Hardware")
st.markdown("Based on Oprea & Bâra (2026) Research")

# Load data
@st.cache_data
def load_data():
    # Load results summary
    results_df = pd.read_csv("best_model_selection/results_summary.csv")
    return results_df

try:
    results_df = load_data()
except FileNotFoundError:
    st.error("Error: Could not find results_summary.csv")
    st.stop()

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select View:",
    ["Dashboard", "Model Rankings", "Detailed Metrics", "Use Case Recommendations", "About"]
)

# ============================================================================
# PAGE 1: DASHBOARD
# ============================================================================
if page == "Dashboard":
    st.markdown("---")
    
    # Key metrics
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.metric(
            "Total Models",
            len(results_df),
            "configurations"
        )
    
    with col2:
        max_throughput = results_df['Throughput_tok_s'].max()
        st.metric(
            "Max Throughput",
            f"{max_throughput:.1f}",
            "tok/s"
        )
    
    with col3:
        best_score = results_df['Composite_Score'].max()
        st.metric(
            "Best Score",
            f"{best_score:.4f}",
            "composite"
        )
    
    with col4:
        avg_bleu = results_df['BLEU'].mean()
        st.metric(
            "Avg BLEU",
            f"{avg_bleu:.4f}",
            "quality metric"
        )
    
    with col5:
        avg_rouge = results_df['ROUGE_1'].mean()
        st.metric(
            "Avg ROUGE-1",
            f"{avg_rouge:.4f}",
            "semantic"
        )
    
    with col6:
        models_count = results_df['Model'].nunique()
        st.metric(
            "Models Tested",
            models_count,
            "architectures"
        )
    
    st.markdown("---")
    
    # Overall comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Composite Scores by Configuration")
        fig = px.bar(
            results_df.sort_values('Composite_Score', ascending=True),
            x='Composite_Score',
            y='Model',
            color='GPU',
            orientation='h',
            hover_data=['Composite_Score', 'Throughput_tok_s', 'BLEU'],
            color_discrete_map={'RTX4080': '#667eea', 'RTX4070': '#764ba2'}
        )
        fig.update_layout(height=400, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Throughput Comparison")
        fig = px.bar(
            results_df.sort_values('Throughput_tok_s', ascending=True),
            x='Throughput_tok_s',
            y='Model',
            color='GPU',
            orientation='h',
            hover_data=['Throughput_tok_s', 'Composite_Score'],
            color_discrete_map={'RTX4080': '#667eea', 'RTX4070': '#764ba2'}
        )
        fig.update_layout(height=400, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Metrics radar chart
    st.subheader("Performance Radar - Best vs Runner-up")
    
    best_model = results_df.loc[results_df['Composite_Score'].idxmax()]
    runner_up = results_df.loc[results_df['Composite_Score'].nlargest(2).index[1]]
    
    # Normalize metrics to 0-1 for radar
    metrics_names = ['Throughput', 'BLEU', 'ROUGE_1', 'ROUGE_L']
    
    # Get min-max for normalization
    throughput_vals = results_df['Throughput_tok_s'].values
    bleu_vals = results_df['BLEU'].values
    rouge1_vals = results_df['ROUGE_1'].values
    rougel_vals = results_df['ROUGE_L'].values
    
    def normalize(value, arr):
        return (value - arr.min()) / (arr.max() - arr.min()) if arr.max() != arr.min() else 0.5
    
    best_values = [
        normalize(best_model['Throughput_tok_s'], throughput_vals),
        normalize(best_model['BLEU'], bleu_vals),
        normalize(best_model['ROUGE_1'], rouge1_vals),
        normalize(best_model['ROUGE_L'], rougel_vals)
    ]
    
    runner_values = [
        normalize(runner_up['Throughput_tok_s'], throughput_vals),
        normalize(runner_up['BLEU'], bleu_vals),
        normalize(runner_up['ROUGE_1'], rouge1_vals),
        normalize(runner_up['ROUGE_L'], rougel_vals)
    ]
    
    fig = go.Figure(data=[
        go.Scatterpolar(
            r=best_values,
            theta=metrics_names,
            fill='toself',
            name=f"{best_model['Model']} ({best_model['GPU']})",
            line=dict(color='#667eea')
        ),
        go.Scatterpolar(
            r=runner_values,
            theta=metrics_names,
            fill='toself',
            name=f"{runner_up['Model']} ({runner_up['GPU']})",
            line=dict(color='#764ba2')
        )
    ])
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE 2: MODEL RANKINGS
# ============================================================================
elif page == "Model Rankings":
    st.markdown("---")
    st.subheader("Complete Model Rankings (by Composite Score)")
    
    # Add ranking
    ranked_df = results_df.sort_values('Composite_Score', ascending=False).reset_index(drop=True)
    ranked_df.insert(0, 'Rank', range(1, len(ranked_df) + 1))
    
    # Format display
    display_df = ranked_df.copy()
    display_df['Composite_Score'] = display_df['Composite_Score'].round(4)
    display_df['Throughput_tok_s'] = display_df['Throughput_tok_s'].round(2)
    display_df['BLEU'] = display_df['BLEU'].round(4)
    display_df['ROUGE_1'] = display_df['ROUGE_1'].round(4)
    display_df['ROUGE_L'] = display_df['ROUGE_L'].round(4)
    
    # Rename columns for display
    display_df.columns = [
        'Rank', 'Model', 'GPU', 'Composite Score', 
        'Throughput (tok/s)', 'BLEU', 'ROUGE-1', 'ROUGE-L', 'Recommendation'
    ]
    
    # Color code the dataframe
    st.dataframe(
        display_df,
        use_container_width=True,
        height=400,
        hide_index=True
    )
    
    st.markdown("---")
    
    # Best model highlight
    col1, col2, col3 = st.columns(3)
    
    best_idx = ranked_df['Composite_Score'].idxmax()
    best = ranked_df.loc[best_idx]
    
    with col1:
        st.markdown("""
            <div class="use-case-box">
                <h3>#1 Best Overall</h3>
                <p><strong>{}</strong></p>
                <p>{}</p>
                <p style="font-size: 1.5em; color: #667eea;"><strong>{:.4f}</strong></p>
            </div>
        """.format(best['Model'], best['GPU'], best['Composite_Score']), unsafe_allow_html=True)
    
    second_idx = ranked_df['Composite_Score'].nlargest(2).index[1]
    second = ranked_df.loc[second_idx]
    
    with col2:
        st.markdown("""
            <div class="use-case-box">
                <h3>#2 Runner-up</h3>
                <p><strong>{}</strong></p>
                <p>{}</p>
                <p style="font-size: 1.5em; color: #667eea;"><strong>{:.4f}</strong></p>
            </div>
        """.format(second['Model'], second['GPU'], second['Composite_Score']), unsafe_allow_html=True)
    
    third_idx = ranked_df['Composite_Score'].nlargest(3).index[2]
    third = ranked_df.loc[third_idx]
    
    with col3:
        st.markdown("""
            <div class="use-case-box">
                <h3>#3 Third Place</h3>
                <p><strong>{}</strong></p>
                <p>{}</p>
                <p style="font-size: 1.5em; color: #667eea;"><strong>{:.4f}</strong></p>
            </div>
        """.format(third['Model'], third['GPU'], third['Composite_Score']), unsafe_allow_html=True)

# ============================================================================
# PAGE 3: DETAILED METRICS
# ============================================================================
elif page == "Detailed Metrics":
    st.markdown("---")
    
    # Metric selector
    metric_cols = ['Throughput_tok_s', 'BLEU', 'ROUGE_1', 'ROUGE_L', 'Composite_Score']
    metric_labels = ['Throughput (tok/s)', 'BLEU Score', 'ROUGE-1 Score', 'ROUGE-L Score', 'Composite Score']
    
    selected_metric = st.selectbox(
        "Select Metric to Analyze:",
        metric_labels,
        index=4
    )
    
    metric_key = metric_cols[metric_labels.index(selected_metric)]
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"{selected_metric} Distribution")
        
        fig = px.box(
            results_df,
            x='GPU',
            y=metric_key,
            color='Model',
            points='all',
            hover_data=['Model', 'GPU',  metric_key]
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Statistics")
        
        col_data = results_df[metric_key]
        
        st.metric("Mean", f"{col_data.mean():.4f}")
        st.metric("Median", f"{col_data.median():.4f}")
        st.metric("Std Dev", f"{col_data.std():.4f}")
        st.metric("Min", f"{col_data.min():.4f}")
        st.metric("Max", f"{col_data.max():.4f}")
    
    st.markdown("---")
    
    # Comparison by Model
    st.subheader("Performance by Model (All Configurations)")
    
    metric_by_model = results_df.groupby('Model')[metric_key].agg(['mean', 'min', 'max', 'count'])
    metric_by_model = metric_by_model.round(4)
    
    st.dataframe(metric_by_model, use_container_width=True)
    
    st.markdown("---")
    
    # GPU Comparison
    st.subheader("Performance by GPU")
    
    metric_by_gpu = results_df.groupby('GPU')[metric_key].agg(['mean', 'min', 'max', 'count'])
    metric_by_gpu = metric_by_gpu.round(4)
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.dataframe(metric_by_gpu, use_container_width=True)
    
    with col_b:
        fig = px.bar(
            metric_by_gpu.reset_index(),
            x='GPU',
            y='mean',
            color='GPU',
            title=f"Average {selected_metric} by GPU",
            color_discrete_map={'RTX4080': '#667eea', 'RTX4070': '#764ba2'}
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE 4: USE CASE RECOMMENDATIONS
# ============================================================================
elif page == "Use Case Recommendations":
    st.markdown("---")
    
    use_cases = {
        "Real-Time Chat Application": {
            "icon": "Text",
            "requirements": [
                "Sub-100ms first-token latency",
                "High throughput for concurrent users",
                "Quality acceptable but not critical",
                "Cost-sensitive"
            ],
            "recommended_model": "GPT-2 INT8 on RTX4080",
            "metrics": {
                "Throughput": "127.36 tok/s (100+ concurrent users)",
                "Latency": "~50ms (acceptable for chat)",
                "BLEU": "0.22 (conversational quality)",
                "Memory": "0.3-0.5 GB",
                "Cost": "Lowest configuration"
            },
            "performance": {
                "Concurrent Users": "200+",
                "Latency": "50-100ms",
                "Daily Requests": "1M+",
                "Server Cost": "$50-100/month"
            },
            "use_cases": ["Customer Support Chatbot", "Real-time Assistance", "Interactive Agents"]
        },
        "Code Generation API": {
            "icon": "Code",
            "requirements": [
                "Syntactic correctness critical (87%+ valid code)",
                "Semantic preservation important",
                "1-5 second latency acceptable",
                "Cost-effective deployment"
            ],
            "recommended_model": "Qwen1.5-1.8B-Chat INT8 on RTX4080",
            "metrics": {
                "Code Validity": "87% syntactic correctness",
                "ROUGE-1": "61.8% semantic preservation",
                "Memory": "2.0 GB",
                "Speed": "23.10 tok/s",
                "Cost": "Cost-effective"
            },
            "performance": {
                "Valid Code Rate": "87%",
                "Generation Time": "1-5 seconds",
                "Memory Per Instance": "2.0 GB",
                "Concurrent Instances": "8 per RTX4080"
            },
            "use_cases": ["GitHub Copilot Alternative", "IDE Integration", "Code Review Tools"]
        },
        "Document Summarization": {
            "icon": "Document",
            "requirements": [
                "Highest quality retention",
                "Semantic accuracy critical",
                "Batch processing acceptable",
                "Comprehensive information preservation"
            ],
            "recommended_model": "LLaMA-2-7B-Chat INT8 on RTX4080",
            "metrics": {
                "Quality": "Best semantic preservation",
                "ROUGE-L": "0.409 (structure retention)",
                "Information": "Complete content capture",
                "Accuracy": "Highest among all models",
                "Speed": "9.61 tok/s acceptable for batch"
            },
            "performance": {
                "Max Quality": "Highest ROUGE scores",
                "Batch Size": "1-5 documents",
                "Processing Time": "2-5 min per document",
                "Output Quality": "Enterprise-grade"
            },
            "use_cases": ["Research Paper Summarization", "Document Processing", "Enterprise Solutions"]
        },
        "Mobile/Edge Deployment": {
            "icon": "Edge",
            "requirements": [
                "Minimal memory footprint (< 1GB VRAM)",
                "Energy efficiency critical",
                "Acceptable latency (1-2 seconds)",
                "On-device processing preferred"
            ],
            "recommended_model": "Qwen1.5-1.8B-Chat INT8 on RTX4070",
            "metrics": {
                "Memory": "Minimal footprint",
                "Speed": "Reasonable for edge",
                "Battery": "Low energy consumption",
                "Quality": "Acceptable quality",
                "Cost": "Low hardware requirements"
            },
            "performance": {
                "Device RAM": "6-8 GB sufficient",
                "Latency": "1-2 seconds acceptable",
                "Battery Impact": "Minimal drain",
                "Portability": "Easy deployment"
            },
            "use_cases": ["Mobile Apps", "Embedded Systems", "IoT Devices"]
        }
    }
    
    # Use case selector
    st.subheader("Select Use Case Scenario")
    selected_use_case = st.selectbox(
        "Choose your deployment scenario:",
        list(use_cases.keys()),
        format_func=lambda x: f"{use_cases[x]['icon']} {x}"
    )
    
    st.markdown("---")
    
    uc = use_cases[selected_use_case]
    
    # Main recommendation box
    st.markdown(f"## {uc['icon']} {selected_use_case}")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### Requirements")
        for req in uc['requirements']:
            st.write(req)
    
    with col2:
        st.markdown("### Recommended Configuration")
        st.markdown(f"**{uc['recommended_model']}**")
        
        # Get the recommended model data
        if "GPT-2" in uc['recommended_model'] and "RTX4080" in uc['recommended_model']:
            rec_data = results_df[(results_df['Model'] == 'GPT-2') & (results_df['GPU'] == 'RTX4080')].iloc[0]
        elif "Qwen" in uc['recommended_model'] and "RTX4080" in uc['recommended_model']:
            rec_data = results_df[(results_df['Model'] == 'Qwen1.5-1.8B-Chat') & (results_df['GPU'] == 'RTX4080')].iloc[0]
        elif "Qwen" in uc['recommended_model'] and "RTX4070" in uc['recommended_model']:
            rec_data = results_df[(results_df['Model'] == 'Qwen1.5-1.8B-Chat') & (results_df['GPU'] == 'RTX4070')].iloc[0]
        else:
            rec_data = results_df[(results_df['Model'] == 'LLaMA-2-7B-Chat') & (results_df['GPU'] == 'RTX4080')].iloc[0]
        
        st.metric("Composite Score", f"{rec_data['Composite_Score']:.4f}")
        st.metric("Throughput", f"{rec_data['Throughput_tok_s']:.2f} tok/s")
        st.metric("BLEU", f"{rec_data['BLEU']:.4f}")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Key Metrics")
        for metric_name, metric_val in uc['metrics'].items():
            st.write(f"**{metric_name}:** {metric_val}")
    
    with col2:
        st.markdown("### Expected Performance")
        for perf_name, perf_val in uc['performance'].items():
            st.write(f"**{perf_name}:** {perf_val}")
    
    with col3:
        st.markdown("### Typical Use Cases")
        for use in uc['use_cases']:
            st.write(f"• {use}")
    
    # Configuration code
    st.markdown("---")
    st.markdown("### Configuration Example")
    
    if "GPT-2" in uc['recommended_model']:
        config_code = """
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_8bit=True,
    device_map="auto"
)

generation_config = {
    'max_new_tokens': 100,
    'do_sample': True,
    'temperature': 0.7,
    'top_p': 0.9,
}

input_ids = tokenizer.encode("Hello, how are", return_tensors="pt")
outputs = model.generate(input_ids, **generation_config)
response = tokenizer.decode(outputs[0])
```
"""
    elif "Qwen" in uc['recommended_model']:
        config_code = """
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen1.5-1.8B-Chat"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_8bit=True,
    device_map="auto"
)

messages = [
    {"role": "user", "content": "Write a Python function to..."}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to("cuda")
generated_ids = model.generate(**model_inputs, max_new_tokens=512)
response = tokenizer.batch_decode(generated_ids)[0]
```
"""
    else:
        config_code = """
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_8bit=True,
    device_map="auto"
)

# High quality generation settings
generation_config = {
    'max_new_tokens': 512,
    'do_sample': True,
    'temperature': 0.3,
    'top_p': 0.95,
}

inputs = tokenizer.encode("Summarize this document", return_tensors="pt")
outputs = model.generate(inputs, **generation_config)
summary = tokenizer.decode(outputs[0])
```
"""
    
    st.markdown(config_code)

# ============================================================================
# PAGE 5: ABOUT
# ============================================================================
elif page == "About":
    st.markdown("---")
    
    st.markdown("## About This Analysis")
    
    st.markdown("""
    This dashboard presents a comprehensive analysis of INT8 quantization on Large Language Models (LLMs),
    based on the research by **Oprea & Bâra (2026)**.
    
    ### Research Objectives
    
    1. **Speed vs Quality Trade-offs**: Measure the impact of INT8 quantization on model performance
    2. **Multi-Architecture Evaluation**: Compare performance across GPT-2, Qwen, and LLaMA-2
    3. **Consumer Hardware Testing**: Analyze on accessible hardware (RTX4070, RTX4080)
    4. **Production-Ready Metrics**: Identify relevant metrics for real-world deployment
    5. **Model Selection Guidance**: Provide recommendations for different use cases
    
    ### Evaluation Metrics
    
    | Metric | Weight | Description |
    |--------|--------|-------------|
    | **Throughput** | 25% | Tokens per second - efficiency indicator |
    | **BLEU** | 15% | N-gram precision - phrase-level accuracy |
    | **ROUGE-1** | 20% | Unigram overlap - semantic recall |
    | **ROUGE-L** | 15% | Longest common subsequence - structure preservation |
    | **VRAM** | 15% | Memory usage - resource efficiency |
    | **GPU Residency** | 10% | Model in-memory status - availability |
    
    ### Models Tested
    
    - **GPT-2** - Smaller, lightweight model
    - **Qwen1.5-1.8B-Chat** - Efficient chat model
    - **LLaMA-2-7B-Chat** - Larger, higher quality model
    
    ### Hardware Configurations
    
    - **RTX4080** - High-end consumer GPU (16GB VRAM)
    - **RTX4070** - Mid-range consumer GPU (12GB VRAM)
    
    ### Methodology
    
    **Multi-Criteria Scoring Framework:**
    - Max-min normalization to [0, 1] scale
    - Weighted average of 6 metrics
    - Transparency and reproducibility focused
    - Bias-minimized approach
    
    ### Data Sources
    
    - Table 3: Timing metrics and throughput
    - Table 6: Single prompt BLEU/ROUGE scores
    - Table 7-11: Model vs human reference comparisons
    - Table 13: Code generation metrics
    
    ### Key Findings
    - INT8 quantization can improve memory efficiency and throughput.
    - Model selection depends heavily on use case requirements.
    - Hardware efficiency enables edge deployment.
    - Cost-performance trade-offs are measurable.
    
    ### References
    
    - Oprea & Bâra (2026). INT8 Quantization Analysis for LLMs
    - Research conducted: 2025-2026
    - Dataset: 50+ prompts per configuration
    - Configurations: 6 model-GPU combinations
    
    ---
    
    **Built with Streamlit** | Cloudflare Pages + Hugging Face Spaces
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Dataset Summary")
        st.write(f"**Total Configurations:** {len(results_df)}")
        st.write(f"**Models Tested:** {results_df['Model'].nunique()}")
        st.write(f"**GPU Types:** {results_df['GPU'].nunique()}")
        st.write(f"**Avg Composite Score:** {results_df['Composite_Score'].mean():.4f}")
    
    with col2:
        st.markdown("### Links")
        st.write("[Full Paper & Analysis](https://doi.org/10.32604/cmc.2026.078985)")
        st.write("[Project Repository](https://github.com/PVegananda/llm-quantization-benchmark)")
        st.write("[Cloudflare Pages Demo](https://pasyahvegananda-benchmark-kuantisasi-llm.pages.dev)")
        st.write("[Hugging Face Spaces](https://huggingface.co/spaces)")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding: 20px; color: #666;'>
        <p>LLM Quantization Benchmark Analysis | Based on Oprea & Bâra (2026) | Built with Streamlit</p>
        <p>Interactive Dashboard | Deployed on Hugging Face Spaces</p>
    </div>
""", unsafe_allow_html=True)
