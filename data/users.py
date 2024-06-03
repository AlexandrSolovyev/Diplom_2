import allure
from faker import Faker


class Users:
    @staticmethod
    @allure.step('формирую рандомные данные')
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }
        return reg_data

    user_correct = {
        'email': 'alex@ya.ru',
        'password': '123QWEasd'
    }

    user_double = {
        'email': 'alex@ya.ru',
        'password': '123QWEasd',
        'name': 'alex'
    }

    user_without_email = {
        'email': '',
        'password': 'password',
        'name': 'username'
    }

    user_without_password = {
        'email': 'email@ya.ru',
        'password': '',
        'name': 'username'
    }

    user_without_name = {
        'email': 'email@ya.ru',
        'password': 'password',
        'name': ''
    }

    user_fail_email = {
        'email': 'alex@yayayacocodjambo.ru',
        'password': '123QWEasd',
    }

    user_fail_password = {
        'email': 'alex@ya.ru',
        'password': '123QWEasdzxc:)',
    }
