import joblib
from src.data_feed import initialize_mt5, get_data
from src.features import add_features
from src.backtest_real import backtest_real

initialize_mt5()

model = joblib.load("models/model.pkl")

df = get_data()
df = add_features(df)

final_balance, equity = backtest_real(model, df)

print("Final Balance:", final_balance)