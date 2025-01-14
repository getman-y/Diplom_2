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
