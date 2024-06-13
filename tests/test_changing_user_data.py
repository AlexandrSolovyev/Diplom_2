import allure
import requests

from data.endpoint import Endpoint
from helpers import create_data_user
from conftest import register_user


@allure.suite("Изменение данных пользователя")
class TestChangingUserData:
    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_changing_user_email_with_auth(self, register_user):
        payload = {'email': create_data_user()["email"]}
        token = {'Authorization': register_user[3]}
        r = requests.patch(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == payload["email"]

    @allure.title("Успешное изменение password авторизованного пользователя")
    def test_changing_user_password_with_auth(self, register_user):
        payload = {'password': create_data_user()["password"]}
        token = {'Authorization': register_user[3]}
        r = requests.patch(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Успешное изменение name авторизованного пользователя")
    def test_changing_user_name_with_auth(self, register_user):
        payload = {'name': create_data_user()["name"]}
        token = {'Authorization': register_user[3]}
        r = requests.patch(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['name'] == payload["name"]

    @allure.title("Изменение данных пользователя без авторизацией")
    def test_changing_user_data_not_auth(self):
        r = requests.patch(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_CHANGE_USER_DATA}", data=create_data_user())
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'
