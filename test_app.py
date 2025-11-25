import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_json(client):
    rv = client.get('/')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['service'] == "Inventory-API"
    assert json_data['status'] == "running"

def test_get_all_items(client):
    rv = client.get('/api/items')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['count'] == 3

def test_get_item_found(client):
    rv = client.get('/api/items/1')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['name'] == "Servidor Dell PowerEdge"

def test_get_item_not_found(client):
    rv = client.get('/api/items/999')
    assert rv.status_code == 404
    json_data = rv.get_json()
    assert "error" in json_data