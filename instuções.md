📘 # Documento de Instruções: Postman - Conceitos Básicos e Estrutura
**Versão**: 1.0  
**Objetivo**: Orientar sobre a organização no Postman, conceitos fundamentais e boas práticas para estudo e portfólio.

---

## 1. Estrutura Principal do Postman

### 1.1 O que é uma Coleção?
> **Definição**: É o conjunto / pasta / projeto onde você agrupa todas as requisições, testes e configurações relacionadas a uma API ou objetivo específico.
> - Exemplo: `Lab Postman - JSONPlaceholder` → esta é a sua Coleção (seu projeto de estudo).
> - Todas as chamadas individuais ficam armazenadas dentro dela.

### 1.2 O que é uma Requisição?
> **Definição**: É cada ação individual executada na API (ex: buscar dados, cadastrar, alterar ou excluir).
> - Exemplo: `POST - 3 Criar novo post` → é uma requisição dentro da Coleção.
> - Cada requisição tem sua própria URL, método (GET, POST, PUT etc.), cabeçalhos, corpo e testes.

---

## 2. Configurações de uma Coleção
Ao selecionar uma Coleção, as abas abaixo definem regras que valem para **todas as requisições dentro dela**, a menos que sejam sobrescritas em uma requisição específica:

| Aba            | Finalidade                                                                 |
|----------------|----------------------------------------------------------------------------|
| **Overview**   | Dados gerais, descrição, versão e informações do projeto.                  |
| **Authorization** | Define o tipo de acesso/permissão necessário para usar a API.            |
| **Scripts**    | Comandos/testes que rodam automaticamente antes ou depois de todas as requisições. |
| **Variables**  | Valores reutilizáveis em todo o projeto (ex: endereço base da API).        |
| **Runs**       | Histórico de execuções em lote e resultados de testes automatizados.        |

---

## 3. Opções de Autorização (Aba Authorization)
Lista dos métodos de autenticação suportados pelo Postman:

| Tipo                     | O que significa                          | Quando usar                                                                 |
|--------------------------|------------------------------------------|-----------------------------------------------------------------------------|
| **No Auth**              | Sem autenticação                         | APIs públicas, que não exigem login ou chave de acesso (ex: JSONPlaceholder). |
| **Basic Auth**           | Acesso com usuário e senha simples        | Sistemas internos ou acesso restrito básico.                                |
| **Bearer Token / JWT Bearer** | Acesso por código de autenticação temporário | APIs modernas, serviços que emitem token após login.                |
| **OAuth 1.0 / 2.0**      | Padrão seguro de autorização             | Login com contas de terceiros (Google, Facebook, GitHub) ou corporativo.    |
| **API Key**              | Chave fixa de identificação              | Serviços que fornecem chave única para identificar o consumidor da API.     |
| *Demais opções*          | Métodos específicos                      | Integrações com AWS, bancos, servidores corporativos etc.                  |

---

## 4. Boas Práticas de Organização
- **Nomeie de forma clara**: Use o padrão `MÉTODO - Ação/Objetivo` (ex: `GET - Listar todos os posts`, `POST - Cadastrar novo post`).
- **Centralize configurações**: Defina autenticação e variáveis na Coleção, evite repetição em cada requisição.
- **Salve sempre**: Confirme o salvamento após criar ou alterar requisições.
- **Faça backup**: Exporte a Coleção periodicamente no formato `.json` para segurança.

---

## 5. Publicação no GitHub
1. Crie repositório com nome descritivo: `laboratorio-api-rest`
2. Estruture os arquivos:
   - Salve este conteúdo como `instrucoes.md`
   - Exporte a Coleção do Postman e adicione o arquivo `.json`
   - Atualize o `README.md` com apresentação do projeto
3. Confirme as alterações e envie ao repositório remoto.
