import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("data.csv")
df = df.dropna()

X = df[["weekly_self_study_hours", "attendance_percentage", "class_participation"]]  # adjust to your columns
y = df["total_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("R2 Score:", model.score(X_test, y_test))

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)