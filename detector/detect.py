import pickle
import pandas as pd
from detector.alert import send_alert

# Load model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_threat(features):
    df = pd.DataFrame([features])

    # Convert categorical → numeric
    df = pd.get_dummies(df)

    # Match columns
    for col in model.feature_names_in_:
        if col not in df:
            df[col] = 0

    df = df[model.feature_names_in_]

    prediction = model.predict(df)[0]

    if prediction == 1:
        send_alert("Suspicious activity detected!")
        return "🚨 Threat Detected"
    else:
        return "✅ Normal Traffic"