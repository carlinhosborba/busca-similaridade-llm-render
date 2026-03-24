from flask import Flask, render_template, request

from app.scraper import scrape_all
from app.chunker import process_documents
from app.embeddings import generate_embeddings
from app.search import search_similar

app = Flask(__name__)

chunks_data = None
chunk_embeddings = None

def ensure_data_loaded():
    global chunks_data, chunk_embeddings

    if chunks_data is None or chunk_embeddings is None:
        documents = scrape_all()
        chunks_data = process_documents(documents)
        chunk_texts = [item["text"] for item in chunks_data]
        chunk_embeddings = generate_embeddings(chunk_texts)

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    results = []

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            ensure_data_loaded()
            query_embedding = generate_embeddings([query])[0]
            similar_chunks = search_similar(
                query_embedding,
                chunk_embeddings,
                chunks_data,
                top_k=3
            )

            results = [
                {
                    "text": item["text"],
                    "url": item["url"],
                    "score": float(score)
                }
                for item, score in similar_chunks
            ]

    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)