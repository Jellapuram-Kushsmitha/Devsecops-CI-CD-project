from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
import os

print("hello")

app = Flask(__name__)

# ✅ Secure SECRET KEY from environment
app.config['SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")

if not app.config['SECRET_KEY']:
    raise ValueError("APP_SECRET_KEY environment variable not set")

# ✅ Enable CSRF protection
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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)