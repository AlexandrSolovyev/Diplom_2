import pytest
import requests
from data.endpoint import Endpoint
from helpers import create_data_user


@pytest.fixture(scope="function")
def generate_data():
    payload = create_data_user()
    yield payload


@pytest.fixture(scope="function")
def register_user(generate_data):
    payload = generate_data
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_USER_CREATE}", data=payload)
    token = response.json()["accessToken"]
    return response, payload, login_data, token


@pytest.fixture(scope="function")
def delete_user(register_user):
    response, payload, login_data, token = register_user
    requests.delete(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_DELETE_USER}", headers={'Authorization': f'{token}'})
    yield response, payload, login_data, token
