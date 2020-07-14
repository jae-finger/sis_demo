# web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String)
    # scores = db.relationship('Score')

# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     class_name = db.Column(db.String)
#     teacher = db.relationship('Teacher', backref='course')

# class Teacher(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     teacher_name = db.Column(db.String)
#     class_id = db.Column(db.Integer, db.ForeignKey('course.id'))

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    teachers = db.relationship('Teacher', uselist=False, back_populates='courses')
    # scores = db.relationship('Score')

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String)
    courses = db.relationship('Course', back_populates='teachers')

class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    # student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    homework = db.Column(db.String)
    score = db.Column(db.Integer)

# class Schedule(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     slot1 = db.Column(db.Integer)
#     slot2 = db.Column(db.Integer)
#     slot3 = db.Column(db.Integer)
