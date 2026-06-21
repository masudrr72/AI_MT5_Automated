import joblib
from src.data_feed import initialize_mt5, get_data
from src.features import add_features
from src.strategy import generate_signal

initialize_mt5()

model = joblib.load("models/model.pkl")

df = get_data()
df = add_features(df)

latest = df.tail(1)

signal, confidence = generate_signal(model, latest)

print("Signal:", signal)
print("Confidence:", confidence)