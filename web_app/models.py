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

def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON
    Param: database_records (a list of db.Model instances)
    Example: parse_records(User.query.all())
    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records