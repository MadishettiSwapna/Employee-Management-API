from flask import Flask
from config import Config
from database.database import db
from models.user import User
from routes.auth import auth
from flask_jwt_extended import JWTManager
from routes.employee import employee
from models.employee import Employee
app = Flask(__name__)

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