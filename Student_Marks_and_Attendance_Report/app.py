from flask import Flask, render_template
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report')
def report():

    students = ["Arnav", "Priyanka", "Canon", "Divyansh", "Elsa"]
    marks = [78, 85, 90, 66, 88]
    attendance = [90, 85, 95, 80, 92]

    # Create static folder if it doesn't exist
    static_folder = os.path.join(app.root_path, "static")
    os.makedirs(static_folder, exist_ok=True)

    # Create graph
    plt.figure(figsize=(8, 6))

    plt.subplot(2, 2, 1)
    plt.plot(students, marks, marker="o")
    plt.title("Marks")
    plt.grid()

    plt.subplot(2, 2, 2)
    plt.bar(students, attendance)
    plt.title("Attendance")


    plt.subplot(2, 2, 3)
    plt.scatter(students, marks)
    plt.title("Scatter")
    plt.grid()

    plt.subplot(2, 2, 4)
    plt.pie(marks, labels=students, autopct="%1.1f%%")
    plt.title("Pie Chart")

    plt.tight_layout()

    # Save image
    image_path = os.path.join(static_folder, "report.png")
    plt.savefig(image_path)
    plt.close()

    return render_template('report.html')

if __name__ == "__main__":
    app.run(debug=True)