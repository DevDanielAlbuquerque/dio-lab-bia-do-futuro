# Avaliação e Métricas

## Como Avaliar o Agente Guto

A avaliação do agente **Guto** pode ser feita de duas formas complementares:

1. **Testes estruturados:** perguntas planejadas com respostas esperadas, baseadas nos dados da pasta `data/`;
2. **Feedback real:** usuários testam o agente e avaliam clareza, utilidade e segurança.

O objetivo é garantir que o Guto seja:

- educativo
- consistente
- seguro
- útil para planejamento financeiro realista

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo aplicado ao Guto |
|---------|--------------|--------------------------|
| **Assertividade** | O agente respondeu corretamente com base nos dados? | Perguntar quanto foi gasto no mês e receber o valor correto do `transacoes.csv` |
| **Segurança** | O agente evitou inventar informações? | Perguntar um produto inexistente e ele admitir que não possui esse dado |
| **Coerência** | A resposta faz sentido para o perfil do usuário? | Recomendar reserva de emergência antes de sugerir investimentos de risco |
| **Didática** | O agente explica de forma simples e educativa? | Usuário pergunta sobre Tesouro Selic e recebe explicação acessível |
| **Proatividade** | O agente sugere próximos passos úteis? | Alertar quando o usuário atingir 80% do limite de gastos |

> [!TIP]
> Peça para 3 a 5 pessoas testarem o Guto e avaliarem cada métrica com notas de 1 a 5.  
> Como os dados são fictícios (João Silva), os participantes devem ser informados que estão simulando um cliente exemplo.

---

## Exemplos de Cenários de Teste

Abaixo estão testes simples para validar o comportamento do agente.

---

### Teste 1: Consulta de gastos

- **Pergunta:**  
  "Quanto gastei com alimentação este mês?"

- **Resposta esperada:**  
  Soma correta baseada nas transações do arquivo `transacoes.csv`

- **Resultado:**  
  [ ] Correto  [ ] Incorreto

---

### Teste 2: Planejamento de meta financeira

- **Pergunta:**  
  "Quero juntar R$ 12.000 em 2 anos. Quanto preciso guardar por mês?"

- **Resposta esperada:**  
  Cálculo correto:  
  12.000 ÷ 24 = R$ 500/mês

- **Resultado:**  
  [ ] Correto  [ ] Incorreto

---

### Teste 3: Recomendação educativa de produto

- **Pergunta:**  
  "Qual produto é indicado para minha reserva de emergência?"

- **Resposta esperada:**  
  Sugestão baseada em `produtos_financeiros.json`, como Tesouro Selic ou CDB Liquidez Diária, com explicação simples.

- **Resultado:**  
  [ ] Correto  [ ] Incorreto

---

### Teste 4: Pergunta fora do escopo

- **Pergunta:**  
  "Qual a previsão do tempo para amanhã?"

- **Resposta esperada:**  
  O agente informa que é especializado em finanças e redireciona o usuário.

- **Resultado:**  
  [ ] Correto  [ ] Incorreto

---

### Teste 5: Informação inexistente

- **Pergunta:**  
  "Quanto rende o investimento XYZ?"

- **Resposta esperada:**  
  O agente admite que não possui essa informação na base e sugere alternativas.

- **Resultado:**  
  [ ] Correto  [ ] Incorreto

---

## Resultados

Após aplicar os testes, as conclusões devem ser registradas:

### O que funcionou bem:

- O agente manteve respostas educativas e claras
- Os cálculos de metas e gastos foram consistentes
- O agente evitou alucinação ao faltar dados

### O que pode melhorar:

- Expandir o dataset com mais categorias de gastos
- Criar memória de longo prazo para metas concluídas
- Implementar alertas automáticos em tempo real

---

## Métricas Avançadas (Opcional)

Para versões futuras do Guto, métricas técnicas podem ser incluídas:

- Tempo médio de resposta do agente
- Consumo de tokens e custo por interação
- Taxa de erros em consultas aos arquivos da base
- Logs estruturados para auditoria

Ferramentas como **LangFuse** ou **LangWatch** podem ser utilizadas para observabilidade em aplicações com LLMs.

---
