from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Temporary "database" (use PostgreSQL/MySQL in production)
users = {}

@app.route('/')
def index():
    return render_template('landing_page/index.html')

@app.route('/login', methods=["GET"])
def login_page():
    return render_template('signup_login/login.html')

@app.route('/signup', methods=["GET"])
def signup_page():
    return render_template('signup_login/signup.html')

# API route for signup
@app.route('/signup', methods=["POST"])
def signup_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if email in users:
        return jsonify({"error": "User already exists"}), 400

    users[email] = generate_password_hash(password)
    return jsonify({"message": "Signup successful"}), 201

# API route for login
@app.route('/login', methods=["POST"])
def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if email not in users or not check_password_hash(users[email], password):
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"message": "Login successful"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
