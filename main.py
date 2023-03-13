from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

actual_number = random.randint(1,10)

@app.route("/number")
def number():
    guessed_number = int(request.args["Number"])
    if guessed_number < actual_number:
        return render_template("go_high.html")
    elif guessed_number > actual_number:
        return render_template("go_low.html")
    else:
        return render_template("perfection.html")
    
@app.route("/redirect")
def re():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
    