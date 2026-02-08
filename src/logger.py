import csv
from datetime import datetime
from pathlib import Path

HISTORICO = Path("../data/historico_atendimento.csv")


def registrar_interacao(usuario, pergunta, resposta):
    with open(HISTORICO, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "chat",
            "interacao",
            pergunta,
            "sim"
        ])
