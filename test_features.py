from src.data_feed import initialize_mt5, get_data
from src.features import add_features

initialize_mt5()

df = get_data()

df = add_features(df)

print(df.tail())

print("\nColumns:")
print(df.columns)