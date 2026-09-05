# 🎓 Student Exam Score Predictor

A simple web app that predicts a student's expected exam score based on 
study hours, attendance, and previous performance — built to explore how 
linear regression can model real academic patterns.

## 🔍 Why this project?
As a CSE (Data Science) student, I wanted to move beyond notebooks and 
build something interactive — a tool where inputs actually produce a live 
prediction, not just a static chart. This project covers the full pipeline: 
data cleaning, model training, and deployment as a usable web app.

## ⚙️ How it works
1. Dataset: [Student Performance Dataset](https://www.kaggle.com/datasets/nabeelqureshitiii/student-performance-dataset)
2. Cleaned and explored data using Pandas
3. Trained a Linear Regression model using scikit-learn
4. Built an interactive UI with Streamlit where users input their stats 
   and get an instant predicted score

## 📊 Model Performance
- R² Score: 0.84 (fill in your real number)
- Features used: hours studied, attendance %, previous exam score

## 🖥️ Tech Stack
- Python
- Pandas, scikit-learn
- Streamlit

## 🚀 Run it locally
\`\`\`bash
git clone https://github.com/salitacorreia-4/student-score-predictor.git
cd student-score-predictor
pip install -r requirements.txt
streamlit run app.py
\`\`\`

## 🔮 Future improvements
- Try Random Forest / XGBoost for comparison
- Add more features (sleep hours, extracurriculars)
- Deploy live on Streamlit Community Cloud

## 🙋 About me
2nd year CSE (Data Science) student at DJ Sanghvi College of Engineering, 
learning by building. Connect with me on [linkedin.com/in/salita-correia-4766b039a].
