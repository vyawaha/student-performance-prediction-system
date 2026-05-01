import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline

from xgboost import XGBClassifier

from pipeline import pre

df = pd.read_csv("data/synthetic_students.csv")

X = df.drop("passed", axis=1)
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = Pipeline([
    ("preprocessing", pre),
    ("classifier", XGBClassifier())
])

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(classification_report(y_test, pred))

joblib.dump(model, "models/model.joblib")

print("Model Saved")