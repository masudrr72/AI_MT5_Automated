def generate_signal(model, latest_data):
    features = ["rsi", "ema20", "ema50", "atr"]

    X = latest_data[features]

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0]
    confidence = max(prob)

    ema20 = latest_data["ema20"].values[0]
    ema50 = latest_data["ema50"].values[0]

    # Trend filter
    bullish = ema20 > ema50
    bearish = ema20 < ema50

    # No trade zone (sideways market)
    if abs(ema20 - ema50) < 0.0005:
        return "NO TRADE", confidence

    # Confidence filter
    if confidence < 0.65:
        return "NO TRADE", confidence

    # Final decision logic
    if pred == 1 and bullish:
        return "BUY", confidence

    if pred == 0 and bearish:
        return "SELL", confidence

    return "NO TRADE", confidence