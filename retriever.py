import numpy as np

def compute_similarity(embedding1, embedding2):
    """Simple cosine similarity for ranking resumes."""
    e1 = np.array(embedding1)
    e2 = np.array(embedding2)
    return np.dot(e1, e2) / (np.linalg.norm(e1) * np.linalg.norm(e2))