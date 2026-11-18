from flask import Flask, jsonify

app = Flask(__name__)

# Dados de exemplo: três livros armazenados em uma lista Python.
livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    {"id": 3, "titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977}
]

@app.route("/livros", methods=["GET"])
def listar_livros():
    """Retorna a lista de livros em formato JSON."""
    return jsonify({"livros": livros}), 200

if __name__ == "__main__":
    app.run(debug=True)
