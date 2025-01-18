import requests
from faker import Faker

from data import Urls


class FakerData:
    @staticmethod
    def generate_full_data_account():
        faker_data = Faker()
        email = faker_data.email()
        password = faker_data.password()
        first_name = faker_data.name()
        data = {
            "email": email,
            "password": password,
            "name": first_name
        }
        return data

    @staticmethod
    def generate_correct_data_ingredients():
        response = requests.get(
            Urls.INGREDIENTS_URL)
        id = response.json()['data'][0]['_id']
        name = response.json()['data'][0]['name']
        data = {
            "id": id,
            "name": name
        }
        return data

    @staticmethod
    def generate_incorrect_data_ingredients():
        response = requests.get(
            Urls.INGREDIENTS_URL)
        id = f'{response.json()['data'][0]['_id']}test'
        return id

