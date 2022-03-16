from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "ICC Rankings API v 2.1"