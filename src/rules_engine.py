import json
from datetime import datetime, time
import os


REGRAS_PATH = os.path.join("config", "rules.json")
with open(REGRAS_PATH) as f:
    regras = json.load(f)


HORARIO_INICIO = datetime.strptime(regras["horario_permitido"]["inicio"], "%H:%M").time()
HORARIO_FIM = datetime.strptime(regras["horario_permitido"]["fim"], "%H:%M").time()
PORTAS_PROIBIDAS = regras["portas_proibidas"]
LIMITE_FALHAS = regras["limite_falhas_login"]

falhas_por_ip = {}

def fora_do_horario(horario_str: str) -> bool:
    hora = datetime.strptime(horario_str, "%Y-%m-%d %H:%M:%S").time()
    return hora < HORARIO_INICIO or hora > HORARIO_FIM

def porta_proibida(porta: int) -> bool:
    return porta in PORTAS_PROIBIDAS

def detectar_falhas(status: str, ip: str) -> bool:
    if status.lower() == "falha":
        falhas_por_ip[ip] = falhas_por_ip.get(ip, 0) + 1
    else:
        falhas_por_ip[ip] = 0
    return falhas_por_ip[ip] >= LIMITE_FALHAS
