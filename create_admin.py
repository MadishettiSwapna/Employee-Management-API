from app import app
from models.user import User
from database.database import db

email = input("Enter user email: ")

with app.app_context():

    user = User.query.filter_by(email=email).first()

    if not user:
        print("User not found.")

    else:
        user.role = "admin"
        db.session.commit()
        print(f"{email} is now an admin.")