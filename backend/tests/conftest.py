import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.models.task import Task  # noqa: F401

# Import models to ensure they're registered with Base
from app.models.user import User  # noqa: F401
from main import app


@pytest.fixture(scope="function")
def test_db():
    """Create a test database session with fresh tables for each test"""
    # Use in-memory SQLite for tests
    test_database_url = "sqlite:///:memory:"

    engine = create_engine(test_database_url, connect_args={"check_same_thread": False})

    # Create all tables
    Base.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()


@pytest.fixture(scope="function")
def client(test_db):
    """Create a test client with database override"""

    def override_get_db():
        try:
            yield test_db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def test_user_data():
    """Sample user data for testing"""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123",
    }


@pytest.fixture
def authenticated_client(client, test_user_data):
    """Create an authenticated test client"""
    # Register user
    client.post("/auth/register", json=test_user_data)

    # Login to get token (using username and password only)
    login_data = {
        "username": test_user_data["username"],
        "password": test_user_data["password"],
    }
    response = client.post("/auth/login", json=login_data)
    token = response.json()["access_token"]

    # Add token to client headers
    client.headers.update({"Authorization": f"Bearer {token}"})

    return client
