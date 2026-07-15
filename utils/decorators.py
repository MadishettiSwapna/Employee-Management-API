from functools import wraps

from flask_jwt_extended import get_jwt_identity

from models.user import User


def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        current_email = get_jwt_identity()

        user = User.query.filter_by(email=current_email).first()

        if not user:
            return {
                "error": "User not found."
            },404

        if user.role != "admin":
            return {
                "error":"Access denied. Admins only."
            },403

        return func(*args, **kwargs)

    return wrapper