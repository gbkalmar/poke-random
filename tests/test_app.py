import pytest
import json
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_random_pokemon(client):
    response = client.get('/pokemon')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'name' in data
    assert 'abilities' in data
    assert isinstance(data['abilities'], list)
