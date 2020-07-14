# web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String)

# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     class_name = db.Column(db.String)
#     teacher = db.relationship('Teacher', backref='course')

# class Teacher(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     teacher_name = db.Column(db.String)
#     class_id = db.Column(db.Integer, db.ForeignKey('course.id'))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slot1 = db.Column(db.Integer)
    slot2 = db.Column(db.Integer)
    slot3 = db.Column(db.Integer)
    