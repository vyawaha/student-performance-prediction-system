import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

attendance = np.random.randint(40, 100, n)
study_hours = np.random.randint(1, 35, n)
quiz_avg = np.random.randint(30, 100, n)
assign_avg = np.random.randint(35, 100, n)
midterm = np.random.randint(25, 100, n)
lms_logins = np.random.randint(0, 30, n)
forum_posts = np.random.randint(0, 20, n)

noise = np.random.normal(0, 10, n)

performance_score = (
    0.20 * attendance +
    0.15 * study_hours +
    0.20 * quiz_avg +
    0.20 * assign_avg +
    0.20 * midterm +
    0.05 * lms_logins +
    0.02 * forum_posts +
    noise
)

passed = (performance_score >= 65).astype(int)

df = pd.DataFrame({
    "attendance_pct": attendance,
    "study_hours_wk": study_hours,
    "quiz_avg": quiz_avg,
    "assign_avg": assign_avg,
    "midterm": midterm,
    "lms_logins_wk": lms_logins,
    "forum_posts": forum_posts,
    "passed": passed
})

df.to_csv("data/synthetic_students.csv", index=False)

print(df.head())
print("\nDataset Created Successfully")