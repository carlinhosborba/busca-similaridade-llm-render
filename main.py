from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    results = []

    if request.method == "POST":
        query = request.form.get("query", "").strip()
        if query:
            results = [
                {
                    "text": "Resultado de teste 1",
                    "url": "#",
                    "score": 0.95
                },
                {
                    "text": "Resultado de teste 2",
                    "url": "#",
                    "score": 0.89
                }
            ]

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