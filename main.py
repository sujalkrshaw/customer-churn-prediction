import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

# Create folders
os.makedirs("models", exist_ok=True)

# -----------------------------
# DATA
# -----------------------------
np.random.seed(42)

data = pd.DataFrame({
    "tenure": np.random.randint(1, 60, 200),
    "monthly_charges": np.random.randint(100, 500, 200),
    "support_calls": np.random.randint(0, 10, 200),
    "contract_type": np.random.choice(["Monthly", "Yearly"], 200)
})

# Better churn logic
prob = (
    (data["tenure"] < 20).astype(int) * 0.4 +
    (data["support_calls"] > 4).astype(int) * 0.3 +
    (data["monthly_charges"] > 300).astype(int) * 0.3
)

noise = np.random.rand(len(data)) * 0.3
data["churn"] = np.where(prob + noise > 0.5, 1, 0)

# Encode
le = LabelEncoder()
data["contract_type"] = le.fit_transform(data["contract_type"])

X = data.drop("churn", axis=1)
y = data["churn"]

# Split (IMPORTANT)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save
joblib.dump(model, "models/churn_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Model saved successfully!")