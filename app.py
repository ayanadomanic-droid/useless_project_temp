import os
import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    report = None
    error = None

    if request.method == "POST":

        city = request.form.get("city", "").strip()
        temperature_raw = request.form.get("temperature", "").strip()
        condition = request.form.get("condition", "").strip().lower()

        if not city or not temperature_raw or not condition:
            error = "Please fill in all fields."
            return render_template("index.html", report=report, error=error)

        try:
            temperature = float(temperature_raw)
        except ValueError:
            error = "Temperature must be a number."
            return render_template("index.html", report=report, error=error)

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

    return render_template("index.html", report=report, error=error)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
