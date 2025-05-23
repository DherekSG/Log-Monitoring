import pandas as pd 

def load_logs(path):
    return pd.read_csv(path, parse_dates=['timestamp'])