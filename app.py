from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
ARQUIVO_USUARIOS = "usuarios.json"

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return [
        {"id": 1, "nome": "Rodrigo", "cargo": "Analista de Sistemas"},
        {"id": 2, "nome": "Maria", "cargo": "Suporte Tecnico"}
    ]

def salvar_usuarios(lista):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)

usuarios = carregar_usuarios()

# Listar todos
@app.route("/api/usuarios", methods=["GET"])
def listar():
    return jsonify({"dados": usuarios})

# Adicionar novo (aceita ID informado ou cria automático)
@app.route("/api/usuarios", methods=["POST"])
def adicionar():
    dados = request.get_json()
    if not dados or "nome" not in dados or "cargo" not in dados:
        return jsonify({"erro": "Informe nome e cargo"}), 400

    # Se informar o ID, usa ele; senão cria automático
    if "id" in dados:
        # Verifica se o ID já existe
        if any(u["id"] == dados["id"] for u in usuarios):
            return jsonify({"erro": "Esse ID já está em uso"}), 409
        novo_id = dados["id"]
    else:
        novo_id = max((u["id"] for u in usuarios), default=0) + 1

    novo = {"id": novo_id, "nome": dados["nome"], "cargo": dados["cargo"]}
    usuarios.append(novo)
    salvar_usuarios(usuarios)
    return jsonify({"mensagem": "Usuário adicionado", "dados": novo}), 201

# Atualizar dados (agora também permite alterar o ID)
@app.route("/api/usuarios/<int:id>", methods=["PUT"])
def atualizar(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    dados = request.get_json() or {}

    # Se quiser mudar o ID
    if "id" in dados:
        novo_id = dados["id"]
        if novo_id != id and any(u["id"] == novo_id for u in usuarios):
            return jsonify({"erro": "Novo ID já está em uso"}), 409
        usuario["id"] = novo_id

    # Atualiza nome e cargo
    if "nome" in dados:
        usuario["nome"] = dados["nome"]
    if "cargo" in dados:
        usuario["cargo"] = dados["cargo"]

    salvar_usuarios(usuarios)
    return jsonify({"mensagem": "Usuário atualizado", "dados": usuario})

# Excluir
@app.route("/api/usuarios/<int:id>", methods=["DELETE"])
def excluir(id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != id]
    salvar_usuarios(usuarios)
    return jsonify({"mensagem": "Usuário removido"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)