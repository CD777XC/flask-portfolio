from flask import Flask, render_template, request

portfolio = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/exp")
def exp():
    return render_template("exp.html")