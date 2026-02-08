# Base de Conhecimento

## Dados Utilizados

O agente Guto utiliza arquivos simples em JSON e CSV como base de conhecimento e memória operacional. Esses dados permitem personalizar metas, acompanhar gastos e oferecer explicações educativas sobre produtos financeiros.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Registrar interações anteriores e acompanhar evolução do usuário ao longo do tempo |
| `perfil_investidor.json` | JSON | Armazenar perfil financeiro do usuário (renda, objetivos, limites e metas) para personalizar respostas |
| `produtos_financeiros.json` | JSON | Base educativa com produtos financeiros e explicações simples para apoiar aprendizado e decisões conscientes |
| `transacoes.csv` | CSV | Controle de gastos do usuário, permitindo análise de padrão mensal e alertas de limite |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Sim. Os dados mockados foram adaptados para refletir melhor o propósito do agente Guto, que é focado em planejamento financeiro e controle de gastos.

As principais adaptações foram:

Inclusão de um campo de linguagem mais acessível (explicacao_simples) em produtos_financeiros.json, reforçando o caráter educativo do agente.

Ajuste do perfil do usuário para suportar planejamento prático, incluindo limite de gastos mensal e metas de longo prazo.

Padronização dos dados para que o agente consiga responder sem inventar informações, sempre baseado no que está armazenado.

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON e CSV são carregados no início da sessão do agente e utilizados como contexto para tomada de decisão.

Exemplo de carregamento:

perfil_investidor.json fornece informações fixas do usuário.

transacoes.csv é lido para calcular gastos acumulados no mês.

produtos_financeiros.json é consultado quando o usuário pede explicações sobre investimentos.

historico_atendimento.csv funciona como memória de interações anteriores.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados não são colocados integralmente no system prompt para evitar excesso de contexto.

A estratégia adotada é:

O agente consulta dinamicamente apenas as partes relevantes conforme a intenção do usuário.

O prompt é montado com informações resumidas, como:

meta atual

limite de gastos

últimas transações

produto financeiro solicitado

Dessa forma, o Guto mantém respostas objetivas, personalizadas e com menor risco de alucinação.

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Perfil do Usuário:
- Nome: João Silva
- Renda mensal: R$ 5.000
- Limite de gastos mensal: R$ 3.000
- Objetivo principal: Construir reserva de emergência

Metas atuais:
- Completar reserva de emergência até 2026-06 (faltam R$ 5.000)
- Entrada do apartamento até 2027-12 (meta: R$ 50.000)

Últimas transações registradas:
- 01/02: Supermercado - R$ 450
- 03/02: Transporte - R$ 55
- 05/02: Lazer - R$ 120

Base educativa disponível:
- Tesouro Selic: investimento seguro para reserva de emergência
- CDB liquidez diária: renda fixa com rendimento diário
