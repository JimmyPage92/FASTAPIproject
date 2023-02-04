from fastapi import APIRouter

from src.database import DBSession
from .schemas import BookingCreateData, BookingUpdateData
from src.interfaces.db_interface import DataObject, DBInterface
from src.api.bookings.models import DBBookings
from src.api.bookings.service import read_all_bookings, read_booking, \
    create_booking, update_booking, delete_booking

router: APIRouter = APIRouter()


@router.get("/bookings")
def api_read_all_bookings() -> list[DataObject]:
    return read_all_bookings(DBInterface(DBSession(), DBBookings))


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int) -> DataObject:
    return read_booking(booking_id, DBInterface(DBSession(), DBBookings))


@router.post("/create_booking")
def api_create_booking(new_booking: BookingCreateData) -> DataObject:
    return create_booking(new_booking, DBInterface(DBSession(), DBBookings))


@router.put("/update_booking/{booking_id}")
def api_update_booking(booking_id: int, data_to_update: BookingUpdateData) -> DataObject:
    return update_booking(booking_id, data_to_update, DBInterface(DBSession(), DBBookings))


@router.delete("/delete_booking")
def api_delete_booking(booking_id: int):
    return delete_booking(booking_id, DBInterface(DBSession(), DBBookings))
