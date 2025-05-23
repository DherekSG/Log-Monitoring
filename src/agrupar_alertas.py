import os
import json
import csv
from collections import defaultdict
from datetime import datetime

ALERTS_DIR = "alerts"
RESUMO_CSV = "resumo_alertas.csv"

def agrupar_alertas():
    resumo = defaultdict(lambda: defaultdict(lambda: {"qtd": 0, "ultima_ocorrencia": None}))

    for nome_arquivo in os.listdir(ALERTS_DIR):
        if not nome_arquivo.endswith(".jsonl"):
            continue

        tipo_alerta = nome_arquivo.split("_alertas")[0]
        caminho = os.path.join(ALERTS_DIR, nome_arquivo)

        with open(caminho, "r") as f:
            for linha in f:
                alerta = json.loads(linha)
                ip = alerta.get("ip_address") or alerta["registro"].get("ip_address")
                timestamp = alerta.get("timestamp") or alerta["registro"].get("timestamp")

                resumo[tipo_alerta][ip]["qtd"] += 1
                atual = resumo[tipo_alerta][ip]["ultima_ocorrencia"]
                nova = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

                if not atual or nova > atual:
                    resumo[tipo_alerta][ip]["ultima_ocorrencia"] = nova

    # Exportar para CSV
    with open(RESUMO_CSV, "w", newline='') as csvfile:
        campos = ["tipo_alerta", "ip_address", "quantidade_alertas", "ultima_ocorrencia"]
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        escritor.writeheader()

        for tipo, ips in resumo.items():
            for ip, dados in ips.items():
                escritor.writerow({
                    "tipo_alerta": tipo,
                    "ip_address": ip,
                    "quantidade_alertas": dados["qtd"],
                    "ultima_ocorrencia": dados["ultima_ocorrencia"].strftime("%Y-%m-%d %H:%M:%S")
                })


    print(f"Resumo gerado em: {RESUMO_CSV}")
    print("IP:", ip)
    print("TIMESTAMP:", timestamp)

if __name__ == "__main__":
    agrupar_alertas()

