import sqlalchemy.sql
from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
from src.database import DBSession
from .models import DBCustomers
from .schemas import CustomerCreateData, CustomerUpdateData
from src.interfaces.db_interface import DataObject, DBInterface
from .service import read_all_customers, read_customer, create_customer, update_customer, delete_customer
from src.database import Base

router: APIRouter = APIRouter()


@router.get("/customers")
def api_read_all_customers() -> list[DataObject]:
    return read_all_customers(DBInterface(DBSession(), DBCustomers))


@router.get("/customer/{customer_id}")
def api_read_customer(customer_id: int) -> DataObject:
    return read_customer(customer_id, DBInterface(DBSession(), DBCustomers))


@router.post("/customer")
def api_create_customer(new_customer: CustomerCreateData) -> DataObject:
    return create_customer(new_customer, DBInterface(DBSession(), DBCustomers))


@router.put("/customer/{customer_id}")
def api_update_customer(customer_id: int, data_to_update: CustomerUpdateData) -> DataObject:
    return update_customer(customer_id, data_to_update, DBInterface(DBSession(), DBCustomers))


@router.delete("/customer")
def api_delete_customer(room_id: int) -> DataObject:
    return delete_customer(room_id, DBInterface(DBSession(), DBCustomers))

# wartośc bool która sprawdzić czy klient chce otrzymwać maile
# jak napisac zapytanie zeby uzyskac informacje z bazy danych czy klient chce dostawac mejla ??
# jak pisac zapytania w sqlalchemy??
# @router.get("/customers/email_info/{customer_id}/")
# def want_email(customer_id: int, db: Base):
#     pass


# @router.get('/do_you_want_email/{response}')
# def want_email(response: bool) -> None:
#     if response == True:
#         return 1
#     elif response == False:
#         return 0
