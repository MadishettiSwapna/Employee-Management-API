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

@employee.route("/employees/<int:id>", methods=["GET"])

@jwt_required()

def get_employee(id):

    employee = Employee.query.get(id)

    if not employee:
        return {
            "error": "Employee not found."
        }, 404

    return {
        "id": employee.id,
        "name": employee.name,
        "department": employee.department,
        "designation": employee.designation,
        "salary": employee.salary,
        "email": employee.email,
        "phone": employee.phone
    }, 200

@employee.route("/employees/<int:id>", methods=["PUT"])

@jwt_required()

def update_employee(id):

    employee = Employee.query.get(id)

    if not employee:
        return {
            "error": "Employee not found."
        }, 404

    data = request.get_json()

    employee.name = data.get("name", employee.name)
    employee.department = data.get("department", employee.department)
    employee.designation = data.get("designation", employee.designation)
    employee.salary = data.get("salary", employee.salary)
    employee.email = data.get("email", employee.email)
    employee.phone = data.get("phone", employee.phone)

    db.session.commit()

    return {
        "message": "Employee updated successfully."
    }, 200

@employee.route("/employees/<int:id>", methods=["DELETE"])

@jwt_required()

def delete_employee(id):

    employee = Employee.query.get(id)

    if not employee:
        return {
            "error": "Employee not found."
        }, 404

    db.session.delete(employee)
    db.session.commit()

    return {
        "message": "Employee deleted successfully."
    }, 200