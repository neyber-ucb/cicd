# ToDo List API

A complete ToDo list backend application with JWT authentication built with FastAPI, SQLAlchemy, and Python.

## Features

- ✅ User registration and authentication with JWT tokens
- ✅ Secure password hashing with bcrypt
- ✅ CRUD operations for tasks (Create, Read, Update, Delete)
- ✅ User-specific task management
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Automatic API documentation (Swagger UI & ReDoc)
- ✅ CORS middleware enabled

## Prerequisites

- Python 3.12+
- uv package manager

## Setup

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure environment (optional)

Copy the example environment file and customize if needed:

```bash
cp .env.example .env
```

Edit `.env` to set your own `SECRET_KEY` (generate one with `openssl rand -hex 32`).

### 3. Run the application

```bash
uv run uvicorn main:app --reload
```

Or run directly:

```bash
uv run python main.py
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive API docs (Swagger)**: http://localhost:8000/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/redoc

## API Endpoints

### Authentication

- **POST** `/auth/register` - Register a new user
  - Body: `{"username": "string", "email": "user@example.com", "password": "string"}`
  
- **POST** `/auth/login` - Login and get JWT token
  - Form data: `username` and `password`
  - Returns: `{"access_token": "...", "token_type": "bearer"}`
  
- **GET** `/auth/me` - Get current user info (requires authentication)

### Tasks

All task endpoints require authentication (Bearer token in Authorization header).

- **POST** `/tasks/` - Create a new task
  - Body: `{"title": "string", "description": "string", "completed": false}`
  
- **GET** `/tasks/` - Get all tasks for current user
  - Query params: `skip` (default: 0), `limit` (default: 100)
  
- **GET** `/tasks/{task_id}` - Get a specific task
  
- **PUT** `/tasks/{task_id}` - Update a task
  - Body: `{"title": "string", "description": "string", "completed": true}`
  
- **DELETE** `/tasks/{task_id}` - Delete a task

### General

- **GET** `/` - Welcome message
- **GET** `/health` - Health check endpoint

## Usage Example

### 1. Register a new user

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "email": "john@example.com", "password": "secret123"}'
```

### 2. Login to get access token

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john&password=secret123"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Create a task (using the token)

```bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread", "completed": false}'
```

### 4. Get all tasks

```bash
curl -X GET "http://localhost:8000/tasks/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── config.py              # Application configuration
│   ├── database.py            # Database setup and session management
│   ├── auth/
│   │   ├── __init__.py
│   │   └── security.py        # JWT and password utilities
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py            # User database model
│   │   └── task.py            # Task database model
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py            # Authentication endpoints
│   │   └── tasks.py           # Task CRUD endpoints
│   └── schemas/
│       ├── __init__.py
│       ├── user.py            # User Pydantic schemas
│       └── task.py            # Task Pydantic schemas
├── main.py                    # FastAPI application entry point
├── pyproject.toml             # Project dependencies and metadata
├── .env.example               # Example environment variables
├── .python-version            # Python version specification
└── README.md                  # This file
```

## Database

The application uses SQLite by default (`todo.db`). The database is automatically created when you first run the application.

To use a different database, update the `DATABASE_URL` in your `.env` file.

## Security Notes

- Change the `SECRET_KEY` in production (use `openssl rand -hex 32` to generate)
- JWT tokens expire after 30 minutes by default
- Passwords are hashed using bcrypt
- CORS is enabled for all origins (restrict in production)

## Development

### Adding Dependencies

```bash
uv add <package-name>
```

### Interactive API Documentation

FastAPI automatically generates interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

You can test all endpoints directly from the Swagger UI interface.
