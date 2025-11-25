import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Inventario de Servidores" in rv.data
    assert b"Servidor Dell PowerEdge" in rv.data

def test_item_count(client):
    rv = client.get('/')
    assert b"Mostrando 3 \xc3\xadtems" in rv.data
    assert b"Rack B" in rv.data
