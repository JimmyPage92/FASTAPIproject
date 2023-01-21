from src.interfaces.db_interface import DataObject, DBInterface
from .schemas import CustomerCreateData, CustomerUpdateData


def read_all_customers(customer_interface: DBInterface) -> list[DataObject]:
    return customer_interface.read_all()


def read_customer(customer_id: int, customer_interface: DBInterface) -> DataObject:
    return customer_interface.read_by_id(customer_id)


def create_customer(new_customer: CustomerCreateData, customer_interface: DBInterface) -> DataObject:
    return customer_interface.create(new_customer.dict())


def update_customer(customer_id: int, customer_to_update: CustomerUpdateData, customer_interface: DBInterface) -> DataObject:
    return customer_interface.update(customer_id, customer_to_update)


def delete_customer(customer_id: int, customer_interface: DBInterface) -> DataObject:
    return customer_interface.delete(customer_id)
