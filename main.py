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

def simple_search(query, chunks, top_k=3):
    query_words = re.findall(r"\w+", query.lower())
    scored_results = []

    for chunk in chunks:
        text = chunk["text"].lower()
        score = sum(1 for word in query_words if word in text)

        if score > 0:
            scored_results.append({
                "text": chunk["text"],
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