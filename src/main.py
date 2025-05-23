from src.rules_engine import fora_do_horario, porta_proibida, detectar_falhas
from src.alert_manager import salvar_alerta
import csv

LOG_FILE = 'logs/sample_log.csv'

def processar_log():
    with open(LOG_FILE, newline='') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            horario = linha['hora']
            porta = int(linha['porta'])
            status = linha['status']
            ip = linha['ip']

            if fora_do_horario(horario):
                salvar_alerta("fora_do_horario", linha)

            if porta_proibida(int(porta)):
                salvar_alerta("porta_proibida", linha)

            if detectar_falhas(status, ip):
                salvar_alerta("falhas_login", linha)

if __name__ == "__main__":
    processar_log()
