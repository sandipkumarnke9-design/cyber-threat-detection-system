import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
data = pd.read_csv('../data/network_data.csv')

# Convert text → numbers
data = pd.get_dummies(data)

# Split input/output
X = data.drop('label', axis=1)
y = data['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained successfully")