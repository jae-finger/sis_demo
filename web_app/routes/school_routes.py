# web_app/routes/school_routes.py

from web_app.models import db, Student, Score, Course, Teacher
from flask import Blueprint, render_template, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

school_routes = Blueprint("school_routes", __name__)


@school_routes.route("/school")
def population():
    students = Student.query.all()
    teachers = Teacher.query.all()
    courses = Course.query.all()
    scores = Score.query.all()
    return render_template("school.html", students=students, teachers=teachers, courses=courses, scores=scores)


@school_routes.route("/seedx")
def seed_db():
    db.session.add(Student(student_name="Jon"))
    db.session.add(Student(student_name="Tony"))
    db.session.add(Student(student_name="Sandy"))
    db.session.add(Student(student_name="Ryan"))
    db.session.add(Student(student_name="Mike"))
    db.session.add(Student(student_name="Hugo"))
    db.session.add(Student(student_name="Jesse"))
    db.session.add(Student(student_name="Paul"))
    db.session.add(Student(student_name="Kathi"))
    db.session.add(Teacher(teacher_name="Gary"))
    db.session.add(Teacher(teacher_name="Jayce"))
    db.session.add(Teacher(teacher_name="Jason"))
    db.session.add(Course(course_name="Jason's Woodshop Class"))
    db.session.add(Course(course_name="Gary's Dart Class"))
    db.session.add(Course(course_name="Jayce's Poetry Class"))
    db.session.commit()
    students = Student.query.all()
    teachers = Teacher.query.all()
    courses = Course.query.all()
    scores = Score.query.all()
    return render_template("school.html", students=students, teachers=teachers, courses=courses, scores=scores)

@school_routes.route("/clearx")
def clear_db():
    Student.query.delete()
    Teacher.query.delete()
    Course.query.delete()
    db.session.commit()
    students = Student.query.all()
    teachers = Teacher.query.all()
    courses = Course.query.all()
    scores = Score.query.all()
    return render_template("school.html", students=students, teachers=teachers, courses=courses, scores=scores)
