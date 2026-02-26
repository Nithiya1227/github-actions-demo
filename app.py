from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps!"

print("CI/CD Pipeline Working Successfully!")