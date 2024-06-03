import pytest
import requests

from data.endpoint import Endpoint
from data.users import Users


@pytest.fixture(scope="function")
def create_user():
    payload = Users.create_data_user()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_USER_CREATE}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_DELETE_USER}", headers={'Authorization': f'{token}'})
