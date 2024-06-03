import string
import random

import allure


@allure.step('Формирование тела запроса для создания пользователя')
def get_data_for_create_user(login=None):
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(6) + "@ya.ru"
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }
    return payload
