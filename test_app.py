import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # Test the root endpoint
    response = client.get('/')
    assert response.status_code == 200

def test_existing_endpoint(client):
    # Replace '/some-existing-route' with an actual route from your app
    response = client.get('/')
    assert response.status_code in [200, 302]  # 302 for redirects
