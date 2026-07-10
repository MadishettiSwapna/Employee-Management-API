from database.database import db


class Employee(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    department = db.Column(db.String(100), nullable=False)

    designation = db.Column(db.String(100), nullable=False)

    salary = db.Column(db.Float, nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    phone = db.Column(db.String(20), nullable=False)