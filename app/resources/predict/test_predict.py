import pytest
import falcon
import json
from app.app import api
from falcon import testing


@pytest.fixture(scope="module")
def client():
    return testing.TestClient(api)


def test_predict_good_request(client):
    """Expected behavior, integer request with 200 OK response."""
    request = {"request": 5}
    response = client.simulate_post("/predict", body=json.dumps(request))
    assert response.status == falcon.HTTP_200


def test_predict_bad_request(client):
    """Expected behavior, non-integer request with 400 Bad Request response."""
    request = {"request": "not an integer"}
    response = client.simulate_post("/predict", body=json.dumps(request))
    assert response.status == falcon.falcon.HTTP_400
