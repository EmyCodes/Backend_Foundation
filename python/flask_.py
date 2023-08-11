#!/usr/bin/python3

from flask import Flask


app = Flask(__name__)

@app.route('/')
def home(name="EmyCodes"):
    return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
    app.run()
