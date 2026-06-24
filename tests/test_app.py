from flask.testing import FlaskClient
import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
    })

    with app.test_client() as client:
        yield client


def test_homepage(client: FlaskClient):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Euro-Wert erfassen" in response.data