# Intelligent RAG Model Router  
### Adaptive LLM Selection for Faster, Smarter Question Answering

This project enhances the open-source RAG system **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** with an **Intelligent Model Router** that dynamically selects the optimal local LLM based on question type — achieving up to **95% faster responses** for simple queries with minimal quality trade-off.

Built for the **COMP S333F (Advanced Programming and AI Algorithms)** course at **Hong Kong Metropolitan University**.

---

## 🎯 Problem
AnythingLLM uses a **static, workspace-level LLM** for all queries — whether asking *“What is PEAS?”* or *“Analyze medical diagnosis environment”*. This leads to:
- **Wasted latency** on simple factual questions (using slow, high-quality models unnecessarily)
- **No quality boost** for complex analytical tasks (if a weaker model is selected)

---

## 💡 Solution: Dual-Layer Architecture

### 1. **Semantic RAG Pipeline** *(by Mike)*
- Grounds answers in the official **Lab 3 solution document** (15 ground-truth Q&A pairs)
- Uses **`BAAI/bge-m3` embeddings** + **K-means clustering (K=5–14)** for semantic retrieval
- Evaluates answer quality using **semantic similarity + ROUGE-L F1**

### 2. **Intelligent Model Router** *(by Maria)*
- Classifies queries as **Simple**, **Explanatory**, or **Technical**
- Dynamically routes to the best local LLM:
  - `llama2-chinese` → **Fast** (1.7s) for simple facts
  - `deepseek-r1:32b` → **Balanced** for explanations
  - `gpt-oss:20b` → **High-quality** (0.73 score) for analytical tasks

> ✨ **No modification to AnythingLLM core** — works as an external pre-processing layer.

---

## 📊 Key Results
| Query Type | Model | Avg Time | Final Score |
|-----------|-------|----------|-------------|
| Simple (e.g., “Is poker static?”) | `llama2-chinese` | **1.7s** | 0.60 |
| Analytical (e.g., “Medical diagnosis dimensions”) | `gpt-oss:20b` | **13.6s** | **0.73** |
| **Overall speedup** | — | **95% faster** | <0.07 quality drop |

> Evaluated across **15 Lab 3 questions**, **3 LLMs**, and **K=5–14 clustering configs** (450+ runs).

---

## ⚙️ Tech Stack
- **RAG Framework**: AnythingLLM (v1.9.0) + Ollama
- **Embeddings**: `BAAI/bge-m3` (1024-dim semantic vectors)
- **Clustering**: K-means (scikit-learn)
- **LLMs**: `gpt-oss:20b`, `deepseek-r1:32b`, `llama2-chinese`
- **Evaluation**: Semantic similarity, ROUGE-L F1, weighted final score (`0.6*semantic + 0.4*rouge`)
- **Hardware**: Windows 11, RTX 5060, 32GB RAM

---

## 🚀 Quick Start
1. **Install Ollama** and pull required models:
   ```bash
   ollama pull gpt-oss:20b
   ollama pull deepseek-r1:32b
   ollama pull llama2-chinese

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the evaluation
   ```bash
   python rag_qa_bgem3_eval.py
