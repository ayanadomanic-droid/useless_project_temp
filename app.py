from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    report = None

    if request.method == "POST":

        city = request.form["city"]
        temperature = float(request.form["temperature"])
        condition = request.form["condition"].lower()

        # Drama level
        if temperature > 35:
            drama = "EXTREMELY HIGH 🔥"
        elif temperature > 30:
            drama = "HIGH 😭"
        else:
            drama = "LOW 😐"

        # Motivation
        if "rain" in condition:
            motivation = "5% 😴"
        else:
            motivation = "42% 🤷"

        # Frog activity
        if "rain" in condition:
            frog = "EXTREMELY HIGH 🐸"
        else:
            frog = "Probably sleeping 🐸"

        # Random useless message
        messages = [
            "The weather has chosen chaos.",
            "Nobody needed this information.",
            "Congratulations. You checked the weather.",
            "This information changes absolutely nothing.",
            "Please go outside. Or don't."
        ]

        message = random.choice(messages)

        report = {
            "city": city,
            "temperature": temperature,
            "condition": condition,
            "drama": drama,
            "motivation": motivation,
            "frog": frog,
            "message": message
        }

    return render_template("index.html", report=report)


if __name__ == "__main__":
    app.run(debug=True)
