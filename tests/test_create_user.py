import allure
import pytest
import requests
from data.endpoint import Endpoint
from helpers import create_data_user
from data.users import Users


@allure.suite("Регистрация")
class TestCreateUser:
    @allure.title('Создание уникального пользователя.')
    def test_create_user(self):
        response = requests.post(f'{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_USER_CREATE}',
                                 data=create_data_user())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('создать пользователя, который уже зарегистрирован.')
    def test_create_double_user(self):
        response = requests.post(f'{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_USER_CREATE}',
                                 data=Users.user_double)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.title('создать пользователя и не заполнить одно из обязательных полей')
    @pytest.mark.parametrize('user_data',
                             [Users.user_without_email, Users.user_without_password,
                              Users.user_without_name])
    def test_create_fail_user(self, user_data):
        response = requests.post(f'{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_USER_CREATE}',
                                 data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text
