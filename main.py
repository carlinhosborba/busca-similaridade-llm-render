from flask import Flask, render_template, request
import os
import re

from app.scraper import scrape_all
from app.chunker import process_documents

app = Flask(__name__)

chunks_data = None

def ensure_data_loaded():
    global chunks_data

    if chunks_data is None:
        documents = scrape_all()
        chunks_data = process_documents(documents)

def build_preview(text, query, max_chars=420):
    clean_text = " ".join(text.split())
    query_words = re.findall(r"\w+", query.lower())

    start_index = 0
    lower_text = clean_text.lower()

    for word in query_words:
        found = lower_text.find(word)
        if found != -1:
            start_index = max(0, found - 80)
            break

    preview = clean_text[start_index:start_index + max_chars]

    if start_index > 0:
        preview = "..." + preview

    if start_index + max_chars < len(clean_text):
        preview = preview + "..."

    return preview

def simple_search(query, chunks, top_k=3):
    query_words = re.findall(r"\w+", query.lower())
    scored_results = []
    seen_texts = set()

    for chunk in chunks:
        original_text = chunk["text"]
        text = original_text.lower()

        score = sum(1 for word in query_words if word in text)

        if score > 0:
            preview = build_preview(original_text, query)

            if preview not in seen_texts:
                seen_texts.add(preview)
                scored_results.append({
                    "text": preview,
                    "url": chunk["url"],
                    "score": score
                })

    scored_results.sort(key=lambda item: item["score"], reverse=True)
    return scored_results[:top_k]

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    results = []

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            ensure_data_loaded()
            results = simple_search(query, chunks_data, top_k=3)

    return render_template("index.html", query=query, results=results)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )