from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevSecOps!"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # intentionally insecure
    if username == "admin" and password == "admin":
        return "Logged in!"
    return "Invalid credentials"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)