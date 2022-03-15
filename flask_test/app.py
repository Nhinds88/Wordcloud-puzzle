import random
from templates.scripts.wcp import wcPuzzle
from distutils.log import debug
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "funsecrects"

@app.route("/")
def index():
    # flash("what's your name?")
    choice = random.choice([1,2,3])
    wcPuzzle(choice)
    return render_template("index.html")
    
@app.route("/cluzzle", methods=["POST", "GET"])
def cluzzle():
    # flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(debug = True)