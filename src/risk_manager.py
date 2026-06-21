def check_risk(balance, risk_percent=1, daily_loss=3):
    max_risk = balance * (risk_percent / 100)
    return max_risk