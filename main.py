from flask import Flask, session, render_template, redirect, url_for, request

app = Flask('app')

app.secret_key = "supersecretkey"

@app.route('/')
def homepage():
    return render_template("home.html")

app.run(host='0.0.0.0', port=8080)