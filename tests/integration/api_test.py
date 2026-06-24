from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post('/api/users', json={'email': 'test@example.com', 'password': 'password'})
    assert response.status_code == 200
    assert response.json()['email'] == 'test@example.com'


def test_get_user():
    response = client.get('/api/users/1')
    assert response.status_code == 200