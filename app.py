import datetime
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/<string:name>")
def name(name):
    return f"Hello, {name}!"

@app.route("/headline", methods=["GET", "POST"])
def headline():
    headline = "Hi, Emma!"
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("index.html", headline = headline, notes = session["notes"])

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline = headline)

@app.route("/newyear")
def newyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("newyear.html", new_year = new_year)

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "please submit the form first"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)