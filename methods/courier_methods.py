import requests
from data import Urls
from faker_data import FakerData

class UserMethods:
    @staticmethod
    def create_user_and_return_data():
        data = FakerData.generate_full_data_account()
        requests.post(
            Urls.CREATE_USER_URL,
            data)
        return {'email': data.get('email'), 'password': data.get('password'), 'name': data.get('name')}

    @staticmethod
    def login_user_and_return_token(data):
        response = requests.post(
            Urls.LOGIN_URL,
            data)
        return response.json()['accessToken']


    @staticmethod
    def delete_user(user_token):
        response = requests.delete(
             Urls.USER_INFO_URL, headers={'Authorization': f'{user_token}'})
