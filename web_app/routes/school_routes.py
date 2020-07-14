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
    db.session.add(Student(id=111, student_name="Jon"))
    db.session.add(Student(id=222, student_name="Tony"))
    db.session.add(Student(id=333, student_name="Sandy"))
    db.session.add(Student(id=444, student_name="Ryan"))
    db.session.add(Student(id=555, student_name="Mike"))
    db.session.add(Student(id=666, student_name="Hugo"))
    db.session.add(Student(id=777, student_name="Jesse"))
    db.session.add(Student(id=888, student_name="Paul"))
    db.session.add(Student(id=999, student_name="Kathi"))
    db.session.add(Teacher(id=1111, teacher_name="Gary"))
    db.session.add(Teacher(id=4444, teacher_name="Jayce"))
    db.session.add(Teacher(id=7777, teacher_name="Jason"))
    db.session.add(Course(id=33, course_name="Jason's Woodshop Class", teacher_id=7777))
    db.session.add(Course(id=66,course_name="Gary's Dart Class", teacher_id=1111))
    db.session.add(Course(id=99,course_name="Jayce's Poetry Class", teacher_id=4444))
    # db.session.add(Score(class_id=1))
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
