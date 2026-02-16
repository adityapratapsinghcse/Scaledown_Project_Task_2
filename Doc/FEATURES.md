# Features

### 1. Resume Ingestion
- Upload plain text (`.txt`) resumes
- Works with resumes of any length
- Stored in Streamlit session state

### 2. Resume Compression
- Uses ScaleDown API to summarize resumes
- Extracts work experience, skills, and projects
- Fallback to original resume if compression fails
- Displays compression ratio and latency

### 3. Semantic Matching
- Accepts job descriptions in text form
- Converts JD and resume into embeddings
- Calculates cosine similarity (0-100%)
- Shows a matching score for candidate-job fit

### 4. Stepwise Workflow
1. Upload resume  
2. Compress resume  
3. Paste job description  
4. View similarity score and evaluation metrics

### 5. Robustness and UI
- Handles empty or malformed resumes
- Prevents “AI stuck in loop” errors
- Displays metrics clearly with Streamlit cards
