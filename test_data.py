from src.data_feed import initialize_mt5, get_data

initialize_mt5()

df = get_data()

print(df.head())

print("\nShape:", df.shape)