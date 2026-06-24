from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV
df = pd.read_csv("LOGIN_PAGE/student_submission_status.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    rollno = request.form['rollno']
    password = request.form['password']

    student = df[
        (df['Roll No'].astype(str) == rollno) &
        (df['Name'].astype(str).str.lower() == password.lower())
    ]

    if student.empty:
        return """
        <h1 style='color:red;text-align:center;'>
        Invalid Roll Number or Password
        </h1>
        """

    return render_template(
        "dashboard.html",
        name=student.iloc[0]['Name'],
        rollno=student.iloc[0]['Roll No'],
        status=student.iloc[0]['Status']
    )

if __name__ == '__main__':
    app.run(debug=True)