import pytest

@pytest.fixture(scope='session')
def db():
    # Setup database connection
    yield db_connection
    # Teardown database connection