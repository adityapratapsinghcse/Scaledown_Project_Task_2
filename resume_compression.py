import os
import requests

SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")
SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"

def compress_text(text):
    if not SCALEDOWN_API_KEY:
        raise Exception("SCALEDOWN_API_KEY not found in environment.")

    headers = {
        "x-api-key": SCALEDOWN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "context": "Compress this resume for a RAG pipeline, keeping technical skills.",
        "prompt": text,
        "scaledown": {"rate": "auto"}
    }

    try:
        response = requests.post(SCALEDOWN_URL, headers=headers, json=payload, timeout=30)
        data = response.json()
        
        # Documentation check: Ensure we handle the response structure accurately
        if not data.get("successful", False):
            raise Exception(f"ScaleDown Error: {data.get('error', 'Unknown error')}")

        # The doc shows 'compressed_prompt' at the top level
        compressed_text = data.get("compressed_prompt")
        
        if compressed_text is None:
            # Fallback check if it's nested in results
            compressed_text = data.get("results", {}).get("compressed_prompt")
            
        return compressed_text
    except Exception as e:
        raise Exception(f"ScaleDown request failed: {e}")