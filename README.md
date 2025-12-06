# Intelligent RAG Model Router  
### Adaptive LLM Selection for Faster, Smarter Question Answering

This project enhances the open-source RAG system **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** with an **Intelligent Model Router** that dynamically selects the optimal local LLM based on question type — achieving up to **95% faster responses** for simple queries with minimal quality trade-off.

Built for the **COMP S333F (Advanced Programming and AI Algorithms)** course at **Hong Kong Metropolitan University**.

> 🔗 **Note**: This repository contains **Maria's Intelligent Model Router**.  
> For **Mike’s Semantic RAG Pipeline & Evaluation**, see: [https://github.com/Mikeahhh/RAG-K-Means-Clustering-Experiment-COMP-4330SEF-S333F-](https://github.com/Mikeahhh/RAG-K-Means-Clustering-Experiment-COMP-4330SEF-S333F-)

---

## 🎯 Problem
AnythingLLM uses a **static, workspace-level LLM** for all queries — whether asking *“What is PEAS?”* or *“Analyze medical diagnosis environment”*. This leads to:
- **Wasted latency** on simple factual questions (using slow, high-quality models unnecessarily)
- **No quality boost** for complex analytical tasks (if a weaker model is selected)

---

## 💡 Solution: Dual-Layer Architecture (Two Repositories)

### 1. **Semantic RAG Pipeline** *(by Mike)*  
> 📁 **[GitHub: Mikeahhh/RAG-K-Means...](https://github.com/Mikeahhh/RAG-K-Means-Clustering-Experiment-COMP-4330SEF-S333F-)**  
- Grounds answers in the official **Lab 3 solution document** (15 ground-truth Q&A pairs)
- Uses **`BAAI/bge-m3` embeddings** + **K-means clustering (K=5–14)** for semantic retrieval
- Evaluates answer quality using **semantic similarity + ROUGE-L F1**

### 2. **Intelligent Model Router** *(by Maria)*  
> 📁 **This Repository**  
- Classifies queries as **Simple**, **Explanatory**, or **Technical**
- Dynamically routes to the best local LLM:
  - `llama2-chinese` → **Fast** (1.7s) for simple facts  
  - `deepseek-r1:32b` → **Balanced** for explanations  
  - `gpt-oss:20b` → **High-quality** (0.73 score) for analytical tasks  

> ✨ **No modification to AnythingLLM core** — works as an external pre-processing layer.

---

## 📊 Key Results (From Combined Evaluation)
| Query Type | Model | Avg Time | Final Score |
|-----------|-------|----------|-------------|
| Simple (e.g., “Is poker static?”) | `llama2-chinese` | **1.7s** | 0.60 |
| Analytical (e.g., “Medical diagnosis dimensions”) | `gpt-oss:20b` | **13.6s** | **0.73** |
| **Overall speedup** | — | **95% faster** | <0.07 quality drop |

> Evaluated across **15 Lab 3 questions**, **3 LLMs**, and **K=5–14 clustering configs** (450+ runs).

---

## 🛠️ Tech Stack (This Repository)
- **Router Logic**: Rule-based classifier (Python)
- **LLMs Supported**: `gpt-oss:20b`, `deepseek-r1:32b`, `llama2-chinese`
- **Integration**: Simulated API calls to AnythingLLM
- **Hardware**: Tested on Windows 11, RTX 5060, 32GB RAM

---

## 🚀 Quick Start
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
2. **Run the router demo**:
   ```bash
   python ImprovedRouter.py
3. **See integration simulation**:
   ```bash
    python integration_demo.py
   ```
---

🙏 **Acknowledgements**
The design of the Intelligent Model Router was inspired by the dynamic model routing logic in the open-source project PatioAI (https://github.com/AKIFQ/patioai?spm=a2ty_o01.29997173.0.0.7e545171LtLBlL).
This project adapts and extends that idea into a quantitatively evaluated, query-aware router for Retrieval-Augmented Generation (RAG) systems.

📚 **References**
- AnythingLLM (https://github.com/Mintplex-Labs/anything-llm?spm=a2ty_o01.29997173.0.0.7e545171LtLBlL)
- BGE-M3 Embeddings (https://huggingface.co/BAAI/bge-m3?spm=a2ty_o01.29997173.0.0.7e545171LtLBlL)
- Asai et al. (2023). Self-RAG (https://arxiv.org/abs/2310.11511?spm=a2ty_o01.29997173.0.0.7e545171LtLBlL&file=2310.11511)


