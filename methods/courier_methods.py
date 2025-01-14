import requests
from data import Urls
from faker_data import FakerData

class CourierMethods:
    @staticmethod
    def create_courier_and_return_data():
        data = FakerData.generate_full_data_account()
        requests.post(
            Urls.CREATE_URL,
            data)
        return {'email': data.get('email'), 'password': data.get('password')}

    @staticmethod
    def login_courier_and_return_token(data):
        response = requests.post(
            Urls.LOGIN_URL,
            data)
        return response.json()['accessToken']


    @staticmethod
    def delete_courier(courier_token):
        response = requests.delete(
             Urls.DELETE_URL, headers={'Authorization': f'{courier_token}'})
        assert response.status_code == 202 and 'User successfully removed' in response.text
