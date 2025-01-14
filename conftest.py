import pytest

from methods.courier_methods import CourierMethods


@pytest.fixture()
def courier():
    couriers = CourierMethods()
    data = couriers.create_courier_and_return_data()
    yield data
    courier_token = couriers.login_courier_and_return_token(data)
    couriers.delete_courier(courier_token)