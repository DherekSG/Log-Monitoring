import json
from datetime import datetime
from pathlib import Path

REGRAS_PATH = "config/rules.json"
ALERTS_DIR = "alerts"

Path(ALERTS_DIR).mkdir(exist_ok=True)

with open(REGRAS_PATH) as f:
    regras = json.load(f)

horario_permitido = regras.get("horario_permitido", {"inicio": "08:00", "fim": "18:00"})
portas_proibidas = regras.get("portas_proibidas", [])
limite_falhas = regras.get("falhas_login", {}).get("limite", 3)

falhas_alertas = []

def salvar_alerta(alerta, tipo_alerta):
    alerta["tipo_alerta"] = tipo_alerta
    alerta["detectado_em"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    arquivo = Path(ALERTS_DIR) / f"{tipo_alerta}_alertas.jsonl"
    with open(arquivo, "a") as f:
        f.write(json.dumps(alerta) + "\n")

def fora_do_horario(registro):
    timestamp = registro.get("timestamp")
    if not timestamp:
        return False
    
    horario_str = timestamp.split()[1]  # pegar hora:minuto:segundo
    hora = datetime.strptime(horario_str, "%H:%M:%S").time()
    inicio = datetime.strptime(horario_permitido["inicio"], "%H:%M").time()
    fim = datetime.strptime(horario_permitido["fim"], "%H:%M").time()
    
    if hora < inicio or hora > fim:
        alerta = {
            "registro": registro,
            "detalhes": f"Registro fora do horário permitido: {hora}"
        }
        salvar_alerta(alerta, "fora_do_horario")
        return True
    return False

def porta_proibida(registro):
    port = str(registro.get("port", ""))
    if port in portas_proibidas:
        alerta = {
            "registro": registro,
            "detalhes": f"Porta {port} está na lista de portas proibidas"
        }
        salvar_alerta(alerta, "porta_proibida")
        return True
    return False

def detectar_falhas(registro, tentativas_falha, limite=3):
    # Garante que limite é inteiro
    if isinstance(limite, list):
        limite = int(limite[0])
    else:
        limite = int(limite)

    ip = registro.get('ip_address')
    status = registro.get('status', '').lower()
    
    if not ip:
        return False

    if status == 'failed': 
        tentativas_falha[ip] = tentativas_falha.get(ip, 0) + 1
        
        if tentativas_falha[ip] >= limite:
            alert = {
                "tipo_alerta": "falha_login_repetida",
                "ip_address": ip,
                "quantidade_alertas": tentativas_falha[ip],
                "ultima_ocorrencia": registro.get('timestamp')
            }
            falhas_alertas.append(alert)
            salvar_alerta(alert, "falha_login")
            tentativas_falha[ip] = 0

    return False
