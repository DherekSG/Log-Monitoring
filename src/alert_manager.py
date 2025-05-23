import os
from datetime import datetime

ALERTS_DIR = 'alerts'

def salvar_alerta(tipo: str, linha: dict):
    """Salva alerta em arquivo de texto organizado por tipo"""
    if not os.path.exists(ALERTS_DIR):
        os.makedirs(ALERTS_DIR)

    data_str = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(ALERTS_DIR, f"{tipo}_{data_str}.log")

    with open(filename, 'a') as f:
        f.write(f"{datetime.now().isoformat()} - {linha}\n")
