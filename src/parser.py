import csv

def carregar_csv(caminho: str) -> list:
    """Carrega um arquivo CSV e retorna como lista de dicionários"""
    with open(caminho, newline='') as csvfile:
        return list(csv.DictReader(csvfile))
