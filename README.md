# Diplom_2
Протестированы "ручки" API https://stellarburgers.nomoreparties.site/
Структура диплома:

1. Основа для написания автотестов — фреймворк pytest, requests.
2. Для отчетов используется Allure
3. Автотесты написаны в соответствии паттерна POM
4. Установить зависимости — `pip install -r requirements.txt`
5. Команда для запуска — `pytest -v`
6. Команда для запуска с записью отчета в allure_results: `pytest --alluredir=allure_results`
7. Генерация отчета в html страницу (находясь в дирректории allure_results): _`allure serve allure_results`_ 

### Директория проекта:

* `allure_results` - сожержит отчеты alure
 *  `data` - дирректория данных
 * * `endpoint.py` - "ручки" API 
 * * `headers.py` - файл с headers
 * * `ingredient.py` - файл с данными ингредиентов
 * * `users.py` - файл с данными пользователей
 * `tests` - дирректория тестов
 * * `test_changing_user_data.py` - тесты изменения данных пользователей
 * * `test_create_order.py` - тесты создания заказов
 * * `test_create_user.py` - тесты создания пользователей
 * * `test_login.py` - тесты авторизации
 * `conftest.py` -  фикстуры
 * `README.md` - описание проекта
 * `requirements` - файл с внешними зависимостями
