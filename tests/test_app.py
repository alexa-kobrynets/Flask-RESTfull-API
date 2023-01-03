import pytest
from app import create_app
from flask import current_app


@pytest.fixture()
def app():
    app = create_app('testing')
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_app_exists():
    assert current_app is not None


def test_request_example(client):
    response = client.get("/report/")
    assert b"Name" in response.data


def test_request_drivers(client):
    response = client.get("/report/drivers/")
    assert b"Sergio" in response.data


def test_non_existent_index(client):
    response = client.get("/test/")
    assert response.status_code == 404


def test_report(client):
    response = client.get('/report/')
    assert response.status_code == 200


def test_param_driver(client):
    response = client.get('/report/drivers/?driver=KRF')
    assert response.status_code == 200
    assert b"Kimi" in response.data


def test_param_order(client):
    response = client.get('/report/?order=desc')
    assert response.status_code == 200
    assert b"desc" in response.data
