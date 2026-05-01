from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Student Performance Prediction API",
    version="1.0.0"
)

# Load model
model = joblib.load(r"models/model.joblib")


# Input schema
class StudentData(BaseModel):
    attendance_pct: float
    study_hours_wk: float
    quiz_avg: float
    assign_avg: float
    midterm: float
    lms_logins_wk: float
    forum_posts: float


@app.get("/")
def home():
    return {
        "message": "Student Performance Prediction API Running Successfully"
    }


@app.post("/predict")
def predict(data: StudentData):

    input_data = pd.DataFrame([{
        "attendance_pct": data.attendance_pct,
        "study_hours_wk": data.study_hours_wk,
        "quiz_avg": data.quiz_avg,
        "assign_avg": data.assign_avg,
        "midterm": data.midterm,
        "lms_logins_wk": data.lms_logins_wk,
        "forum_posts": data.forum_posts
    }])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    return {
        "prediction": int(prediction),
        "probability": round(float(probability), 4),
        "status": (
            "At Risk Student"
            if prediction == 0
            else "Good Performance Expected"
        )
    }