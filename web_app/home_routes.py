from flask import Flask

app = Flask(__name__)


@app.route("/")
def land_page():
    print("YOU VISITED THE LANDING PAGE")
    return "Landing Page (TODO)"
