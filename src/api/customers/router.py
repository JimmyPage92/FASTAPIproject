from fastapi import APIRouter

from src.database import DBSession
from .models import DBCustomers
from .schemas import CustomerCreateData, CustomerUpdateData
from src.interfaces.db_interface import DataObject, DBInterface
from .service import read_all_customers, read_customer, create_customer, update_customer, delete_customer


router: APIRouter = APIRouter()


@router.get("/customers")
def api_read_all_customers() -> list[DataObject]:
    return read_all_customers(DBInterface(DBSession(), DBCustomers))


@router.get("/customer/{customer_id}")
def api_read_customer(customer_id: int) -> DataObject:
    return read_customer(customer_id, DBInterface(DBSession(), DBCustomers))


@router.post("/create_customer")
def api_create_customer(new_customer: CustomerCreateData) -> DataObject:
    return create_customer(new_customer, DBInterface(DBSession(), DBCustomers))


@router.put("/update_customer/{customer_id}")
def api_update_customer(customer_id: int, data_to_update: CustomerUpdateData) -> DataObject:
    return update_customer(customer_id, data_to_update, DBInterface(DBSession(), DBCustomers))


@router.delete("/delete_customer")
def api_delete_customer(room_id: int) -> DataObject:
    return delete_customer(room_id, DBInterface(DBSession(), DBCustomers))

