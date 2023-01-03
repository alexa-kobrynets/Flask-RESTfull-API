import pytest
from app import create_app


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


def test_report(client):
    response = client.get('/api/v1/report/')
    assert response.status_code == 200
    assert b'[[1,"Sebastian Vettel","FERRARI","0:01:04.415000"]' in response.data


def test_report_drivers(client):
    response = client.get('/api/v1/report/drivers/')
    assert response.status_code == 200
    assert b"SVF" in response.data


def test_report_drivers_svf(client):
    response = client.get('/api/v1/report/drivers/?driver=SVF')
    assert response.status_code == 200
    assert b"Sebastian Vettel" in response.data


def test_report_drivers_json_asc(client):
    response = client.get('/api/v1/report/?order=asc&format=json')
    assert response.status_code == 200
    print(response.data)
    assert response.headers["Content-Type"] == "application/json"
    assert b'[[1,"Sebastian Vettel","FERRARI","0:01:04.415000"]' in response.data


def test_report_drivers_json_desc(client):
    response = client.get('/api/v1/report/?order=desc&format=json')
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert b'[[1,"Lewis Hamilton","MERCEDES","0:07:12.460000"]' in response.data


def test_report_drivers_xml_asc(client):
    response = client.get('/api/v1/report/?order=asc&format=xml')
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml; charset=utf-8"
    assert b'0:01:12.657000</time><place>5' in response.data


def test_report_drivers_xml_desc(client):
    response = client.get('/api/v1/report/?order=desc&format=xml')
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml; charset=utf-8"
    assert b'<time>0:01:13.393000</time><place>5' in response.data
