def backtest_real(model, df, rr=2, risk_per_trade=1):
    features = ["rsi", "ema20", "ema50", "atr"]

    balance = 1000
    equity_curve = []

    for i in range(len(df) - 2):

        X = df[features].iloc[i:i+1]

        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0]
        confidence = max(prob)

        if confidence < 0.65:
            equity_curve.append(balance)
            continue

        entry = df["close"].iloc[i]
        next_high = df["high"].iloc[i+1]
        next_low = df["low"].iloc[i+1]

        atr = df["atr"].iloc[i]

        # Define SL & TP
        sl = atr
        tp = atr * rr

        trade_result = 0

        # BUY trade
        if pred == 1:
            if next_low <= entry - sl:
                trade_result = -risk_per_trade
            elif next_high >= entry + tp:
                trade_result = risk_per_trade * rr

        # SELL trade
        elif pred == 0:
            if next_high >= entry + sl:
                trade_result = -risk_per_trade
            elif next_low <= entry - tp:
                trade_result = risk_per_trade * rr

        balance += trade_result
        equity_curve.append(balance)

    return balance, equity_curve