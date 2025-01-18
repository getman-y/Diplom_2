import requests
from data import Urls
from methods.courier_methods import UserMethods


class TestGetOrders:
    def test_get_orders_auth_user_success(self, courier):
        user = UserMethods()
        token = user.login_user_and_return_token(courier)
        response = requests.get(
            Urls.ORDERS_URL,
            headers={'Authorization': token})
        assert response.status_code == 200 and '"success":true' in response.text

    def test_get_orders_unauth_user_error(self, courier):
        response = requests.get(
            Urls.ORDERS_URL)
        assert response.status_code == 401 and 'You should be authorised' in response.text