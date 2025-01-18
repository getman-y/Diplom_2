import pytest

from methods.courier_methods import UserMethods


@pytest.fixture()
def courier():
    couriers = UserMethods()
    data = couriers.create_user_and_return_data()
    yield data
    user_token = couriers.login_user_and_return_token(data)
    couriers.delete_user(user_token)