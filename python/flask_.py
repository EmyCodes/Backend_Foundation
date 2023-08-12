#!/usr/bin/python3

from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Welcome to my Page!"

@app.route('/<name>')
def user(name="EmyCodes"):
    return f"<h1>Hello {name}</h1>!"

def admin():
    return(url_for("home"))


if __name__ == "__main__":
    app.run()
