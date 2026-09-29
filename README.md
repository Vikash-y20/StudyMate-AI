# StudyMate AI

On-device AI learning assistant starter project for Snapdragon-powered HP PCs.

## Features
- Upload or paste study material
- Local summary
- Keyword extraction
- Revision-question generation
- Downloadable study notes

This is a starter prototype. Qualcomm AI Hub / Snapdragon-optimized models should be integrated and benchmarked on the target device before claiming hardware-specific performance.

## Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Planned competition upgrade
Add a suitable Qualcomm AI Hub speech-to-text model and a compact local language model, then benchmark latency and memory on the actual Snapdragon-powered HP PC.
