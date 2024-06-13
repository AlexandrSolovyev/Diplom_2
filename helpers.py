from faker import Faker
import allure


@allure.step('формирую рандомные данные')
def create_data_user():
    fake = Faker()

    reg_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }
    return reg_data
