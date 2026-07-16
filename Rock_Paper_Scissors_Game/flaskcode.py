from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    computer_choice = ""
    user_choice = ""

    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = np.random.choice(["Rock", "Paper", "Scissors"])

        match user_choice:
            case "Rock":
                if computer_choice == "Scissors":
                    result = "Rock hits Scissors. User Wins!"
                elif computer_choice == "Paper":
                    result = "Paper beats Rock. User Loses!"
                else:
                    result = "Tie Match!"

            case "Paper":
                if computer_choice == "Rock":
                    result = "Paper beats Rock. User Wins!"
                elif computer_choice == "Scissors":
                    result = "Scissors beat Paper. User Loses!"
                else:
                    result = "Tie Match!"

            case "Scissors":
                if computer_choice == "Paper":
                    result = "Scissors beat Paper. User Wins!"
                elif computer_choice == "Rock":
                    result = "Rock hits Scissors. User Loses!"
                else:
                    result = "Tie Match!"

    return render_template(
        "index.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)