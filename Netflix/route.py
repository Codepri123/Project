import pandas as pd
from flask import Flask, request, render_template,send_file

app = Flask(__name__)

@app.route('/')
def front_page():
    return render_template("front_page.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/csv_file')
def csv_file():
    df = pd.read_csv("Netflix_clean_data_file.csv")
    return df.to_html(index=False)
@app.route('/clean_code')
def clean_code():
    with open("netflix.py", "r", encoding="utf-8") as file:
        code = file.read()
    return f"<pre>{code}</pre>"
@app.route('/powerbi_dashboard')
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
