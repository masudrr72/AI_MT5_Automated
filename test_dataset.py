from src.data_feed import initialize_mt5, get_data
from src.features import add_features
from src.dataset import create_dataset

initialize_mt5()

df = get_data()
df = add_features(df)
df = create_dataset(df)

print(df[["close", "future_close", "target"]].tail())

print("\nDataset shape:", df.shape)