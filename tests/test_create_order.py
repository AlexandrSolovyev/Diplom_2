import allure
import requests

from conftest import register_user
from data.endpoint import Endpoint
from data.ingredient import Ingredient
from data.headers import Headers


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, register_user):
        token = {'Authorization': register_user[3]}
        r = requests.post(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_MAKE_GET_ORDER}",
                          headers=token,
                          data=Ingredient.correct_ingredients_data)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Создание заказа не авторизованным пользователем")
    def test_create_order_not_auth(self):
        r = requests.post(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_MAKE_GET_ORDER}",
                          data=Ingredient.correct_ingredients_data)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_with_ingredient(self):
        r = requests.post(f"{Endpoint.MAIN_URL}{Endpoint.ENDPOINT_MAKE_GET_ORDER}")
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"

    @allure.title("Создание с невалидным хешем ингредиента")
    def test_create_order_invalid_hash_ingredient(self):
        response = requests.post(Endpoint.MAIN_URL + Endpoint.ENDPOINT_MAKE_GET_ORDER,
                                 headers=Headers.headers_make_order,
                                 json=Ingredient.incorrect_ingredients_data)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
