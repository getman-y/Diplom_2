import requests
from data import Urls



class TestLoginCourier:
    # @allure.title('Тест на успешную авторизацию')
    def test_login_courier_success(self, courier):
        response = requests.post(
            Urls.LOGIN_URL,
            courier)
        assert response.status_code == 200 and 'accessToken' in response.text



