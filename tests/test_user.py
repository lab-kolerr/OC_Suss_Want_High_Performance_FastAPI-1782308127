import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_user():
    response = await client.post('/api/users', json={'email': 'test@example.com', 'password': 'strongpassword'})
    assert response.status_code == 200
    assert response.json()['email'] == 'test@example.com'

@pytest.mark.asyncio
async def test_create_user_invalid_password():
    response = await client.post('/api/users', json={'email': 'test@example.com', 'password': 'short'})
    assert response.status_code == 400
    assert response.json()['detail'] == 'User creation failed'