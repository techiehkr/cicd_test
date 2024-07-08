import pytest
from app import app

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client

def test_hello(client):
	rv = client.get('/')
	assert b'hello' in rv.data 
def test_tel(client):
	rv = client.get('/')
	assert b'hel' in rv.data
