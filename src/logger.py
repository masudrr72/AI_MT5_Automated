import pandas as pd
import os

def log_trade(data, file="data/trade_log.csv"):
    df = pd.DataFrame([data])

    if os.path.exists(file):
        old = pd.read_csv(file)
        df = pd.concat([old, df], ignore_index=True)

    df.to_csv(file, index=False)
    