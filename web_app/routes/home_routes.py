# web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    return render_template("index.html")

@home_routes.route("/sql")
def sql_page():
    return render_template("sql.html")

@home_routes.route("/stats")
def stats_page():
    return render_template("stats.html")