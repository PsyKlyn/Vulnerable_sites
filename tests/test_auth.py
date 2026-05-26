import pytest
from src.app import app

def test_login():
    response = app.test_client().post('/login',
        json={'username': 'admin', 'password': 'test123'})
    assert response.status_code == 200
