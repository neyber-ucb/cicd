class TestAuthRegistration:
    """Test user registration functionality"""

    def test_register_new_user(self, client, test_user_data):
        """Test successful user registration"""
        response = client.post("/auth/register", json=test_user_data)

        assert response.status_code == 200
        data = response.json()
        assert data["email"] == test_user_data["email"]
        assert "id" in data
        assert "password" not in data

    def test_register_duplicate_user(self, client, test_user_data):
        """Test that registering duplicate user fails"""
        # Register first time
        client.post("/auth/register", json=test_user_data)

        # Try to register again
        response = client.post("/auth/register", json=test_user_data)

        assert response.status_code == 400

    def test_register_invalid_email(self, client):
        """Test registration with invalid email"""
        invalid_data = {"email": "not-an-email", "password": "testpassword123"}
        response = client.post("/auth/register", json=invalid_data)

        assert response.status_code == 422


class TestAuthLogin:
    """Test user login functionality"""

    def test_login_success(self, client, test_user_data):
        """Test successful login"""
        # Register user first
        client.post("/auth/register", json=test_user_data)

        # Login (using username and password only)
        login_data = {
            "username": test_user_data["username"],
            "password": test_user_data["password"],
        }
        response = client.post("/auth/login", json=login_data)

        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    def test_login_wrong_password(self, client, test_user_data):
        """Test login with wrong password"""
        # Register user
        client.post("/auth/register", json=test_user_data)

        # Try login with wrong password
        wrong_data = {
            "username": test_user_data["username"],
            "password": "wrongpassword",
        }
        response = client.post("/auth/login", json=wrong_data)

        assert response.status_code == 401

    def test_login_nonexistent_user(self, client):
        """Test login with non-existent user"""
        response = client.post(
            "/auth/login",
            json={"username": "nonexistent", "password": "somepassword"},
        )

        assert response.status_code == 401


class TestAuthMe:
    """Test current user endpoint"""

    def test_get_current_user(self, authenticated_client, test_user_data):
        """Test getting current user information"""
        response = authenticated_client.get("/auth/me")

        assert response.status_code == 200
        data = response.json()
        assert data["email"] == test_user_data["email"]

    def test_get_current_user_unauthorized(self, client):
        """Test getting current user without authentication"""
        response = client.get("/auth/me")

        assert response.status_code == 401
