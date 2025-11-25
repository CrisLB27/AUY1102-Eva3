import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Prueba que la página carga y muestra el inventario"""
    rv = client.get('/')
    
    # 1. Verificar que la página responde bien (Código 200)
    assert rv.status_code == 200
    
    # 2. Verificar el título NUEVO de la versión simple
    # Nota: b"" indica que buscamos bytes, necesario en Flask testing
    assert b"Inventario de Equipos TI" in rv.data
    
    # 3. Verificar que aparezcan datos del inventario
    assert b"Servidor Dell PowerEdge" in rv.data
    assert b"Switch Cisco Catalyst" in rv.data
