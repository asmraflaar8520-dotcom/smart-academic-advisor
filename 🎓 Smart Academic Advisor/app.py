import numpy as np
import pandas as pd
from flask import Flask, request, render_template

# ===============================
# Load Dataset
# ===============================
df = pd.read_csv("students_5000_logical.csv")

FEATURES = ["attendance", "study_hours", "assignments", "quizzes", "difficulty", "gpa"]
TARGET = "final_grade"

# ===============================
# Normalize Features
# ===============================
X = df[FEATURES].values
y = df[TARGET].values.reshape(-1, 1)

X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X_norm = (X - X_mean) / X_std

# ===============================
# Linear Regression From Scratch
# ===============================
def train(X, y, lr=0.01, epochs=3000):
    weights = np.zeros((X.shape[1], 1))
    bias = 0
    m = len(y)
    for _ in range(epochs):
        y_pred = np.dot(X, weights) + bias
        dw = np.dot(X.T, (y_pred - y)) / m
        db = np.sum(y_pred - y) / m
        weights -= lr * dw
        bias -= lr * db
    return weights, bias

weights, bias = train(X_norm, y)

def predict_final(input_data):
    input_norm = (input_data - X_mean) / X_std
    return float(np.dot(input_norm, weights) + bias)

# ===============================
# Flask App
# ===============================
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    max_vals = {f: int(df[f].max()) for f in FEATURES}
    max_vals["gpa"] = float(df["gpa"].max())

    if request.method == "POST":
        values = np.array([[float(request.form[f]) for f in FEATURES]])
        final_grade = predict_final(values)
        status = "✅ SAFE" if final_grade >= 50 else "⚠️ AT RISK"
        cls = "safe" if final_grade >= 50 else "risk"
        return render_template("index.html", FEATURES=FEATURES, max_vals=max_vals,
                               result=status, final_grade=round(final_grade,2), cls=cls)
    return render_template("index.html", FEATURES=FEATURES, max_vals=max_vals)

if __name__ == "__main__":
    app.run(debug=True)
