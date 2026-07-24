# 📘 Cenário Prático: Integração entre Concessionária CSG e MeuPedágio
**Versão**: 1.0
**Objetivo**: Explicar como APIs conectam sistemas reais, usando o exemplo do pedágio — de forma simples e técnica.

---

## 🚛 Contexto
A **Concessionária CSG** administra trechos rodoviários e oferece benefícios, como **descontos para veículos frequentes ou de transporte**. O **MeuPedágio** é a plataforma que centraliza pagamentos, emite VPO e integra diretamente com as concessionárias — tudo isso só funciona graças às **APIs**.

---

### 🎯 Cenário passo a passo: Aplicando um desconto promocional da CSG
Imagine um caminhão que passa pela praça de pedágio e tem direito a uma promoção exclusiva da CSG. Veja como a API faz tudo acontecer:

| Passo | Ação do sistema | O que a API faz | Resultado |
|---|---|---|---|
| 1 | O veículo passa pela praça; o sistema da CSG lê a placa | A **API da CSG** consulta: *"Esse veículo tem direito ao desconto de 15% da promoção vigente?"* | Confirma que o benefício está ativo e registrado. |
| 2 | O sistema da CSG envia os dados para o MeuPedágio | A **API do MeuPedágio** recebe: placa, valor original, valor com desconto, tipo de benefício | Valida as informações e confere se tudo está de acordo com as regras da ANTT. |
| 3 | O motorista acessa o MeuPedágio para pagar | A API apresenta o valor já com o desconto aplicado automaticamente | O usuário vê: *"Valor original: R$ 20,00 — Com desconto CSG: R$ 17,00"* |
| 4 | Pagamento concluído via Pix | A API avisa imediatamente a CSG: *"Pagamento confirmado, desconto aplicado com sucesso"* | A concessionária registra a receita e contabiliza o benefício concedido. |

---

### 🧠 Por que isso só funciona com API?
- Sem a integração por API, a CSG teria que enviar arquivos manualmente, o MeuPedágio teria que conferir tudo à mão — demorado, sujeito a erros e sem garantia legal.
- Com a API:
  ✅ O desconto é aplicado **automaticamente**, sem o usuário precisar fazer nada
  ✅ Os dados são trocados em **segundos**, de forma segura e criptografada
  ✅ Tudo fica registrado para auditoria e cumprimento das regras da ANTT
  ✅ O sistema do MeuPedágio não precisa saber como funciona o sistema interno da CSG — só usa o que a API disponibiliza

---

### 📌 Resumo simples
> **A API é a ponte que conecta o benefício da CSG ao pagamento no MeuPedágio.**
> Ela garante que o desconto chegue ao motorista sem burocracia, que o pagamento seja repassado corretamente e que todas as regras sejam seguidas — sem que ninguém precise entender o funcionamento interno de cada sistema.

---

### ✅ O que isso significa para testes de API?
Quando testamos essa integração, verificamos:
- A API da CSG está informando o desconto corretamente?
- O MeuPedágio está aplicando o valor recebido?
- O retorno está chegando certo após o pagamento?
- Tudo está de acordo com o que foi acordado entre as partes?
