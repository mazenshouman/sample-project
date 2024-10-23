import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.post('/calculate', json={'operation': 'add', 'num1': 5, 'num2': 3})
    assert response.status_code == 200
    assert response.get_json() == {'result': 8}

def test_subtract(client):
    response = client.post('/calculate', json={'operation': 'subtract', 'num1': 10, 'num2': 4})
    assert response.status_code == 200
    assert response.get_json() == {'result': 6}

def test_multiply(client):
    response = client.post('/calculate', json={'operation': 'multiply', 'num1': 3, 'num2': 7})
    assert response.status_code == 200
    assert response.get_json() == {'result': 21}

def test_divide(client):
    response = client.post('/calculate', json={'operation': 'divide', 'num1': 20, 'num2': 4})
    assert response.status_code == 200
    assert response.get_json() == {'result': 5}

def test_divide_by_zero(client):
    response = client.post('/calculate', json={'operation': 'divide', 'num1': 5, 'num2': 0})
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Cannot divide by zero'}

def test_invalid_operation(client):
    response = client.post('/calculate', json={'operation': 'modulus', 'num1': 5, 'num2': 3})
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid operation'}