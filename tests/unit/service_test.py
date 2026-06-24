import pytest
from app.services import UserService

@pytest.fixture
def user_service():
    return UserService()


def test_create_user(user_service):
    user = user_service.create_user(email='test@example.com', password='password')
    assert user.email == 'test@example.com'


def test_user_service_logic(user_service):
    assert user_service.some_logic() == expected_value