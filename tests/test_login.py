import allure
import pytest
import requests
from data.endpoint import Endpoint
from data.users import Users
from conftest import register_user


@allure.suite("Авторизация")
class TestLogIn:

    @allure.title("LogIn под существующим пользователем")
    def test_login_correct(self, register_user):
        response_register, payload, login_data, token = register_user
        assert response_register.status_code == 200 and response_register.json()["success"] is True
        response_login = requests.post(f'{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_LOGIN}', data=login_data)
        assert response_login.status_code == 200 and response_login.json()["success"] is True

    @allure.title('LogIn с неверным логином и паролем')
    @pytest.mark.parametrize('user_data',
                             [Users.user_fail_email, Users.user_fail_password])
    def test_login_fail(self, user_data):
        response = requests.post(f'{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_LOGIN}',
                                 data=user_data)
        assert response.status_code == 401 and 'email or password are incorrect' in response.text
