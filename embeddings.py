# embeddings.py
from sentence_transformers import SentenceTransformer

# We use 'all-MiniLM-L6-v2'. It's one of the most popular free models 
# because it's tiny, fast, and very accurate for English text.
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text):
    if not text:
        return None
    try:
        # This converts your resume text into a list of 384 numbers.
        embedding = model.encode(text)
        return embedding.tolist()
    except Exception as e:
        raise Exception(f"Local Embedding Error: {e}")