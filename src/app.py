import os
from flask import Flask, request

app = Flask(__name__)
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_123')

@app.route('/')
def index():
    return "Hello World"

@app.route('/admin')
def admin():
    token = request.headers.get('Authorization')
    if token == 'Bearer admin_token_12345':
        return "Welcome admin!"
    return "Forbidden", 403

if __name__ == '__main__':
    app.run(debug=True)
