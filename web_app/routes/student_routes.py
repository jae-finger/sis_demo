# web_app/routes/student_routes.py

from web_app.models import db, Student, parse_records
from flask import Blueprint, render_template, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

student_routes = Blueprint("student_routes", __name__)


@student_routes.route("/students")
def student_list():
    students = Student.query.all()
    return render_template("students.html", students=students)


@student_routes.route("/seedx")
def seed_students():
    db.session.add(Student(student_name="Jon"))
    db.session.add(Student(student_name="Tony"))
    db.session.add(Student(student_name="Sandy"))
    db.session.add(Student(student_name="Ryan"))
    db.session.add(Student(student_name="Mike"))
    db.session.add(Student(student_name="Hugo"))
    db.session.add(Student(student_name="Jesse"))
    db.session.add(Student(student_name="Paul"))
    db.session.add(Student(student_name="Kathi"))
    db.session.commit()
    students = Student.query.all()
    return render_template("students.html", students=students)

@student_routes.route("/clearx")
def clear_students():
    Student.query.delete()
    db.session.commit()
    students = Student.query.all()
    return render_template("students.html", students=students)
