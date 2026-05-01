🚀 Student Performance Prediction System










📌 Overview

The Student Performance Prediction System is an end-to-end Machine Learning project that predicts student academic outcomes using behavioral and academic indicators such as:

Attendance rate
Study hours per week
Quiz performance
Assignment scores
Midterm results
LMS engagement activity

It identifies whether a student is:

✅ High Performer
⚠️ At Risk Student
📊 Average Performer

This project simulates real-world EdTech analytics systems used in universities and learning platforms.

🎯 Problem Statement

Educational institutions often fail to detect struggling students early.

This system solves that by:

Predicting academic risk early
Enabling timely intervention
Improving student success rates
Reducing dropout probability
🧠 Machine Learning Approach
Type: Supervised Learning (Classification)
Model: XGBoost Classifier
Pipeline: Scikit-learn Pipeline
Evaluation Metrics:
Accuracy
F1 Score
ROC-AUC
Explainability: Feature Importance Analysis

🏗️ Architecture
Student Data
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
XGBoost Model Training
   ↓
FastAPI Backend
   ↓
Swagger Testing Interface
   ↓
Prediction Output (Risk / Safe)

⚙️ Tech Stack
Layer	Technology
Language	Python 3.11
ML Model	XGBoost
API Framework	FastAPI
Data Processing	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Model Explainability	Feature Importance
Server	Uvicorn

📂 Project Structure
Student-Performance-Prediction/
│
├── data/
├── src/
├── serving/
├── models/
├── outputs/
├── images/
├── requirements.txt
├── README.md
└── main.py

🚀 How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/vyawaha/student-performance-prediction.git
cd student-performance-prediction
2️⃣ Create Virtual Environment
python -m venv venv
.\venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Generate Dataset
python src/data_generator.py
5️⃣ Train Model
python src/train.py
6️⃣ Run API Server
uvicorn serving.app:app --reload
🌐 Access API
Swagger UI:
http://127.0.0.1:8000/docs
📡 API Endpoints
🏠 Home
GET /

🎯 Predict Student Performance
POST /predict
Sample Request:
{
  "attendance_pct": 70,
  "study_hours_wk": 10,
  "quiz_avg": 65,
  "assign_avg": 68,
  "midterm": 62,
  "lms_logins_wk": 7,
  "forum_posts": 2
}
Sample Response:
{
  "prediction": 0,
  "probability": 0.46,
  "status": "At Risk Student"
}

📊 Model Performance
Metric	Score
Accuracy	87%
F1 Score	0.85
ROC-AUC	0.91

📸 Outputs & Visualizations
📉 Confusion Matrix


📈 ROC Curve


📊 Feature Importance


🖥️ API Interface

Swagger UI


🧪 Prediction Samples

⚠️ At Risk Student


✅ High Performer


🔍 Key Insights
Attendance is the strongest predictor of success
Quiz + assignment scores strongly influence outcomes
LMS engagement correlates with performance
Low study hours → high failure risk

🌍 Real-World Applications

Used in:

🎓 Universities
📚 EdTech platforms
🧑‍🏫 Coaching institutes
📊 Learning analytics dashboards
🧠 Adaptive learning systems

🚀 Future Improvements
SHAP explainability integration
Next.js dashboard UI
Docker containerization
Cloud deployment (AWS/Azure)
MLflow tracking system
Real-time student monitoring

👨‍💻 Author
Muktai Vyawahare
Student ML Project (Portfolio Build)
Focused on Data Science + ML Engineering + Backend Systems