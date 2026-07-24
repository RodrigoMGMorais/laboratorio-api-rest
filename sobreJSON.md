# 📘 Aula Completa: Formato JSON
**Versão**: 1.0
**Objetivo**: Ensinar o que é JSON, como funciona, regras de sintaxe, tipos de dados e como aplicar no dia a dia com APIs e testes.

---

## 1. O que é JSON?
**JSON** significa **JavaScript Object Notation** (Notação de Objetos JavaScript).
- É um formato de **dados texto**, leve e fácil de ler tanto para pessoas quanto para máquinas.
- É o padrão mundial para troca de informações entre sistemas, especialmente em APIs.
- Apesar do nome, **não é exclusivo do JavaScript**: funciona com todas as linguagens e ferramentas (Postman, Python, Java, VS Code etc.).

---

## 2. Regras Fundamentais de Sintaxe
Essas regras **nunca podem ser quebradas** — se errar alguma, o JSON fica inválido:

✅ **Regra 1**: Usa **chaves `{ }`** para representar um **OBJETO** (um conjunto de informações de uma coisa só).<br>
✅ **Regra 2**: Usa **colchetes `[ ]`** para representar um **ARRAY/LISTA** (vários itens agrupados).<br>
✅ **Regra 3**: Os dados são sempre no formato **`"chave": valor`** — a chave sempre entre **aspas duplas**.<br>
✅ **Regra 4**: Separe os pares com **vírgula**, nunca coloque vírgula no último item.<br>
✅ **Regra 5**: Valores de texto/string ficam entre **aspas duplas**; números, booleanos e valores nulos **não usam aspas**.<br>
✅ **Regra 6**: Use **ponto `.`** para decimais, nunca vírgula.<br>

❌ **Erros mais comuns**:
- Usar aspas simples `' '` em vez de duplas `" "`
- Esquecer de fechar chaves, colchetes ou aspas
- Colocar vírgula sobrando no último item
- Usar vírgula em números decimais

---

## 3. Tipos de Dados Suportados
| Tipo | Exemplo | Descrição |
|---|---|---|
| **Texto / String** | `"nome": "Rodrigo"` | Qualquer sequência de caracteres, entre aspas duplas. |
| **Número** | `"peso": 1.20` | Valores numéricos, inteiros ou decimais — sem aspas. |
| **Booleano** | `"ativo": true` / `"ativo": false` | Valor lógico — **sem aspas e minúsculo**. |
| **Nulo** | `"descricao": null` | Valor vazio ou não definido — sem aspas. |
| **Objeto** | `"endereco": { "rua": "Av. Brasil" }` | Conjunto de dados dentro de outro dado. |
| **Array / Lista** | `"telefones": ["11999998888", "67988887777"]` | Lista de valores agrupados. |

---

## 4. Estruturas Práticas

### 4.1 Objeto Único (`{ }`)
Usado quando temos **UM CONJUNTO DE DADOS SÓ**:
```json
{
  "produto": "Câmera",
  "categoria": "Eletrônicos",
  "peso_kg": 1.20,
  "disponivel": true
}
```

## 4.2 Lista / Vários Itens ([ ] contendo { })
Usado quando temos VÁRIOS REGISTROS (como uma tabela):
```json
[
  {
    "produto": "Câmera",
    "categoria": "Eletrônicos",
    "peso_kg": 1.20,
    "disponivel": true
  },
  {
    "produto": "Tripé",
    "categoria": "Acessórios",
    "peso_kg": 2.00,
    "disponivel": false
  }
]
```
---
## 5. Como Validar e Formatar JSON
Sempre confira se o seu JSON está correto:
Na web: Use ferramentas como o JSONLint — basta colar e ele aponta exatamente onde está o erro.
No VS Code: Salve o arquivo com extensão .json — o editor já marca erros em vermelho.
No Postman: Na aba Body da resposta, selecione a visualização JSON — ele já formata automaticamente.

## 6. Por que JSON é essencial para Testes de APIs?
Todas as APIs modernas usam JSON como padrão de envio e recebimento de dados.
Para testar bem, você precisa saber:
✅ Montar um JSON válido para enviar na requisição
✅ Ler e entender a estrutura da resposta que vem da API
✅ Extrair valores do JSON para usar em testes ou outras requisições
✅ Validar se o que veio está exatamente no formato esperado

---
## 7. Resumo Rápido para Não Errar

Se for...	Usa...	Exemplo
1 coisa só	{ }	1 produto, 1 usuário
Várias coisas	[ { }, { } ]	Lista de produtos, tabela completa
Texto	"valor"	"Fulano"
Número / Verdadeiro / Falso	valor	1.5, true, false

**Dica final:** O JSON é simples — basta seguir as regras e praticar. Quanto mais você usar no Postman e no VS Code, mais natural fica!

