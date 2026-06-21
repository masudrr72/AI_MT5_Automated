from src.data_feed import initialize_mt5, get_data
from src.features import add_features
from src.model import load_model, predict
from src.execution import open_trade
from src.logger import log_trade

import MetaTrader5 as mt5

initialize_mt5()
model = load_model()

symbol = "EURUSD"

df = get_data(symbol)
df = add_features(df)

latest = df.tail(1)

X = latest[["rsi", "ema20", "ema50", "atr"]]

pred, prob = predict(model, X)

confidence = max(prob[0])

if confidence > 0.80:
    if pred[0] == 1:
        order = "BUY"
    else:
        order = "SELL"

    result = open_trade(symbol, 0.01, order, 0, 0)

    log_trade({
        "symbol": symbol,
        "prediction": order,
        "confidence": confidence
    })