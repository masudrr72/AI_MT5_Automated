def generate_signal(model, latest_data):
    """
    Returns: BUY / SELL / NO TRADE
    """

    X = latest_data[["rsi", "ema20", "ema50", "atr"]]

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0]

    confidence = max(prob)

    # Safety filter (VERY IMPORTANT)
    if confidence < 0.60:
        return "NO TRADE", confidence

    if pred == 1:
        return "BUY", confidence
    else:
        return "SELL", confidence