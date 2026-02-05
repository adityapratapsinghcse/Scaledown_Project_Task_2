# System Architecture

## Overview
The Recruitment Screening Agent is designed using a modular, scalable architecture
based on Retrieval-Augmented Generation (RAG). The system processes resumes and job
descriptions, compresses them to reduce cost, stores semantic representations in a
vector database, and generates explainable candidate-job matching results.

The architecture prioritizes:
- Cost efficiency
- Explainability
- Scalability
- Data privacy

---

## High-Level Architecture

User → UI Layer → Compression Layer → Embedding Layer → Vector Database  
→ Retrieval Layer → RAG Evaluation Layer → Structured Output

---

## Component Breakdown

### 1. User Interface Layer
- Built using Streamlit
- Allows recruiters to:
  - Upload resumes
  - Enter job descriptions
  - Trigger candidate screening
- Displays structured evaluation results

---

### 2. Document Ingestion Layer
- Loads resumes and job descriptions from local storage
- Supports text and PDF formats
- Performs text normalization:
  - Removes formatting noise
  - Cleans irrelevant metadata

---

### 3. Compression Layer (Core Innovation)
- Uses an LLM to compress documents before embedding
- Extracts only relevant hiring information:
  - Skills
  - Technologies
  - Experience
  - Education
  - Certifications
- Eliminates redundant and verbose content
- Significantly reduces token usage and cost

---

### 4. Embedding Layer
- Converts compressed summaries into dense vector embeddings
- Uses OpenAI-compatible embedding models
- Ensures semantic representation instead of keyword-based matching

---

### 5. Vector Database Layer
- Uses FAISS for efficient similarity search
- Stores embeddings of compressed resumes
- Enables fast top-K retrieval

---

### 6. Retrieval Layer
- Retrieves the most relevant candidate profiles
- Uses semantic similarity based on job description queries
- Prevents irrelevant candidate matches

---

### 7. RAG Evaluation Layer
- Combines retrieved candidate summaries with the job description
- Uses a strict RAG prompt to ensure context-only reasoning
- Produces explainable hiring decisions

---

## Output
The system generates structured results including:
- Match score
- Matching skills
- Missing skills
- Experience alignment
- Final hiring recommendation

---

## Scalability Considerations
- Modular pipeline allows easy extension
- Vector database supports large resume datasets
- Compression reduces storage and inference overhead

---

## Conclusion
This architecture ensures an efficient, explainable, and production-ready recruitment
screening system using modern RAG techniques.
