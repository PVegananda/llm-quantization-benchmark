// Data for models
const modelsData = [
    { rank: 1, model: "GPT-2 INT8", gpu: "RTX4080", score: 0.7234, throughput: 127.36, bleu: 0.6821, rouge1: 0.7234, rougeL: 0.6987, memory: 2.3 },
    { rank: 2, model: "GPT-2 INT8", gpu: "RTX4070", score: 0.6891, throughput: 103.21, bleu: 0.6821, rouge1: 0.7234, rougeL: 0.6987, memory: 2.3 },
    { rank: 3, model: "Qwen1.5-1.8B INT8", gpu: "RTX4080", score: 0.6745, throughput: 87.45, bleu: 0.7123, rouge1: 0.7456, rougeL: 0.7234, memory: 4.5 },
    { rank: 4, model: "Qwen1.5-1.8B INT8", gpu: "RTX4070", score: 0.6234, throughput: 64.32, bleu: 0.7123, rouge1: 0.7456, rougeL: 0.7234, memory: 4.5 },
    { rank: 5, model: "LLaMA-2-7B INT8", gpu: "RTX4080", score: 0.5234, throughput: 45.67, bleu: 0.7987, rouge1: 0.8123, rougeL: 0.7987, memory: 10.2 },
    { rank: 6, model: "LLaMA-2-7B INT8", gpu: "RTX4070", score: 0.4123, throughput: 28.34, bleu: 0.7987, rouge1: 0.8123, rougeL: 0.7987, memory: 10.2 }
];

// Use cases with detailed explanations
const useCases = {
    chat: {
        titleEn: "Real-Time Chat Applications",
        titleId: "Aplikasi Chat Real-Time",
        recommendationEn: "GPT-2 INT8 on RTX4080",
        recommendationId: "GPT-2 INT8 di RTX4080",
        scoreEn: "Score: 0.7234",
        scoreId: "Skor: 0.7234",
        throughputEn: "127 tokens/sec (0.4s per 50-word response)",
        throughputId: "127 token/detik (0.4 detik per respons 50-kata)",
        reasoningEn: [
            "Fastest response time ensures responsive chat experience",
            "Small model (125M params) uses minimal VRAM (2.3 GB)",
            "Quality remains high (78% ROUGE-1) for conversational tasks",
            "Cost-effective - can run on mid-range consumer GPUs",
            "Perfect for web servers handling multiple concurrent users"
        ],
        reasoningId: [
            "Waktu respons tercepat memastikan pengalaman chat responsif",
            "Model kecil (125M params) menggunakan VRAM minimal (2.3 GB)",
            "Kualitas tetap tinggi (78% ROUGE-1) untuk tugas percakapan",
            "Cost-effective - dapat berjalan pada GPU konsumen mid-range",
            "Sempurna untuk server web menangani banyak pengguna bersamaan"
        ],
        configEn: { "Model": "GPT-2 (125M)", "GPU": "RTX4080", "VRAM": "2.3 GB", "Throughput": "127 tok/sec", "Quality": "72%" },
        configId: { "Model": "GPT-2 (125M)", "GPU": "RTX4080", "VRAM": "2.3 GB", "Throughput": "127 tok/detik", "Kualitas": "72%" }
    },
    code: {
        titleEn: "Code Generation & Completion",
        titleId: "Pembuatan & Penyelesaian Kode",
        recommendationEn: "Qwen1.5-1.8B INT8 on RTX4080",
        recommendationId: "Qwen1.5-1.8B INT8 di RTX4080",
        scoreEn: "Score: 0.6745",
        scoreId: "Skor: 0.6745",
        throughputEn: "87 tokens/sec (0.6s per 50-word response)",
        throughputId: "87 token/detik (0.6 detik per respons 50-kata)",
        reasoningEn: [
            "Qwen trained on diverse code datasets - better code understanding",
            "Higher BLEU score (71.2%) captures syntax precision better",
            "Balances speed (87 tok/sec) with quality (74.6% ROUGE-1)",
            "Moderate VRAM (4.5 GB) still fits in RTX4070+",
            "Industry use case from the Oprea & Bâra benchmark"
        ],
        reasoningId: [
            "Qwen dilatih pada dataset kode beragam - pemahaman kode lebih baik",
            "Skor BLEU lebih tinggi (71.2%) menangkap presisi sintaks lebih baik",
            "Menyeimbangkan kecepatan (87 tok/detik) dengan kualitas (74.6% ROUGE-1)",
            "VRAM sedang (4.5 GB) masih cocok untuk RTX4070+",
            "Kasus penggunaan industri dari benchmark Oprea & Bâra"
        ],
        configEn: { "Model": "Qwen1.5 (1.8B)", "GPU": "RTX4080", "VRAM": "4.5 GB", "Throughput": "87 tok/sec", "Quality": "74%" },
        configId: { "Model": "Qwen1.5 (1.8B)", "GPU": "RTX4080", "VRAM": "4.5 GB", "Throughput": "87 tok/detik", "Kualitas": "74%" }
    },
    batch: {
        titleEn: "Batch Processing (Summarization)",
        titleId: "Pemrosesan Batch (Peringkasan)",
        recommendationEn: "GPT-2 INT8 on RTX4080",
        recommendationId: "GPT-2 INT8 di RTX4080",
        scoreEn: "Score: 0.7234",
        scoreId: "Skor: 0.7234",
        throughputEn: "127 tokens/sec (process 10,000 documents in ~2 hours)",
        throughputId: "127 token/detik (memproses 10.000 dokumen dalam ~2 jam)",
        reasoningEn: [
            "Batch processing not latency-sensitive - throughput matters most",
            "GPT-2's speed (127 tok/sec) processes documents fastest",
            "High quality (72.3% ROUGE-1) sufficient for summarization",
            "Can process large document collections cost-effectively",
            "Proven in production use from journal benchmark data"
        ],
        reasoningId: [
            "Pemrosesan batch tidak sensitif latensi - throughput paling penting",
            "Kecepatan GPT-2 (127 tok/detik) memproses dokumen paling cepat",
            "Kualitas tinggi (72.3% ROUGE-1) cukup untuk peringkasan",
            "Dapat memproses koleksi dokumen besar dengan cost-effective",
            "Terbukti dalam penggunaan produksi dari data benchmark jurnal"
        ],
        configEn: { "Model": "GPT-2 (125M)", "GPU": "RTX4080", "VRAM": "2.3 GB", "Throughput": "127 tok/sec", "Quality": "72%" },
        configId: { "Model": "GPT-2 (125M)", "GPU": "RTX4080", "VRAM": "2.3 GB", "Throughput": "127 tok/detik", "Kualitas": "72%" }
    },
    edge: {
        titleEn: "Edge Devices & Mobile",
        titleId: "Perangkat Edge & Mobile",
        recommendationEn: "Qwen1.5-1.8B INT8 on RTX4070",
        recommendationId: "Qwen1.5-1.8B INT8 di RTX4070",
        scoreEn: "Score: 0.6234",
        scoreId: "Skor: 0.6234",
        throughputEn: "64 tokens/sec (good for constrained devices)",
        throughputId: "64 token/detik (bagus untuk perangkat terbatas)",
        reasoningEn: [
            "RTX4070 (12GB VRAM) representative of consumer-grade edge GPUs",
            "Qwen1.5 (1.8B) fits within memory constraints (4.5 GB needed)",
            "Quality-speed tradeoff (62.3% score) optimal for edge use",
            "Still responsive for user interaction (64 tok/sec)",
            "Edge computing node case study from the research"
        ],
        reasoningId: [
            "RTX4070 (12GB VRAM) mewakili GPU edge grade konsumen",
            "Qwen1.5 (1.8B) cocok dalam batasan memori (4.5 GB diperlukan)",
            "Trade-off kualitas-kecepatan (skor 62.3%) optimal untuk edge",
            "Masih responsif untuk interaksi pengguna (64 tok/detik)",
            "Studi kasus komputasi edge dari penelitian"
        ],
        configEn: { "Model": "Qwen1.5 (1.8B)", "GPU": "RTX4070", "VRAM": "4.5 GB", "Throughput": "64 tok/sec", "Quality": "62%" },
        configId: { "Model": "Qwen1.5 (1.8B)", "GPU": "RTX4070", "VRAM": "4.5 GB", "Throughput": "64 tok/detik", "Kualitas": "62%" }
    },
    premium: {
        titleEn: "Premium Quality (Complex Tasks)",
        titleId: "Kualitas Premium (Tugas Kompleks)",
        recommendationEn: "LLaMA-2-7B INT8 on RTX4080",
        recommendationId: "LLaMA-2-7B INT8 di RTX4080",
        scoreEn: "Score: 0.5234",
        scoreId: "Skor: 0.5234",
        throughputEn: "45 tokens/sec (acceptable for complex problem-solving)",
        throughputId: "45 token/detik (dapat diterima untuk pemecahan masalah kompleks)",
        reasoningEn: [
            "Highest quality model - 81.2% ROUGE-1, 79.9% BLEU score",
            "LLaMA-2-7B designed for complex reasoning and analysis",
            "Speed still acceptable (45 tok/sec) for quality-critical tasks",
            "RTX4080 required (10.2 GB VRAM) but worth the investment",
            "Professional/research use case from benchmark evaluation"
        ],
        reasoningId: [
            "Model berkualitas tertinggi - 81.2% ROUGE-1, skor BLEU 79.9%",
            "LLaMA-2-7B dirancang untuk penalaran dan analisis kompleks",
            "Kecepatan masih dapat diterima (45 tok/detik) untuk tugas kritis kualitas",
            "RTX4080 diperlukan (VRAM 10.2 GB) tetapi layak investasi",
            "Kasus penggunaan profesional/penelitian dari evaluasi benchmark"
        ],
        configEn: { "Model": "LLaMA-2 (7B)", "GPU": "RTX4080", "VRAM": "10.2 GB", "Throughput": "45 tok/sec", "Quality": "81%" },
        configId: { "Model": "LLaMA-2 (7B)", "GPU": "RTX4080", "VRAM": "10.2 GB", "Throughput": "45 tok/detik", "Kualitas": "81%" }
    },
    research: {
        titleEn: "Research & Benchmarking",
        titleId: "Penelitian & Benchmarking",
        recommendationEn: "All Models (Comparative Study)",
        recommendationId: "Semua Model (Studi Komparatif)",
        scoreEn: "Multiple configurations",
        scoreId: "Konfigurasi ganda",
        throughputEn: "Wide range: 28-127 tokens/sec",
        throughputId: "Jangkauan luas: 28-127 token/detik",
        reasoningEn: [
            "Researchers need comprehensive comparison across all model-GPU pairs",
            "This benchmark provides all 6 configurations for statistical analysis",
            "Can measure scalability from 125M to 7B parameters",
            "Evaluate quantization impact across different model sizes",
            "Foundation for future research on quantization techniques"
        ],
        reasoningId: [
            "Peneliti membutuhkan perbandingan komprehensif di semua pasangan model-GPU",
            "Benchmark ini menyediakan semua 6 konfigurasi untuk analisis statistik",
            "Dapat mengukur skalabilitas dari 125M hingga 7B parameter",
            "Evaluasi dampak kuantisasi di berbagai ukuran model",
            "Fondasi untuk penelitian masa depan tentang teknik kuantisasi"
        ],
        configEn: { "Analysis": "6 configurations", "Models": "3 sizes", "GPUs": "2 variants", "Metrics": "6 measures", "Scale": "Full study" },
        configId: { "Analisis": "6 konfigurasi", "Model": "3 ukuran", "GPU": "2 varian", "Metrik": "6 ukuran", "Skala": "Studi penuh" }
    }
};

// Language switching
function setupLanguageToggle() {
    const buttons = document.querySelectorAll('.lang-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const lang = btn.dataset.lang;
            document.body.className = `lang-${lang}`;
            localStorage.setItem('language', lang);
            
            // Update active button
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });
    
    // Load saved language preference
    const saved = localStorage.getItem('language') || 'en';
    document.body.className = `lang-${saved}`;
    buttons.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === saved);
    });
}

// Tab switching
function initializeTabs() {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const tabName = link.dataset.tab;
            showTab(tabName);
        });
    });
}

function showTab(tabName) {
    const contents = document.querySelectorAll('.tab-content');
    const links = document.querySelectorAll('.nav-link');
    
    contents.forEach(content => content.classList.remove('active'));
    links.forEach(link => link.classList.remove('active'));
    
    document.getElementById(tabName).classList.add('active');
    document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');
}

// Populate results table
function initializeResultsTable() {
    populateTable(modelsData);
    
    // Filter buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.dataset.filter;
            if (filter === 'all') {
                populateTable(modelsData);
            } else {
                populateTable(modelsData.filter(m => m.gpu === filter));
            }
        });
    });
    
    // Sort dropdown
    document.getElementById('sortSelect').addEventListener('change', (e) => {
        const sortBy = e.target.value;
        const filtered = Array.from(modelsData);
        if (sortBy === 'score') filtered.sort((a, b) => b.score - a.score);
        else if (sortBy === 'throughput') filtered.sort((a, b) => b.throughput - a.throughput);
        else if (sortBy === 'bleu') filtered.sort((a, b) => b.bleu - a.bleu);
        populateTable(filtered);
    });
    
    // Search
    document.getElementById('searchInput').addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const filtered = modelsData.filter(m => 
            m.model.toLowerCase().includes(query) || m.gpu.toLowerCase().includes(query)
        );
        populateTable(filtered);
    });
}

function populateTable(data) {
    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = '';
    data.forEach(model => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${model.rank}</td>
            <td>${model.model}</td>
            <td>${model.gpu}</td>
            <td>${model.score.toFixed(4)}</td>
            <td>${model.throughput.toFixed(2)}</td>
            <td>${model.bleu.toFixed(4)}</td>
            <td>${model.rouge1.toFixed(4)}</td>
            <td>${model.rougeL.toFixed(4)}</td>
            <td>${model.memory.toFixed(1)}</td>
        `;
    });
    
    // Display top 3
    displayTop3(data.slice(0, 3));
}

function displayTop3(topModels) {
    const container = document.getElementById('topModels');
    container.innerHTML = '';
    const medals = ['🥇', '🥈', '🥉'];
    topModels.forEach((model, idx) => {
        const card = document.createElement('div');
        card.style.cssText = 'background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px; text-align: center;';
        card.innerHTML = `
            <div style="font-size: 2rem; margin-bottom: 10px;">${medals[idx]}</div>
            <h4>${model.model}</h4>
            <p><strong>${model.gpu}</strong></p>
            <p><strong>Score:</strong> ${model.score.toFixed(4)}</p>
            <p><strong>Throughput:</strong> ${model.throughput.toFixed(2)} tok/sec</p>
        `;
        container.appendChild(card);
    });
}

// Initialize use cases
function initializeUseCases() {
    const container = document.getElementById('useCasesContainer');
    container.innerHTML = '';
    
    Object.entries(useCases).forEach(([key, useCase]) => {
        const card = document.createElement('div');
        card.style.cssText = 'background: white; border: 2px solid #e5e7eb; border-radius: 8px; padding: 20px; cursor: pointer; transition: all 0.3s;';
        card.className = 'use-case-card';
        card.innerHTML = `
            <div class="en-content"><h3>${useCase.titleEn}</h3></div>
            <div class="id-content"><h3>${useCase.titleId}</h3></div>
            <p class="en-content"><strong>Recommended:</strong> ${useCase.recommendationEn}</p>
            <p class="id-content"><strong>Direkomendasikan:</strong> ${useCase.recommendationId}</p>
        `;
        card.addEventListener('click', () => showUseCaseResult(key));
        card.addEventListener('mouseenter', () => card.style.transform = 'translateY(-5px)');
        card.addEventListener('mouseleave', () => card.style.transform = 'translateY(0)');
        container.appendChild(card);
    });
}

function showUseCaseResult(usecaseKey) {
    const useCase = useCases[usecaseKey];
    const modal = document.getElementById('usecaseModal');
    const title = document.getElementById('modalTitle');
    const body = document.getElementById('modalBody');
    
    const lang = document.body.className.includes('lang-id') ? 'id' : 'en';
    const titleKey = lang === 'id' ? 'titleId' : 'titleEn';
    const recKey = lang === 'id' ? 'recommendationId' : 'recommendationEn';
    const scoreKey = lang === 'id' ? 'scoreId' : 'scoreEn';
    const throughputKey = lang === 'id' ? 'throughputId' : 'throughputEn';
    const reasoningKey = lang === 'id' ? 'reasoningId' : 'reasoningEn';
    const configKey = lang === 'id' ? 'configId' : 'configEn';
    
    title.innerHTML = `<div class="en-content">${useCase.titleEn}</div><div class="id-content">${useCase.titleId}</div>`;
    
    let configHtml = '<table style="width: 100%; margin-top: 10px;"><tr style="background: #f0f9ff;">';
    Object.entries(useCase[configKey]).forEach(([k, v]) => {
        configHtml += `<th style="padding: 10px;">${k}</th>`;
    });
    configHtml += '</tr><tr>';
    Object.values(useCase[configKey]).forEach(v => {
        configHtml += `<td style="padding: 10px; text-align: center;">${v}</td>`;
    });
    configHtml += '</tr></table>';
    
    body.innerHTML = `
        <div class="en-content">
            <p><strong>${useCase[recKey]}</strong></p>
            <p>${useCase[scoreKey]}</p>
            <p>${useCase[throughputKey]}</p>
            <h4>Why this recommendation:</h4>
            <ul>
                ${useCase[reasoningKey].map(r => `<li>${r}</li>`).join('')}
            </ul>
            ${configHtml}
        </div>
        <div class="id-content">
            <p><strong>${useCase[recKey]}</strong></p>
            <p>${useCase[scoreKey]}</p>
            <p>${useCase[throughputKey]}</p>
            <h4>Mengapa rekomendasi ini:</h4>
            <ul>
                ${useCase[reasoningKey].map(r => `<li>${r}</li>`).join('')}
            </ul>
            ${configHtml}
        </div>
    `;
    
    modal.style.display = 'block';
}

function closeUseCaseModal() {
    document.getElementById('usecaseModal').style.display = 'none';
}

// Close modal on background click
window.addEventListener('click', (e) => {
    const modal = document.getElementById('usecaseModal');
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});

// Deployment tabs
function initializeDeployment() {
    const buttons = document.querySelectorAll('.deploy-tab-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            buttons.forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.deploy-tab-content').forEach(c => c.classList.remove('active'));
            btn.classList.add('active');
            const tabId = btn.dataset.deployTab;
            document.getElementById(tabId).classList.add('active');
        });
    });
}

// Copy to clipboard
function copyCode(button) {
    const codeBlock = button.previousElementSibling;
    if (!codeBlock || !codeBlock.textContent) {
        const parent = button.closest('pre');
        if (parent) {
            const code = parent.textContent;
            navigator.clipboard.writeText(code).then(() => {
                button.textContent = 'Copied!';
                setTimeout(() => {
                    button.textContent = 'Copy';
                }, 2000);
            });
        }
        return;
    }
    
    const code = codeBlock.textContent;
    navigator.clipboard.writeText(code).then(() => {
        button.textContent = 'Copied!';
        setTimeout(() => {
            button.textContent = 'Copy';
        }, 2000);
    });
}

// FAQ functionality
function initializeFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
            const answer = item.querySelector('.faq-answer');
            answer.style.maxHeight = answer.style.maxHeight ? null : answer.scrollHeight + 'px';
            answer.style.overflow = 'hidden';
            answer.style.transition = 'max-height 0.3s ease-out';
        });
    });
}

// Initialize everything
document.addEventListener('DOMContentLoaded', () => {
    setupLanguageToggle();
    initializeTabs();
    initializeResultsTable();
    initializeUseCases();
    initializeDeployment();
    initializeFAQ();
    
    // Add copy buttons to code blocks
    document.querySelectorAll('pre').forEach(pre => {
        if (!pre.querySelector('button')) {
            const button = document.createElement('button');
            button.textContent = 'Copy';
            button.style.cssText = 'position: absolute; right: 10px; top: 10px; padding: 5px 10px; background: #667eea; color: white; border: none; border-radius: 4px; cursor: pointer;';
            pre.style.position = 'relative';
            pre.appendChild(button);
            button.addEventListener('click', () => {
                const code = pre.querySelector('code').textContent;
                navigator.clipboard.writeText(code).then(() => {
                    button.textContent = 'Copied!';
                    setTimeout(() => {
                        button.textContent = 'Copy';
                    }, 2000);
                });
            });
        }
    });
});
