# web_app/routes/student_routes.py

from flask import Blueprint, render_template

student_routes = Blueprint("student_routes", __name__)

@student_routes.route("/students")
def student_list():
    return render_template("students.html", message="Here is the list of students in D3000:")