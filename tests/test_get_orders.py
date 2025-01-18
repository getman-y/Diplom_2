import allure
import requests
from data import Urls
from methods.courier_methods import UserMethods


@allure.suite('Получение заказов')
class TestGetOrders:

    @allure.title('Тест на получение заказов авторизованного пользователя')
    def test_get_orders_auth_user_success(self, courier):
        user = UserMethods()
        token = user.login_user_and_return_token(courier)
        response = requests.get(
            Urls.ORDERS_URL,
            headers={'Authorization': token})
        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Тест на получение заказов неавторизованного пользователя')
    def test_get_orders_unauth_user_error(self, courier):
        response = requests.get(
            Urls.ORDERS_URL)
        assert response.status_code == 401 and 'You should be authorised' in response.text