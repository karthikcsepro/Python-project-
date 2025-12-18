import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

data = {
    "duration": [10, 200, 5, 300, 20, 400, 15, 500],
    "src_bytes": [100, 5000, 80, 7000, 120, 9000, 90, 11000],
    "dst_bytes": [50, 2000, 30, 3000, 60, 4000, 40, 6000],
    "failed_logins": [0, 3, 0, 5, 0, 7, 0, 10],
    "label": [0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

plt.bar(["Normal", "Attack"], y.value_counts())
plt.title("Network Traffic Distribution")
plt.show()
