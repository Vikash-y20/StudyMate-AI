import re
from collections import Counter

STOPWORDS = {
    "the","and","for","that","this","with","from","are","was","were","have",
    "has","into","their","they","which","about","there","using","used","than",
    "then","also","can","will","its","been","being","not","but","you","your",
    "how","what","when","where","why","who","a","an","of","to","in","on",
    "is","as","by","or","be","it","at","we","our"
}

def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]

def summarize_text(text, max_sentences=4):
    sents = sentences(text)
    if len(sents) <= max_sentences:
        return " ".join(sents)
    words = re.findall(r"[A-Za-z]{3,}", text.lower())
    freq = Counter(w for w in words if w not in STOPWORDS)
    scored = []
    for i, sent in enumerate(sents):
        sw = re.findall(r"[A-Za-z]{3,}", sent.lower())
        scored.append((sum(freq.get(w, 0) for w in sw), i, sent))
    chosen = sorted(scored, reverse=True)[:max_sentences]
    return " ".join(x[2] for x in sorted(chosen, key=lambda x: x[1]))

def extract_keywords(text, limit=8):
    words = re.findall(r"[A-Za-z][A-Za-z-]{2,}", text.lower())
    freq = Counter(w for w in words if w not in STOPWORDS)
    return [w for w, _ in freq.most_common(limit)]

def generate_questions(text, limit=5):
    keys = extract_keywords(text, limit)
    templates = [
        "What is {k} and why is it important?",
        "Explain the role of {k} in the topic.",
        "How does {k} work?",
        "Give one practical application of {k}.",
        "What are the main points to remember about {k}?"
    ]
    return [templates[i % len(templates)].format(k=k) for i, k in enumerate(keys)]
