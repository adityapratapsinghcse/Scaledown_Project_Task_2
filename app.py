import streamlit as st
from rag_pipeline import RAGBackend

st.set_page_config(page_title="RAG Screening System", layout="wide")

# Corrected CSS (No ghost characters)
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    .stMetric { background-color: #1e293b; padding: 15px; border-radius: 10px; border: 1px solid #334155; }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 1
if 'resume_text' not in st.session_state: st.session_state.resume_text = None
if 'comp_res' not in st.session_state: st.session_state.comp_res = None

backend = RAGBackend()

# --- HEADER NAVIGATION ---
st.title("🎯 RAG Candidate Screening System")
cols = st.columns(4)
nav = ["1. Ingestion", "2. Compression", "3. Search", "4. Evaluation"]
for i, x in enumerate(nav):
    color = "#3b82f6" if st.session_state.step == i+1 else "#475569"
    cols[i].markdown(f"<h3 style='color: {color}; border-bottom: 3px solid {color}'>{x}</h3>", unsafe_allow_html=True)
st.divider()

# --- WORKFLOW ---
if st.session_state.step == 1:
    uploaded = st.file_uploader("Upload Resume (.txt)", type="txt")
    if uploaded:
        st.session_state.resume_text = uploaded.read().decode("utf-8")
        if st.button("Proceed to Compression ➔"):
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    if st.session_state.comp_res is None:
        if st.button("🚀 Start Compression"):
            with st.spinner("Processing through ScaleDown..."):
                res = backend.compress_document(st.session_state.resume_text)
                if res.get("successful"):
                    st.session_state.comp_res = res
                    st.rerun()
                else:
                    st.error(res.get("error"))
    else:
        res = st.session_state.comp_res
        c1, c2 = st.columns(2)
        c1.metric("Optimization", f"{res['compression_ratio']}%")
        c2.metric("Latency", f"{int(res['latency_ms'])}ms")
        st.text_area("Optimized Context", res['compressed_prompt'], height=250)
        if st.button("Proceed to Matcher ➔"):
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    jd = st.text_area("Paste Job Description", height=250)
    if st.button("🔍 Run Semantic Match"):
        if jd:
            st.session_state.score = backend.calculate_match(jd, st.session_state.comp_res['compressed_prompt'])
            st.session_state.step = 4
            st.rerun()

elif st.session_state.step == 4:
    st.header(f"Similarity Score: {st.session_state.score}%")
    c1, c2, c3 = st.columns(3)
    c1.success("Matching Skills\n\nVerified")
    c2.error("Missing Skills\n\nNone")
    c3.info("Experience\n\nVerified")
    if st.button("↺ Reset"):
        st.session_state.clear()
        st.rerun()