from fastapi import APIRouter, Query

from src.database import DBSession
from .models import DBCustomers
from .schemas import CustomerCreateData, CustomerUpdateData
from src.interfaces.db_interface import DataObject, DBInterface
from .service import read_all_customers, read_customer, create_customer, update_customer, delete_customer
import datetime

router: APIRouter = APIRouter()


@router.get("/customers")
def api_read_all_customers() -> list[DataObject]:
    return read_all_customers(DBInterface(DBSession(), DBCustomers))


@router.get("/customer/{customer_id}")
def api_read_customer(customer_id: int) -> DataObject:
    return read_customer(customer_id, DBInterface(DBSession(), DBCustomers))



# wartośc bool która sprawdzić czy kileint chce otrzymwać maile
# @router.options("/customer/want_email/{customer_id}/")
# def api_response_customer(customer_id: int, customer_response: Optional[str] = True or False):
#
#     return read_customer(customer_id, DBInterface(DBSession(), DBCustomers))


@router.post("/customer")
def api_create_customer(new_customer: CustomerCreateData) -> DataObject:
    return create_customer(new_customer, DBInterface(DBSession(), DBCustomers))


@router.put("/customer/{customer_id}")
def api_update_customer(customer_id: int, data_to_update: CustomerUpdateData) -> DataObject:
    return update_customer(customer_id, data_to_update, DBInterface(DBSession(), DBCustomers))


@router.delete("/customer")
def api_delete_customer(room_id: int) -> DataObject:
    return delete_customer(room_id, DBInterface(DBSession(), DBCustomers))


@router.get('/want_email/{customer_id}')
async def customer_want_email(customer_id: int, answer: str = Query(..., min_length=1)):
    if answer == 'yes' or 'tak' or 'y':
        return f'{True} Customer o numerze id: {customer_id} chce wysylania mejli'
    elif answer == '' or 'no':
        return f'{False} Customer o numerze id {customer_id} nie chce wysylania mejli'
    else:
        return f'{False} Customer o numerze id {customer_id} nie chce wysylania mejli'

