from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "ICC Rankings API"

@app.route("/teams")
def getAllTeams():
    return "All Teams will be displayed here."