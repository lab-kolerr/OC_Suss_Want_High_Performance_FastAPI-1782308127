import pytest

@pytest.fixture(scope='session')
def db():
    # Setup database connection
    yield db_connection
    # Teardown database connection

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from app.main import app
    return TestClient(app)