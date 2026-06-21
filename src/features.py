import pandas_ta as ta

def add_features(df):
    # Trend indicator
    df["rsi"] = ta.rsi(df["close"], length=14)

    # Trend direction
    df["ema20"] = ta.ema(df["close"], length=20)
    df["ema50"] = ta.ema(df["close"], length=50)

    # Volatility
    df["atr"] = ta.atr(df["high"], df["low"], df["close"], length=14)

    # Clean data
    df = df.dropna()

    return df