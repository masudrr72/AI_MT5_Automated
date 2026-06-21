import pandas as pd

def create_dataset(df, horizon=5):
    """
    horizon = how many candles ahead we predict
    """

    df = df.copy()

    # Future price (shifted)
    df["future_close"] = df["close"].shift(-horizon)

    # Target creation
    df["target"] = (df["future_close"] > df["close"]).astype(int)

    # Remove last rows (NaN from shift)
    df = df.dropna()

    return df