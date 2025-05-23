import csv
from src.rules_engine import fora_do_horario, porta_proibida, detectar_falhas, falhas_alertas

LOG_PATH = "logs/sample_log.csv"  # caminho correto para seu log

def processar_log():
    tentativas_falha = {}
    alertas_falhas_login = []

    with open(LOG_PATH, newline='') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            fora_do_horario(linha)
            porta_proibida(linha)
            detectar_falhas(linha, tentativas_falha, limite=3)
    
    print("Alertas de falha login repetida detectados:")
    for alerta in falhas_alertas:
        print(alerta)

if __name__ == "__main__":
    processar_log()
