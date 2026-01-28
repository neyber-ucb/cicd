from app.database import check_db_connection, get_db


class TestDatabaseConnection:
    """Test database connection functionality"""

    def test_check_db_connection(self):
        """Test that database connection check works"""
        result = check_db_connection()
        assert result is True

    def test_get_db_generator(self):
        """Test that get_db returns a database session"""
        db_gen = get_db()
        db = next(db_gen)

        assert db is not None

        # Clean up
        try:
            next(db_gen)
        except StopIteration:
            pass
