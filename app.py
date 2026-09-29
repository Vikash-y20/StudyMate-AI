import streamlit as st
from src.study_engine import summarize_text, extract_keywords, generate_questions

st.set_page_config(page_title="StudyMate AI", page_icon="📚", layout="wide")
st.title("📚 StudyMate AI")
st.caption("Starter prototype • Local-first AI learning assistant")

st.info("This starter uses a lightweight local text engine. Qualcomm AI Hub models can be integrated next.")

uploaded = st.file_uploader("Upload study material", type=["txt", "md"])
default_text = """Artificial intelligence is the field of computer science concerned with building systems
that can perform tasks that normally require human intelligence. Machine learning is a major
part of AI in which systems learn patterns from data. Deep learning uses multi-layer neural
networks and is widely used for speech recognition, computer vision and natural language tasks.
On-device AI performs inference directly on a device, which can reduce latency and limit the
need to send sensitive data to cloud servers."""

text = uploaded.read().decode("utf-8", errors="ignore") if uploaded else st.text_area(
    "Or paste your lecture/study material", value=default_text, height=220
)

if st.button("Analyze Study Material", type="primary"):
    if not text.strip():
        st.warning("Please upload or enter study material.")
    else:
        st.session_state.summary = summarize_text(text)
        st.session_state.keywords = extract_keywords(text)
        st.session_state.questions = generate_questions(text)

if "summary" in st.session_state:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📝 Summary")
        st.write(st.session_state.summary)
    with c2:
        st.subheader("🔑 Key Topics")
        for k in st.session_state.keywords:
            st.write("• " + k)

    st.subheader("🧠 Revision Questions")
    for i, q in enumerate(st.session_state.questions, 1):
        st.write(f"**{i}.** {q}")

    notes = (
        "StudyMate AI Notes\n\nSUMMARY\n" + st.session_state.summary +
        "\n\nKEY TOPICS\n" +
        "\n".join("- " + k for k in st.session_state.keywords) +
        "\n\nREVISION QUESTIONS\n" +
        "\n".join(f"{i}. {q}" for i, q in enumerate(st.session_state.questions, 1))
    )
    st.download_button("Download Study Notes", notes, "studymate_notes.txt", "text/plain")
