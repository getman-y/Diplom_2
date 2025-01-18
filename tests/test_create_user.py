import requests
from data import Urls
from faker_data import FakerData

class TestCreateUser:
    def test_create_user_success(self):
        data = FakerData.generate_full_data_account()
        response = requests.post(
            Urls.CREATE_USER_URL,
            data)
        assert response.status_code == 200 and 'accessToken' in response.text

    def test_create_two_user_with_same_login_error(self, courier):
        response = requests.post(
            Urls.CREATE_USER_URL,
            courier)
        assert response.status_code == 403 and 'User already exists' in response.text

    def test_create_user_without_required_field_error(self, courier):
        data = FakerData.generate_full_data_account()
        response = requests.post(
            Urls.CREATE_USER_URL,
            data= {data.get('email'), data.get('password') })
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text



