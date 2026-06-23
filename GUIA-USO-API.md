# 📖 Guia de Uso e Documentação da API
> Projeto: Laboratório API REST de Gerenciamento de Usuários

---

## 🎯 Objetivo
Este guia explica de forma simples o funcionamento da API, os métodos HTTP utilizados, o que cada um faz e exemplos práticos de requisições.

---

## 📌 Conceitos Básicos
API = Interface de Programação de Aplicações. Ela permite que diferentes sistemas troquem dados entre si. Neste projeto, usamos o padrão **REST**, que é o mais comum e organizado.

### 🔹 Principais Métodos HTTP
Cada método serve para uma ação específica:

| Método | Nome da Ação | O que faz | Precisa de ID na URL? | Precisa de corpo JSON? |
|--------|--------------|-----------|------------------------|-------------------------|
| **GET**    | Consultar / Listar | Busca dados cadastrados | ❌ Não (para lista completa)<br>✅ Sim (para um único usuário) | ❌ Não |
| **POST**   | Criar / Adicionar | Cadastra um novo registro | ❌ Nunca | ✅ Sim |
| **PUT**    | Atualizar / Alterar | Modifica dados de um registro existente | ✅ Sempre | ✅ Sim |
| **DELETE** | Excluir / Remover | Apaga um registro | ✅ Sempre | ❌ Não |

---

## 🚀 Endereço Base da API:
https://upgraded-space-goggles-p75v475gr5539799-5000.app.github.dev/api

## Ou, para uso local:
http://localhost:5000/api

---

## 🖥️ Como executar a API localmente
Você pode rodar o projeto no seu computador sem depender de ambientes externos. Basta seguir esses passos:

### ✅ Pré-requisitos
- Ter o **Python 3.8 ou superior** instalado
- Ter o **Git** instalado para clonar o repositório

### 📋 Passo a passo
1. **Baixar o código do projeto**
   Abra o terminal e execute:
   ```bash
   git clone https://github.com/RodrigoMGMorais/laboratorio-api-rest.git
   cd laboratorio-api-rest

---

## 📋 Detalhamento de Cada Operação

### 1️⃣ GET → Listar todos os usuários
**Rota:** `/usuarios`
**Descrição:** Retorna a lista completa de todos os usuários cadastrados.

✅ Exemplo:
```http
GET https://upgraded-space-goggles-p75v475gr5539799-5000.app.github.dev/api/usuarios

📤RESPOSTA:
{
  "dados": [
    {"id": 1, "nome": "Rodrigo", "cargo": "Analista de Sistemas"},
    {"id": 2, "nome": "Maria", "cargo": "Suporte Técnico"}
  ]
}

---
2️⃣ GET → Consultar um usuário específico
Rota: /usuarios/<id>
Descrição: Busca apenas os dados do usuário com o ID informado.

✅ Exemplo:
GET https://upgraded-space-goggles-p75v475gr5539799-5000.app.github.dev/api/usuarios/3
📤RESPOSTA:
{"id": 3, "nome": "Heitor", "cargo": "Programador JR"}
---
3️⃣ POST → Adicionar novo usuário
Rota: /usuarios
Descrição: Cria um novo usuário. O ID pode ser gerado automaticamente ou informado manualmente.

✅ Exemplo sem informar ID (geração automática):
POST /api/usuarios
Content-Type: application/json
{
  "nome": "Ana Silva",
  "cargo": "Desenvolvedora"
}
✅ Exemplo com ID definido por você:
{
  "id": 10,
  "nome": "Ana Silva",
  "cargo": "Desenvolvedora"
}
📤RESPOSTA:
{
  "mensagem": "Usuário adicionado",
  "dados": {"id": 10, "nome": "Ana Silva", "cargo": "Desenvolvedora"}
}
---
4️⃣ PUT → Atualizar dados ou alterar ID
Rota: /usuarios/<id>
Descrição: Altera nome, cargo ou até o ID de um usuário que já existe.
✅ Exemplo: alterar apenas o cargo
PUT /api/usuarios/10
Content-Type: application/json
{
  "cargo": "Desenvolvedora Pleno"
}
✅ Exemplo: alterar o ID do usuário
PUT /api/usuarios/10
Content-Type: application/json
{
  "id": 5
}
✅ Exemplo: alterar tudo de uma vez
{
  "id": 7,
  "nome": "Ana Carolina Silva",
  "cargo": "Desenvolvedora Sênior"
}
📤RESPOSTA:
{
  "mensagem": "Usuário atualizado",
  "dados": {"id": 7, "nome": "Ana Carolina Silva", "cargo": "Desenvolvedora Sênior"}
}
---
5️⃣ DELETE → Excluir usuário
Rota: /usuarios/<id>
Descrição: Remove definitivamente o usuário com o ID informado.
✅ Exemplo:
DELETE /api/usuarios/7
📤RESPOSTA:
{"mensagem": "Usuário removido"}

⚠️ Códigos de Resposta Comuns:
Código	Significado
200 OK	Tudo funcionou corretamente
201 Created	Novo usuário cadastrado com sucesso
400 Bad Request	Dados enviados estão incorretos ou incompletos
404 Not Found	Usuário com esse ID não existe
405 Method Not Allowed	Método usado não é permitido para essa rota
409 Conflict	Tentou usar um ID que já está cadastrado

💡 Dicas Importantes
Sempre use o cabeçalho Content-Type: application/json para requisições com corpo (POST e PUT).
O ID é único: não pode ter dois usuários com o mesmo número.
Os dados ficam salvos no arquivo usuarios.json — não somem ao reiniciar a API.
Para testar, use ferramentas como Postman, ReqBin ou o terminal com curl.

🚀 Projeto desenvolvido para estudo e prática de APIs REST com Python e Flask.
