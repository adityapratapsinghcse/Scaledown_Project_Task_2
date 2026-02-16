# Scaledown_Project_Task_2
Its a Project made Under the Intels Unnati Program With Integration of Scaledown APIs

# Scaledown Project Task 2 🚀

**🔎 Project Overview**  
This repository contains **Task 2 of the Scaledown Project**, developed as part of the *Intel Unnati Program*. The objective of this task was to integrate **Scaledown APIs** into a working project solution.

---

# 🎯 RAG Candidate Screening System

A robust Resume-Augmented Generation (RAG) pipeline built with **Streamlit** and **ScaleDown API** for automatically compressing resumes and matching them with job descriptions using semantic embeddings.

---

## **Features**

1. **Resume Ingestion**
   - Upload plain text resumes (`.txt` files)
   - Supports fallback if compression fails

2. **Resume Compression**
   - Uses ScaleDown API to summarize resumes into a dense technical profile
   - Fallback to original resume if compression fails

3. **Semantic Matching**
   - Calculates similarity score between job description and resume using `SentenceTransformer` embeddings (`all-MiniLM-L6-v2`)

4. **Stepwise Streamlit Workflow**
   - Step 1: Resume upload
   - Step 2: Compression and optimization metrics
   - Step 3: Paste job description
   - Step 4: Similarity score and evaluation metrics

5. **Robust & User-Friendly**
   - Metrics: compression ratio, latency
   - Prevents the “AI stuck in loop” issue
   - Fully works even if ScaleDown API returns empty text

---

## **Installation**

1. Clone the repository:

```bash
https://github.com/adityapratapsinghcse/Scaledown_Project_Task_2.git
---
