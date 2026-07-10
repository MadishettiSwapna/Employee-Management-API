from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from models.user import User
import bcrypt
from database.database import db
auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])

def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Validation
    if not username or not email or not password:
        return {
            "error": "All fields are required."
        }, 400

    # Duplicate email check
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return {
            "error": "Email already registered."
        }, 409

    # Hash password
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    # Create user
    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    # Save user
    db.session.add(new_user)
    db.session.commit()

    return {
        "message": "User registered successfully."
    }, 201

@auth.route("/login", methods=["POST"])

def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {
            "error": "Email and Password are required."
        }, 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return {
            "error": "User not found."
        }, 404

    if not bcrypt.checkpw(
        password.encode("utf-8"),
        user.password.encode("utf-8")
    ):
        return {
            "error": "Invalid password."
        }, 401

    access_token = create_access_token(identity=user.email)

    return {
        "message": "Login Successful",
        "access_token": access_token
    }, 200