import allure
import requests

from data import Urls
from faker_data import FakerData
from methods.courier_methods import UserMethods

@allure.suite('Изменение данных пользователя')
class TestUpdateUser:

    @allure.title('Тест на изменение данных авторизованного пользователя')
    def test_update_user_success(self):
        user = UserMethods()
        data = FakerData.generate_full_data_account()
        courier_login = user.create_user_and_return_data()
        token = user.login_user_and_return_token(courier_login)
        response = requests.patch(
            Urls.USER_INFO_URL,
            headers={'Authorization': token},
            data={"name": data.get('name'),"email": data.get('email')}
            )
        assert (response.status_code == 200 and data.get('name') in response.text
                and data.get('email') in response.text)

    @allure.title('Тест на изменение данных неавторизованного пользователя')
    def test_update_unauth_user_error(self):
        data = FakerData.generate_full_data_account()
        response = requests.patch(
            Urls.USER_INFO_URL,
            data={"name": data.get('name'),"email": data.get('email')}
            )
        assert (response.status_code == 401 and 'You should be authorised' in response.text)

