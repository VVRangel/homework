from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ["Камень", "Ножницы", "Бумага"]

@app.route("/", methods=["GET", "POST"])
def index():
    player_choice = None
    computer_choice = None
    result = None

    if request.method == "POST":
        player_choice = request.form["choice"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "Ничья!"
        elif (
            (player_choice == "Камень" and computer_choice == "Ножницы") or
            (player_choice == "Ножницы" and computer_choice == "Бумага") or
            (player_choice == "Бумага" and computer_choice == "Камень")
        ):
            result = "Вы победили!"
        else:
            result = "Компьютер победил!"

    return render_template(
        "index.html",
        player_choice=player_choice,
        computer_choice=computer_choice,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)