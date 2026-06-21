import joblib

def load_model(path="models/model.pkl"):
    return joblib.load(path)

def predict(model, X):
    return model.predict(X), model.predict_proba(X)
    