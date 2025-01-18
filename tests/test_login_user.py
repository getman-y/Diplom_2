import requests
from data import Urls
from faker_data import FakerData


class TestLoginUser:
    # @allure.title('Тест на успешную авторизацию')
    def test_login_user_success(self, courier):
        response = requests.post(
            Urls.LOGIN_URL,
            courier)
        assert response.status_code == 200 and 'accessToken' in response.text

    def test_login_user_with_incorrect_data_error(self, courier):
        data = FakerData.generate_full_data_account()
        response = requests.post(Urls.LOGIN_URL, data= {data.get('email'), data.get('password') })
        assert response.status_code == 401 and 'email or password are incorrect' in response.text