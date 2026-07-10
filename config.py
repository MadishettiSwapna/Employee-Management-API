class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///employee.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your-secret-key"
    JWT_SECRET_KEY = "swapna-secret-key"