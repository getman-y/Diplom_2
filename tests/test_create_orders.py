import requests
from data import Urls
from faker_data import FakerData
from methods.courier_methods import UserMethods


class TestCreateOrders:
    def test_create_orders_auth_user_success(self, courier):
        user = UserMethods()
        data = FakerData.generate_correct_data_ingredients()
        token = user.login_user_and_return_token(courier)
        response = requests.post(
            Urls.ORDERS_URL,
            headers={'Authorization': token},
            data={"ingredients": [data.get('id')]}
            )
        assert (response.status_code == 200 and '"success":true' in response.text
                and data.get('name') in response.text)

    def test_create_orders_unauth_user_success(self):
        data = FakerData.generate_correct_data_ingredients()
        response = requests.post(
            Urls.ORDERS_URL,
            data={"ingredients":  [data.get('id')]}
            )
        assert response.status_code == 200 and '"success":true' in response.text

    def test_create_orders_without_ingredients_error(self):
        response = requests.post(
            Urls.ORDERS_URL
        )
        assert response.status_code == 400 and '"Ingredient ids must be provided"' in response.text

    def test_create_orders_with_incorrect_hash_error(self):
        data = FakerData.generate_incorrect_data_ingredients()
        response = requests.post(
            Urls.ORDERS_URL,
            data={"ingredients":data}
        )
        print(response.text)
        assert response.status_code == 500

