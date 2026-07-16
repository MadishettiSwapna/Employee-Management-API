# Employee Management API

A secure Employee Management REST API built with **Flask**, **JWT Authentication**, **Role-Based Access Control (RBAC)**, **SQLite**, and **Docker**. The application allows authenticated users to manage employee records while enforcing role-based permissions.

---

## Features
- User Registration
- User Login
- JWT Authentication
- Password Hashing using bcrypt
- Role-Based Access Control (RBAC)
- Employee CRUD Operations
- SQLAlchemy ORM
- SQLite Database
- Environment Variables using `.env`
- Dockerized Application
- Persistent SQLite Database using Docker Volume Mounting
- RESTful API
- Tested using Postman

---

## Tech Stack

- Python 3
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- bcrypt
- Docker
- Postman
- Git & GitHub

---

## Project Structure

```
Employee-Management-API/
│
├── database/
│   └── database.py
│
├── instance/
│   └── employee.db
│
├── models/
│   ├── employee.py
│   └── user.py
│
├── routes/
│   ├── auth.py
│   └── employee.py
│
├── utils/
│   └── decorators.py
│
├── app.py
├── config.py
├── create_admin.py
├── Dockerfile
├── requirements.txt
├── README.md
├── .dockerignore
├── .gitignore
└── .env
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Employee-Management-API.git

cd Employee-Management-API
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create .env file

```
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
```

---

### 5. Run the application

```bash
python app.py
```

Server runs at

```
http://localhost:5000
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t employee-management-api .
```

## Run Docker Container

```bash
docker run -p 5000:5000 -v "${PWD}/instance:/app/instance" employee-management-api
```

The SQLite database is mounted from the host machine, ensuring data persists even after stopping or recreating the container.

---

# Authentication

## Register

**POST**

```
/register
```

Example

```json
{
    "username":"username",
    "email":"name@gmail.com",
    "password":"pwd"
}
```

---

## Login

**POST**

```
/login
```

Example

```json
{
    "email":"name@gmail.com",
    "password":"name@123"
}
```

Response

```json
{
    "message":"Login Successful",
    "access_token":"JWT_TOKEN"
}
```

---

## Authorization

Include the JWT token in the Authorization header.

```
Authorization:
Bearer <your_access_token>
```

---

# Employee APIs

## Get All Employees

```
GET /employees
```

---

## Get Employee by ID

```
GET /employees/<id>
```

---

## Create Employee

```
POST /employees
```

---

## Update Employee

```
PUT /employees/<id>
```

---

## Delete Employee

```
DELETE /employees/<id>
```

---

# Role-Based Access Control (RBAC)

### Admin

- Create Employee
- Update Employee
- Delete Employee
- View Employees

### User

- View Employees

---

# Database

The project uses SQLite with SQLAlchemy ORM.

Database file:

```
instance/employee.db
```

When running with Docker, the database is persisted using Docker volume mounting.

---

# API Testing

All endpoints were tested successfully using Postman.

---

## Future Improvements

- Develop a responsive frontend using React.js
- Integrate the frontend with the Flask REST API
- Complete Swagger/OpenAPI documentation
- Migrate from SQLite to PostgreSQL or MySQL
- Add Docker Compose for multi-container deployment
- Implement CI/CD using GitHub Actions
- Add Unit and Integration Testing
- Implement API Rate Limiting
- Add Email Verification and Password Reset
- Add Pagination, Search, and Filtering for employee records
- Deploy the application using Render, Railway, or AWS

---

# Author

**Madishetti Swapna**

GitHub: https://github.com/MadishettiSwapna

LinkedIn: https://www.linkedin.com/in/madishettiswapna/
