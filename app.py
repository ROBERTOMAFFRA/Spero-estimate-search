import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Carregar planilha
df = pd.read_excel("data/Modelo app estimate.xlsx", sheet_name="Sheet1")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    if not query:
        return jsonify([])
    results = df[df["DESCRIPTION"].str.lower().str.contains(query, na=False)]
    return jsonify(results.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
