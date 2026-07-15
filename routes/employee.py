from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.employee import Employee
from database.database import db
from utils.decorators import admin_required

employee = Blueprint("employee", __name__)

@employee.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    """
    Dashboard
    ---
    tags:
      - Dashboard
    security:
      - BearerAuth: []
    responses:
      200:
        description: Dashboard loaded successfully.
    """

    current_user = get_jwt_identity()

    return {
        "message": "Welcome",
        "user": current_user
    },200
    
@employee.route("/employees", methods=["POST"])
@jwt_required()
@admin_required
def create_employee():
    """
    Create employee.
    ---
    tags:
      - Employees
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
              department:
                type: string
              designation:
                type: string
              salary:
                type: integer
              email:
                type: string
              phone:
                type: string
    responses:
      201:
        description: Employee created.
    """

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
    """
    Get all employees.
    ---
    tags:
      - Employees
    parameters:
      - name: department
        in: query
        schema:
          type: string
      - name: designation
        in: query
        schema:
          type: string
      - name: name
        in: query
        schema:
          type: string
      - name: page
        in: query
        schema:
          type: integer
      - name: per_page
        in: query
        schema:
          type: integer
    responses:
      200:
        description: Employee list.
    """
    department = request.args.get("department")
    designation = request.args.get("designation")
    name = request.args.get("name")

    query = Employee.query

    if department:
        query = query.filter(
            Employee.department.ilike(f"%{department}%")
        )

    if designation:
        query = query.filter(
            Employee.designation.ilike(f"%{designation}%")
        )
    if name:
        query = query.filter(Employee.name.ilike(f"%{name}%"))
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    employees = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    employee_list = []

    for emp in employees.items:
        employee_list.append({
            "id": emp.id,
            "name": emp.name,
            "department": emp.department,
            "designation": emp.designation,
            "salary": emp.salary,
            "email": emp.email,
            "phone": emp.phone
        })

    return {
    "page": employees.page,
    "per_page": employees.per_page,
    "total": employees.total,
    "pages": employees.pages,
    "employees": employee_list
    }, 200

@employee.route("/employees/<int:id>", methods=["GET"])

@jwt_required()

def get_employee(id):
    """
    Get employee by ID.
    ---
    tags:
      - Employees
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Employee found.
      404:
        description: Employee not found.
    """

    employee = db.session.get(Employee, id)

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

@admin_required
def update_employee(id):
    """
    Update employee.
    ---
    tags:
      - Employees
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Employee updated.
      404:
        description: Employee not found.
    """

    employee = db.session.get(Employee, id)

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
@admin_required
def delete_employee(id):
    """
    Delete employee.
    ---
    tags:
      - Employees
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Employee deleted.
      404:
        description: Employee not found.
    """

    employee = db.session.get(Employee, id)

    if not employee:
        return {
            "error": "Employee not found."
        }, 404

    db.session.delete(employee)
    db.session.commit()

    return {
        "message": "Employee deleted successfully."
    }, 200