from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/exp")
def exp():
    return render_template("exp.html")

@app.route("/<article>")
def article(article):
    return render_template(f"{article}.html")