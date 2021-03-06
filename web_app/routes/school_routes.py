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
    db.session.add(Student(id=222, student_name="Tony"))
    db.session.add(Student(id=333, student_name="Sandy"))
    db.session.add(Student(id=444, student_name="Ryan"))
    db.session.add(Student(id=555, student_name="Mike"))
    db.session.add(Student(id=666, student_name="Hugo"))
    db.session.add(Student(id=777, student_name="Jesse"))
    db.session.add(Student(id=888, student_name="Paul"))
    db.session.add(Student(id=999, student_name="Kathi"))
    db.session.commit()
    db.session.add(Teacher(id=1111, teacher_name="Gary"))
    db.session.add(Teacher(id=4444, teacher_name="Jayce"))
    db.session.commit()
    db.session.add(Course(id=66,course_name="Gary's Dart Class", teacher_id=1111))
    db.session.add(Course(id=99,course_name="Jayce's Poetry Class", teacher_id=4444))
    db.session.commit()
    db.session.add(Score(class_id=66, student_id=222, assignment_name='hw_1', score=81))
    db.session.add(Score(class_id=66, student_id=222, assignment_name='hw_2', score=88))
    db.session.add(Score(class_id=66, student_id=222, assignment_name='hw_3', score=82))
    db.session.add(Score(class_id=66, student_id=222, assignment_name='exam_1', score=91))
    db.session.add(Score(class_id=66, student_id=333, assignment_name='hw_1', score=77))
    db.session.add(Score(class_id=66, student_id=333, assignment_name='hw_2', score=98))
    db.session.add(Score(class_id=66, student_id=333, assignment_name='hw_3', score=81))
    db.session.add(Score(class_id=66, student_id=333, assignment_name='exam_1', score=54))
    db.session.add(Score(class_id=66, student_id=444, assignment_name='hw_1', score=99))
    db.session.add(Score(class_id=66, student_id=444, assignment_name='hw_2', score=98))
    db.session.add(Score(class_id=66, student_id=444, assignment_name='hw_3', score=80))
    db.session.add(Score(class_id=66, student_id=444, assignment_name='exam_1', score=50))
    db.session.add(Score(class_id=66, student_id=555, assignment_name='hw_1', score=44))
    db.session.add(Score(class_id=66, student_id=555, assignment_name='hw_2', score=76))
    db.session.add(Score(class_id=66, student_id=555, assignment_name='hw_3', score=95))
    db.session.add(Score(class_id=66, student_id=555, assignment_name='exam_1', score=90))
    db.session.add(Score(class_id=99, student_id=666, assignment_name='hw_1', score=55))
    db.session.add(Score(class_id=99, student_id=666, assignment_name='hw_2', score=66))
    db.session.add(Score(class_id=99, student_id=666, assignment_name='hw_3', score=77))
    db.session.add(Score(class_id=99, student_id=666, assignment_name='exam_1', score=88))
    db.session.add(Score(class_id=99, student_id=777, assignment_name='hw_1', score=85))
    db.session.add(Score(class_id=99, student_id=777, assignment_name='hw_2', score=65))
    db.session.add(Score(class_id=99, student_id=777, assignment_name='hw_3', score=76))
    db.session.add(Score(class_id=99, student_id=777, assignment_name='exam_1', score=50))
    db.session.add(Score(class_id=99, student_id=888, assignment_name='hw_1', score=95))
    db.session.add(Score(class_id=99, student_id=888, assignment_name='hw_2', score=90))
    db.session.add(Score(class_id=99, student_id=888, assignment_name='hw_3', score=80))
    db.session.add(Score(class_id=99, student_id=888, assignment_name='exam_1', score=60))
    db.session.add(Score(class_id=99, student_id=999, assignment_name='hw_1', score=25))
    db.session.add(Score(class_id=99, student_id=999, assignment_name='hw_2', score=55))
    db.session.add(Score(class_id=99, student_id=999, assignment_name='hw_3', score=40))
    db.session.add(Score(class_id=99, student_id=999, assignment_name='exam_1', score=80))
    db.session.commit()
    students = Student.query.all()
    teachers = Teacher.query.all()
    courses = Course.query.all()
    scores = Score.query.all()
    return render_template("school.html", students=students, teachers=teachers, courses=courses, scores=scores)

@school_routes.route("/clearx")
def clear_db():
    def clear_data(session):
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            session.execute(table.delete())
        session.commit()
    clear_data(db.session)
    students = Student.query.all()
    teachers = Teacher.query.all()
    courses = Course.query.all()
    scores = Score.query.all()
    return render_template("school.html", students=students, teachers=teachers, courses=courses, scores=scores)
