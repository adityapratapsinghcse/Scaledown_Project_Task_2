# Modules

### 1. app.py
- Streamlit frontend
- Handles workflow steps, buttons, and displays
- Manages session state

### 2. rag_pipeline.py
- RAG backend
- Handles resume compression and semantic matching
- Contains `RAGBackend` class

### 3. embeddings.py
- Generates embeddings using `all-MiniLM-L6-v2`
- Computes cosine similarity between vectors

### 4. resume_compression.py
- Integrates with ScaleDown API
- Compresses resume text
- Provides fallback if compression fails

### 5. requirements.txt
- Lists all dependencies
