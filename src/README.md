# Código da Aplicação — Agente Guto

Esta pasta contém o código principal do agente financeiro **Guto**.

O objetivo do Guto é ajudar o usuário com:

- Planejamento de metas financeiras
- Controle de gastos mensais
- Educação financeira simples e prática
- Alertas baseados nos dados da pasta `data/`

---

## Estrutura Sugerida

```
src/
├── app.py # ponto de entrada do agente (executável)
├── agente.py # lógica principal de respostas do Guto
├── dados.py # leitura dos arquivos JSON/CSV da pasta data/
├── logger.py # registro de interações no histórico
└── README.md # instruções de execução

```

## Exemplo de requirements.txt

```
Pandas
```

## Como Rodar

### 1. Acesse a pasta `src`

```bash
cd src

python app.py