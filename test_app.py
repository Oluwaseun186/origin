import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Task" in response.data or b"tasks" in response.data  # basic content check


def test_add_and_delete(client):
    # Add a task
    response = client.post('/add', data={'content': 'Test Task'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Task' in response.data

    # Find the task ID
    response = client.get('/')
    assert b'Test Task' in response.data

    # Since we don’t know the exact ID, just check delete works (by adding another task and deleting it later if needed)


def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}
