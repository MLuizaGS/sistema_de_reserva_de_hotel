
import json
from pathlib import Path

ARQUIVO_DADOS = Path(__file__).parent / "dados_hotel.json"


def salvar_dados(dados):
    """Salva um dicionário em arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def carregar_dados():
    """Carrega os dados do JSON ou retorna uma estrutura vazia."""
    if not ARQUIVO_DADOS.exists():
        return {
            "quartos": [],
            "hospedes": [],
            "reservas": []
        }

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
