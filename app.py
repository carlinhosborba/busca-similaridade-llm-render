from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    results = []

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            results = [
                "Resultado de exemplo 1",
                "Resultado de exemplo 2",
                "Resultado de exemplo 3",
            ]

    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)