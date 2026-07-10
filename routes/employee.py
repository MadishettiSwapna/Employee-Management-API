from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.employee import Employee
from database.database import db

employee = Blueprint("employee", __name__)

@employee.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():

    current_user = get_jwt_identity()

    return {
        "message": "Welcome",
        "user": current_user
    },200
    
@employee.route("/employees", methods=["POST"])
@jwt_required()
def create_employee():

    data = request.get_json()

    name = data.get("name")
    department = data.get("department")
    designation = data.get("designation")
    salary = data.get("salary")
    email = data.get("email")
    phone = data.get("phone")

    # Validation
    if not all([name, department, designation, salary, email, phone]):
        return {
            "error": "All fields are required."
        }, 400

    # Duplicate email check
    existing_employee = Employee.query.filter_by(email=email).first()

    if existing_employee:
        return {
            "error": "Employee email already exists."
        }, 409

    # Create employee object
    new_employee = Employee(
        name=name,
        department=department,
        designation=designation,
        salary=salary,
        email=email,
        phone=phone
    )

    # Save to database
    db.session.add(new_employee)
    db.session.commit()

    return {
        "message": "Employee added successfully."
    }, 201

@employee.route("/employees", methods=["GET"])

@jwt_required()

def get_employees():

    employees = Employee.query.all()

    employee_list = []

    for emp in employees:
        employee_list.append({
            "id": emp.id,
            "name": emp.name,
            "department": emp.department,
            "designation": emp.designation,
            "salary": emp.salary,
            "email": emp.email,
            "phone": emp.phone
        })

    return employee_list, 200