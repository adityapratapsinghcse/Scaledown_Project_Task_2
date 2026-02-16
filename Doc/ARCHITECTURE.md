# System Architecture

### Overview
### Flow Description
1. **Resume Upload** – User uploads a `.txt` file  
2. **RAGBackend** – Handles API calls and semantic matching  
3. **ScaleDown Compression** – Compresses resumes into a dense technical summary  
4. **Embeddings** – Generates vector embeddings using `SentenceTransformer`  
5. **Semantic Matching** – Computes cosine similarity between job description and resume embeddings  
6. **UI Display** – Shows metrics: similarity score, matching skills, missing skills, experience
