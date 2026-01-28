def test_health_endpoint_returns_healthy(client):
    """Test that health endpoint returns healthy status with DB connection"""
    response = client.get("/api/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["database"] == "connected"


def test_root_endpoint(client):
    """Test that root endpoint returns welcome message"""
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "docs" in data
