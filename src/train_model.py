import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model(df):
    # Features (inputs)
    features = ["rsi", "ema20", "ema50", "atr"]

    X = df[features]
    y = df["target"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Prediction
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print("Model Accuracy:", acc)

    # Save model
    joblib.dump(model, "models/model.pkl")

    print("Model saved successfully!")

    return model