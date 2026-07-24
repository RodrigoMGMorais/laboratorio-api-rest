# 📘 Cenário Prático: Integração Concessionária CSG ↔ MeuPedágio
**Versão**: 1.1
**Contexto**: A CSG opera **6 pórticos de cobrança Free-Flow** ao longo do trecho rodoviário. O sistema integra com a plataforma MeuPedágio por meio de APIs para aplicar benefícios e processar pagamentos automaticamente.

---

## 🎯 Cenário: Aplicando promoção de desconto da CSG em qualquer um dos 6 pórticos
Um veículo cadastrado na campanha "Frequência CSG" (10% de desconto) passa por um dos pórticos. Veja como a API conecta tudo:

| Passo | Ação nos pórticos | O que as APIs fazem | Resultado final |
|---|---|---|---|
| 1 | O veículo passa pelo **pórtico 3** (ou qualquer um dos 6); o sistema da CSG lê a placa | A **API Central da CSG** consulta: *"Placa ABC1234 tem direito ao desconto ativo? Em qual pórtico passou?"* | Confirma o benefício e identifica o pórtico e o valor da tarifa. |
| 2 | A CSG envia os dados para o MeuPedágio | A **API do MeuPedágio** recebe: placa, pórtico, valor original, valor com desconto, tipo de benefício | Valida as regras da ANTT e registra o débito já com o valor correto. |
| 3 | Motorista acessa o MeuPedágio | A API mostra automaticamente: *"Passagem no Pórtico 3 – Valor R$ 25,00 → Com desconto CSG: R$ 22,50"* | O usuário vê tudo certo, sem precisar informar nada extra. |
| 4 | Pagamento efetuado | A API avisa imediatamente a CSG: *"Pagamento confirmado, desconto aplicado no débito referente ao Pórtico 3"* | Os **6 pórticos permanecem atualizados**, o repasse é feito corretamente e a auditoria fica completa. |

---

### 🧠 Importante: Mesmo com 6 pórticos, o funcionamento não muda!
- A API da CSG **centraliza todas as informações** dos 6 pontos de cobrança;
- Não importa por qual pórtico o veículo passe: o desconto e os dados são enviados corretamente;
- Sem a API, cada um dos 6 pórticos teria que enviar dados separadamente, manualmente — risco enorme de erros, débitos duplicados ou benefícios não aplicados;
- Com a integração, tudo é padronizado, automático e em conformidade com a ANTT.

---

### 📌 Resumo prático
> **A API funciona como um "cérebro" que conecta os 6 pórticos da CSG ao MeuPedágio.**
> Ela garante que o benefício chegue ao motorista independente de onde ele passou, que os valores estejam certos e que todo o processo seja rápido e seguro.
