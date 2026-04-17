from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

# Safe default for testing
app.config.from_object('config.Config')

csrf = CSRFProtect(app)

@app.route("/", methods=["GET"])
def home():
    return "Hello DevSecOps!"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "admin":
        return "Logged in!"
    return "Invalid credentials"