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

✅ **Regra 1**: Usa **chaves `{ }`** para representar um **OBJETO** (um conjunto de informações de uma coisa só).
✅ **Regra 2**: Usa **colchetes `[ ]`** para representar um **ARRAY/LISTA** (vários itens agrupados).
✅ **Regra 3**: Os dados são sempre no formato **`"chave": valor`** — a chave sempre entre **aspas duplas**.
✅ **Regra 4**: Separe os pares com **vírgula**, nunca coloque vírgula no último item.
✅ **Regra 5**: Valores de texto/string ficam entre **aspas duplas**; números, booleanos e valores nulos **não usam aspas**.
✅ **Regra 6**: Use **ponto `.`** para decimais, nunca vírgula.

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
