from fastapi import APIRouter

from src.database import DBSession
from .models import DBCustomers
from .schemas import CustomerCreateData, CustomerUpdateData

router: APIRouter = APIRouter()


@router.get("/customers")
def api_read_all_customers():
    session: DBSession = DBSession()

    all_customers = session.query(DBCustomers).all()
    return all_customers


@router.get("/customer/{customer_id}")
def api_read_customer(customer_id: int):
    session: DBSession = DBSession()

    customer = session.query(DBCustomers).get(customer_id)
    return customer


@router.post("/customer")
def api_create_customer(new_customer: CustomerCreateData):
    session: DBSession = DBSession()

    new_customer_obj = DBCustomers(**new_customer.dict())
    session.add(new_customer_obj)
    session.commit()
    return "Created new customer!"


@router.put("/customer/{customer_id}")
def api_update_customer(customer_id: int, data_to_update: CustomerUpdateData):
    session: DBSession = DBSession()

    customer_to_update = session.query(DBCustomers).get(customer_id)

    for key, value in data_to_update.dict(exclude_none=True).items():
        setattr(customer_to_update, key, value)

    session.commit()
    return "Updated customer!"


@router.delete("/customer")
def api_delete_customer(customer_id: int):
    session = DBSession()
    customer_to_delete = session.query(DBCustomers).get(customer_id)
    session.delete(customer_to_delete)
    session.commit()
    return "Deleted customer!"


