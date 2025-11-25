import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_content(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Inventario de Infraestructura" in rv.data

def test_navigation(client):
    rv = client.get('/')
    # Verificamos que existan los botones del menú
    assert b"Nuevo Equipo" in rv.data
    assert b"Acerca de" in rv.data

def test_add_page(client):
    rv = client.get('/add')
    assert rv.status_code == 200
    assert b"Registrar Nuevo Equipo" in rv.data