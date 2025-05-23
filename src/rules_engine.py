import pandas as pd
import numpy as np
from datetime import time


def fora_do_horario(timestamp, horario_inicio, horario_fim):
    hora = timestamp.time()
    return not (horario_inicio <= hora <= horario_fim)

def porta_fechada(porta, porta_fechada):
    return porta in porta_proibidas

def detectar_falhas(df, limite):
    falhas = df[df['status'] == 'failed']
    counts = falhas.groupby(['username', 'ip_address']).size()
    return counts[counts > limite].reset_index(name='tentativas')