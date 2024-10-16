from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    answers = db.relationship('StudentAnswers', backref='student', lazy=True)
    scores = db.relationship('Score', backref='student', lazy=True)

class StudentAnswers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer_text = db.Column(db.String(255), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    result = db.Column(db.String(6), nullable=False)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    courses = db.relationship('Course', backref='doctor', lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    questions = db.relationship('Questions', backref='courses', lazy=True)
    scores = db.relationship('Score', backref='courses', lazy=True)

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    answer_id = db.relationship('StudentAnswers', backref='questions', lazy=True)

class Score(db.Model):
    sore = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True, nullable=False)
