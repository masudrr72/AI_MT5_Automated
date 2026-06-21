import MetaTrader5 as mt5
import pandas as pd

def initialize_mt5():
    if not mt5.initialize():
        print("MT5 initialize failed")
        quit()

def get_data(symbol="EURUSD", timeframe=mt5.TIMEFRAME_M15, n=200):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df