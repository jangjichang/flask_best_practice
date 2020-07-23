import pytest
import random
from .app import app


@pytest.fixture
def test_client():
    return app.test_client()

@pytest.fixture
def random_int():
    return random.randint(1, 10)

def test_get_movies(test_client):
    response = test_client.get('/movies')
    assert response.status_code == 200
    assert '{"data": "movies"}' == response.data.decode()

def test_post_movies(test_client):
    response = test_client.post('/movies')
    assert response.status_code == 201
    assert '{"message": "created"}' == response.data.decode()

def test_put_movie(test_client, random_int):
    response = test_client.put(f'/movies/{random_int}')
    assert response.status_code == 200
    assert f'{{"message": "put {random_int}"}}' == response.data.decode()

def test_delete_movie(test_client, random_int):
    response = test_client.delete(f'/movies/{random_int}')
    assert response.status_code == 200
    assert f'{{"message": "deleted {random_int}"}}' == response.data.decode()

def test_get_movie(test_client, random_int):
    response = test_client.get(f'/movies/{random_int}')
    assert response.status_code == 200
    assert f'{{"data": "movie number {random_int}"}}' == response.data.decode()

    
