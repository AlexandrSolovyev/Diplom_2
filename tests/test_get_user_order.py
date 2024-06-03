import allure
import requests

from data.endpoint import Endpoint
from data.ingredient import Ingredient
from conftest import create_user


@allure.suite("Получение заказов")
class TestGetUserOrder:

    @allure.title("Получение доступных заказов авторизованного пользователя")
    def test_get_order_user_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        requests_create_order = requests.post(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_MAKE_GET_ORDER}", headers=token,
                                              data=Ingredient.correct_ingredients_data)
        response_get_order = requests.get(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_MAKE_GET_ORDER}", headers=token)
        assert (response_get_order.status_code == 200 and
                response_get_order.json()['orders'][0]['number'] == requests_create_order.json()['order']['number'])

    @allure.title("Получение заказов пользователя если пользователь не авторизовался")
    def test_get_order_user_not_auth(self):
        r = requests.get(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_MAKE_GET_ORDER}")
        assert r.status_code == 401 and r.json()['message'] == "You should be authorised"
