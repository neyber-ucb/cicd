class TestTaskCreation:
    """Test task creation functionality"""

    def test_create_task(self, authenticated_client):
        """Test creating a new task"""
        task_data = {"title": "Test Task", "description": "Test Description"}
        response = authenticated_client.post("/tasks/", json=task_data)

        assert response.status_code == 200
        data = response.json()
        assert data["title"] == task_data["title"]
        assert data["description"] == task_data["description"]
        assert data["completed"] is False
        assert "id" in data

    def test_create_task_unauthorized(self, client):
        """Test creating task without authentication"""
        task_data = {"title": "Test Task", "description": "Test Description"}
        response = client.post("/tasks/", json=task_data)

        assert response.status_code == 401


class TestTaskRetrieval:
    """Test task retrieval functionality"""

    def test_get_all_tasks(self, authenticated_client):
        """Test getting all tasks for authenticated user"""
        # Create some tasks
        authenticated_client.post(
            "/tasks/", json={"title": "Task 1", "description": "Description 1"}
        )
        authenticated_client.post(
            "/tasks/", json={"title": "Task 2", "description": "Description 2"}
        )

        # Get all tasks
        response = authenticated_client.get("/tasks/")

        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2

    def test_get_task_by_id(self, authenticated_client):
        """Test getting a specific task by ID"""
        # Create a task
        create_response = authenticated_client.post(
            "/tasks/", json={"title": "Test Task", "description": "Test Description"}
        )
        task_id = create_response.json()["id"]

        # Get the task
        response = authenticated_client.get(f"/tasks/{task_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
        assert data["title"] == "Test Task"

    def test_get_nonexistent_task(self, authenticated_client):
        """Test getting a task that doesn't exist"""
        response = authenticated_client.get("/tasks/99999")

        assert response.status_code == 404


class TestTaskUpdate:
    """Test task update functionality"""

    def test_update_task(self, authenticated_client):
        """Test updating a task"""
        # Create a task
        create_response = authenticated_client.post(
            "/tasks/",
            json={"title": "Original Title", "description": "Original Description"},
        )
        task_id = create_response.json()["id"]

        # Update the task
        update_data = {
            "title": "Updated Title",
            "description": "Updated Description",
            "completed": True,
        }
        response = authenticated_client.put(f"/tasks/{task_id}", json=update_data)

        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["description"] == "Updated Description"
        assert data["completed"] is True

    def test_update_nonexistent_task(self, authenticated_client):
        """Test updating a task that doesn't exist"""
        update_data = {"title": "Updated Title", "description": "Updated Description"}
        response = authenticated_client.put("/tasks/99999", json=update_data)

        assert response.status_code == 404


class TestTaskDeletion:
    """Test task deletion functionality"""

    def test_delete_task(self, authenticated_client):
        """Test deleting a task"""
        # Create a task
        create_response = authenticated_client.post(
            "/tasks/",
            json={"title": "Task to Delete", "description": "This will be deleted"},
        )
        task_id = create_response.json()["id"]

        # Delete the task
        response = authenticated_client.delete(f"/tasks/{task_id}")

        assert response.status_code == 200

        # Verify task is deleted
        get_response = authenticated_client.get(f"/tasks/{task_id}")
        assert get_response.status_code == 404

    def test_delete_nonexistent_task(self, authenticated_client):
        """Test deleting a task that doesn't exist"""
        response = authenticated_client.delete("/tasks/99999")

        assert response.status_code == 404
