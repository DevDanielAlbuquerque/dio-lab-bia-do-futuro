import json
import csv
from pathlib import Path

# Caminho da pasta data/
DATA_DIR = Path("../data")


def carregar_perfil():
    """Carrega o perfil do investidor (JSON)."""
    with open(DATA_DIR / "perfil_investidor.json", encoding="utf-8") as f:
        return json.load(f)


def carregar_transacoes():
    """Carrega as transações financeiras (CSV)."""
    with open(DATA_DIR / "transacoes.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def carregar_produtos():
    """Carrega a lista de produtos financeiros disponíveis (JSON)."""
    with open(DATA_DIR / "produtos_financeiros.json", encoding="utf-8") as f:
        return json.load(f)
