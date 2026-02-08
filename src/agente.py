from dados import carregar_perfil, carregar_transacoes, carregar_produtos
from logger import registrar_interacao


def responder_meta(perfil):
    meta = perfil["metas"][0]

    nome_meta = meta["meta"]
    valor_total = meta["valor_necessario"]
    atual = perfil["reserva_emergencia_atual"]

    faltando = valor_total - atual

    return (
        f"🎯 Meta principal: {nome_meta}\n"
        f"✅ Valor necessário: R$ {valor_total:,.2f}\n"
        f"📌 Valor atual: R$ {atual:,.2f}\n"
        f"➡️ Falta: R$ {faltando:,.2f}"
    )


def responder_gastos(transacoes):
    total_saida = 0

    for t in transacoes:
        if t["tipo"].lower() == "saida":
            total_saida += float(t["valor"])

    return (
        f"📊 Gastos registrados no mês: R$ {total_saida:,.2f}\n"
        f"Quer que eu identifique a categoria que mais consumiu seu orçamento?"
    )


def responder_produto(produtos, pergunta):
    for p in produtos:
        if p["nome"].lower() in pergunta.lower():
            return (
                f"📚 {p['nome']}\n"
                f"- Categoria: {p['categoria']}\n"
                f"- Risco: {p['risco']}\n"
                f"- Rentabilidade: {p['rentabilidade']}\n"
                f"- Explicação simples: {p['explicacao_simples']}"
            )

    return "Não encontrei esse produto na base. Quer tentar outro nome?"


def iniciar_guto():
    perfil = carregar_perfil()
    transacoes = carregar_transacoes()
    produtos = carregar_produtos()

    print("\n=== GUTO — Agente Financeiro Educativo ===\n")

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Guto: Até mais 😄")
            break

        # META
        if "meta" in pergunta.lower() or "falta" in pergunta.lower():
            resposta = responder_meta(perfil)

        # GASTOS
        elif "gastei" in pergunta.lower() or "gastos" in pergunta.lower():
            resposta = responder_gastos(transacoes)

        # PRODUTOS
        elif "tesouro" in pergunta.lower() or "cdb" in pergunta.lower():
            resposta = responder_produto(produtos, pergunta)

        else:
            resposta = "Posso te ajudar com metas, gastos ou produtos financeiros 😄"

        print("\nGuto:", resposta, "\n")

        registrar_interacao(perfil["nome"], pergunta, resposta)
