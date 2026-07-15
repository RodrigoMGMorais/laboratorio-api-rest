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

2. **Instalar as dependências necessárias**
pip install -r requirements.txt

3. **Iniciar a API**
Quando iniciada, ela ficará disponível no endereço local:
http://localhost:5000/api/usuarios

🧪 Exemplos de teste com o comando curl
Além do Postman, você pode testar todas as operações diretamente pelo terminal:
🔹 Listar todos os usuários
curl http://localhost:5000/api/usuarios

🔹 Consultar um usuário por ID
curl http://localhost:5000/api/usuarios/3

🔹 Adicionar novo usuário (ID gerado automaticamente)
curl -X POST -H "Content-Type: application/json" -d '{"nome":"Heitor","cargo":"Programador JR"}' http://localhost:5000/api/usuarios

🔹 Adicionar novo usuário definindo o ID
curl -X POST -H "Content-Type: application/json" -d '{"id":5,"nome":"Ana Silva","cargo":"Desenvolvedora"}' http://localhost:5000/api/usuarios

🔹 Atualizar dados do usuário
curl -X PUT -H "Content-Type: application/json" -d '{"cargo":"Programador Pleno"}' http://localhost:5000/api/usuarios/3

🔹 Alterar o ID do usuário
curl -X PUT -H "Content-Type: application/json" -d '{"id":7}' http://localhost:5000/api/usuarios/3

🔹 Excluir usuário
curl -X DELETE http://localhost:5000/api/usuarios/7

⚠️ Observação sobre acesso externo
Durante o desenvolvimento, foi usado o ambiente GitHub Codespaces, que forneceu a URL temporária:
https://upgraded-space-goggles-p75v475gr5539799-5000.app.github.dev/api/usuarios

Essa URL só permanece ativa enquanto o ambiente de desenvolvimento estiver aberto. Para uso contínuo, basta executar a API localmente ou hospedá-la em qualquer serviço compatível com Python/Flask.

---

## 📤 Enviar a atualização para o GitHub
No terminal do Codespaces, execute esses comandos para salvar e publicar essa alteração:
```bash
git add GUIA-USO-API.md
git commit -m "Adiciona instruções para execução local e comandos curl"
git push

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

---
## 💡Dicas Importantes
 1. O "Cerne": O que uma API realmente é?
Esqueça a definição de dicionário. Uma API (Application Programming Interface) é um contrato de comunicação.

O segredo da elite: Nunca confie que o contrato será cumprido. O contrato pode mudar, a rede pode falhar e o servidor pode estar sobrecarregado. APIs de elite são construídas com o princípio de "Defense in Depth".

2. O Vocabulário de Elite (O que falar na entrevista)
Se você quer ser contratado como sênior, não diga apenas "eu consumo APIs". Use estes termos:

Idempotência: A capacidade de fazer a mesma requisição múltiplas vezes sem alterar o resultado. Exemplo: Se eu envio um comando de "cobrar pedágio" duas vezes por erro de rede, o sistema deve entender que é a mesma transação (o correlation_id do nosso exemplo anterior é o que garante isso).

Rate Limiting / Throttling: A capacidade de proteger seu sistema limitando o número de requisições que um cliente pode fazer. Se você não domina isso, seu sistema cai por excesso de carga.

Códigos de Status HTTP (O "ABC" da comunicação):

2xx (Sucesso): Tudo certo.

4xx (Erro do Cliente): O problema é quem enviou (ex: 400 Bad Request, 401 Unauthorized, 404 Not Found).

5xx (Erro do Servidor): O problema é seu. Se um sistema de CS retorna 500 para o cliente, você tem um problema crítico de estabilidade.

Autenticação vs. Autorização: Autenticação é "quem você é?" (Bearer Token, JWT). Autorização é "o que você pode fazer?" (Scopes, RBAC).

3. "Macetes" que os Amadores não sabem
Circuit Breaker (O Padrão de Elite): Se uma API que seu sistema consome está fora do ar, você não pode ficar tentando reconectar infinitamente, pois isso vai consumir todos os seus recursos. O Circuit Breaker "abre o circuito", para as tentativas por um tempo e falha rápido, protegendo seu sistema.

Versioning (Versionamento): Nunca mude uma API em produção. Se precisar mudar, crie a /v2/. Se você não versiona, você quebra a integração de todo mundo que consome seu serviço.

Payload Minimalista: O que você envia e recebe deve ser o mínimo necessário. Dados desnecessários incham a rede e aumentam a latência.

Sempre use o cabeçalho Content-Type: application/json para requisições com corpo (POST e PUT).
O ID é único: não pode ter dois usuários com o mesmo número.
Os dados ficam salvos no arquivo usuarios.json — não somem ao reiniciar a API.
Para testar, use ferramentas como Postman, ReqBin ou o terminal com curl.

🚀 Projeto desenvolvido para estudo e prática de APIs REST com Python e Flask.
