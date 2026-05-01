import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

numeric_features = [
    "attendance_pct",
    "study_hours_wk",
    "quiz_avg",
    "assign_avg",
    "midterm",
    "lms_logins_wk",
    "forum_posts"
]

numeric_transformer = Pipeline([
    ("scaler", StandardScaler())
])

pre = ColumnTransformer([
    ("num", numeric_transformer, numeric_features)
])