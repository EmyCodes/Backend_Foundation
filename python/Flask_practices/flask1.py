#!/usr/bin/python3.11

from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': "EmyCodes",
        "title": "Post 1",
        "content": "First Post",
        "date_posted": "Sep 26, 2023"
    },
    {
        'author': "MzipTech",
        "title": "Post 2",
        "content": "Second Post",
        "date_posted": "Sep 27, 2023"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="EmyCodes Page", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="Flask Blog")

if __name__ == "__main__":
    app.run(debug=True)
