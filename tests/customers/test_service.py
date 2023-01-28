import unittest

from src.api.customers.service import create_customer
from src.interfaces.db_interface import DataObject
from src.api.customers.schemas import CustomerCreateData


class DataInterfaceStub:
    def create(self, customer_data) -> DataObject:
        raise NotImplementedError()


class CustomerInterface(DataInterfaceStub):
    def create(self, customer_data: DataObject) -> DataObject:
        new_customer = dict(customer_data)
        new_customer["id"] = 1
        print(new_customer)
        return new_customer


class TestCustomer(unittest.TestCase):
    def test_create_customer(self):
        customer_data = create_customer(
            CustomerCreateData(
                id=1,
                first_name='Michal',
                last_name='Michal',
                email_address='Michal',
                phone_number=100,
                street='test',
                city='test',
                post_code=100,
                want_email=True
            ),
            customer_interface=CustomerInterface(),
        )
        self.assertEqual(customer_data["post_code"], 100)