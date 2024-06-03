import allure
import pytest
import requests
from data.endpoint import Endpoint
from data.users import Users


@allure.suite("Авторизация")
class TestLogIn:
    @allure.title('LogIn под существующим пользователем')
    def test_login_correct(self):
        response = requests.post(f'{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_LOGIN}',
                                 data=Users.user_correct)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('LogIn с неверным логином и паролем')
    @pytest.mark.parametrize('user_data',
                             [Users.user_fail_email, Users.user_fail_password])
    def test_login_fail(self, user_data):
        response = requests.post(f'{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_LOGIN}',
                                 data=user_data)
        assert response.status_code == 401 and 'email or password are incorrect' in response.text
