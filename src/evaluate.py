import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    RocCurveDisplay
)

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from xgboost import XGBClassifier

from pipeline import pre

# Load dataset
df = pd.read_csv("data/synthetic_students.csv")

# Features and target
X = df.drop("passed", axis=1)
y = df["passed"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model pipeline
model = Pipeline([
    ("preprocessing", pre),
    ("classifier", XGBClassifier())
])

# Train model
model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

# ==============================
# Confusion Matrix
# ==============================
cm = confusion_matrix(y_test, pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot()

plt.title("Confusion Matrix")

plt.savefig("outputs/confusion_matrix.png")

plt.close()

# ==============================
# ROC Curve
# ==============================
RocCurveDisplay.from_estimator(model, X_test, y_test)

plt.title("ROC Curve")

plt.savefig("outputs/roc_curve.png")

plt.close()

# ==============================
# Feature Importance
# ==============================
feature_names = X.columns

importances = model.named_steps[
    "classifier"
].feature_importances_

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

# Plot feature importance
plt.figure(figsize=(10, 6))

plt.barh(
    importance_df["Feature"],
    importance_df["Importance"]
)

plt.xlabel("Importance Score")

plt.ylabel("Features")

plt.title("Feature Importance")

plt.gca().invert_yaxis()

plt.savefig("outputs/feature_importance.png")

plt.close()

print("Evaluation Graphs Saved Successfully")