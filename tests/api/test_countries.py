from application.factory import create_app
import pytest
from ..context import application


@pytest.fixture
def client():
    return create_app().test_client()


def test_countries_route(client):
    response = client.get('/moon/')
    # assert response.get_json() == {}