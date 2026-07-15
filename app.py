from flask import Flask
from config import Config
from database.database import db
from models.user import User
from routes.auth import auth
from flask_jwt_extended import JWTManager
from routes.employee import employee
from models.employee import Employee
from flasgger import Swagger

app = Flask(__name__)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

template = {
    "swagger": "2.0",
    "info": {
        "title": "Employee Management API",
        "description": "Employee Management System using Flask, JWT and SQLite",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Enter: Bearer <JWT Token>"
        }
    }
}

Swagger(app, config=swagger_config, template=template)

app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)
app.register_blueprint(auth)
app.register_blueprint(employee)

@app.route("/")
def home():
    return "Welcome to Employee Management API!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)