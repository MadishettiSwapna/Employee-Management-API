from flask import Flask
from config import Config
from database.database import db
from models.user import User
from routes.auth import auth
app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(auth)

@app.route("/")
def home():
    return "Welcome to Employee Management API!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)