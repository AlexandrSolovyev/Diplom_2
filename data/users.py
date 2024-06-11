

class Users:

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
