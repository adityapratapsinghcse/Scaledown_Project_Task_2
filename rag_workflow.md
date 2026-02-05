# Retrieval-Augmented Generation (RAG) Workflow

## What is RAG?
Retrieval-Augmented Generation (RAG) is an AI technique that combines:
- Information retrieval from external data sources
- Natural language generation using Large Language Models (LLMs)

This approach prevents hallucinations and ensures responses are grounded in real data.

---

## Why RAG is Used in This Project
Traditional AI models rely on pre-trained knowledge, which is unsuitable for:
- Private resumes
- Dynamic job requirements
- Hiring decisions

RAG ensures that all evaluations are strictly based on candidate data.

---

## Step-by-Step RAG Workflow

### Step 1: Resume & Job Description Input
- Recruiter uploads multiple resumes
- Recruiter provides a job description

---

### Step 2: Compression
- Each document is compressed using an LLM
- Only hiring-relevant attributes are retained
- Output is concise and structured

---

### Step 3: Embedding
- Compressed summaries are converted into embeddings
- Embeddings capture semantic meaning rather than keywords

---

### Step 4: Vector Storage
- Embeddings are stored in FAISS vector database
- Each resume is indexed independently

---

### Step 5: Retrieval
- Job description is embedded as a query
- Top-K most relevant resumes are retrieved
- Irrelevant candidates are filtered out

---

### Step 6: Generation
- Retrieved resumes + job description are passed to the LLM
- A strict RAG prompt ensures:
  - No hallucinations
  - Context-only reasoning

---

## Output Format
The RAG system produces:
- Match Score (0–100)
- Matching Skills
- Missing Skills
- Experience Alignment
- Risk Factors
- Final Recommendation

---

## Benefits of RAG in Recruitment
- Accurate matching
- Explainable decisions
- Reduced bias
- Improved recruiter trust

---

## Summary
RAG enables reliable, transparent, and scalable AI-driven candidate screening
by grounding all decisions in retrieved candidate data.
