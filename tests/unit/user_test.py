import pytest
from app.models import User

@pytest.fixture
def user():
    return User(email='test@example.com', hashed_password='hashed_password')


def test_user_creation(user):
    assert user.email == 'test@example.com'
    assert user.hashed_password == 'hashed_password'


def test_user_email_uniqueness():
    user1 = User(email='unique@example.com', hashed_password='pass1')
    user2 = User(email='unique@example.com', hashed_password='pass2')
    assert user1.email == user2.email