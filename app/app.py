from flask import Flask, request
from flask_wtf.csrf import CSRFProtect

print("hello")

app = Flask(__name__)

# 🔐 Required for CSRF protection
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-for-local-use')

# 🔐 Enable CSRF protection
csrf = CSRFProtect(app)

@app.route("/", methods=["GET"])
def home():
    return "Hello DevSecOps!"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # intentionally insecure (for demo)
    if username == "admin" and password == "admin":
        return "Logged in!"
    return "Invalid credentials"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)