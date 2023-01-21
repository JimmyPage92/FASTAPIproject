from fastapi import APIRouter

from src.database import DBSession
from .models import DBBookings
from .schemas import BookingCreateData, BookingUpdateData

router: APIRouter = APIRouter()


@router.get("/bookings")
def api_read_all_bookings():
    session: DBSession = DBSession()

    all_bookings = session.query(DBBookings).all()
    return all_bookings


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int):
    session: DBSession = DBSession()

    booking = session.query(DBBookings).get(booking_id)
    return booking


@router.post("/booking")
def api_create_booking(new_booking: BookingCreateData):
    session: DBSession = DBSession()

    new_booking_obj = DBBookings(**new_booking.dict())
    session.add(new_booking_obj)
    session.commit()
    return "Created new booking!"


@router.put("/booking/{booking_id}")
def api_update_booking(booking_id: int, data_to_update: BookingUpdateData):
    session: DBSession = DBSession()

    booking_to_update = session.query(DBBookings).get(booking_id)

    for key, value in data_to_update.dict(exclude_none=True).items():
        setattr(booking_to_update, key, value)

    session.commit()
    return "Updated booking!"


@router.delete("/booking")
def api_delete_booking(booking_id: int):
    session = DBSession()
    booking_to_delete = session.query(DBBookings).get(booking_id)
    session.delete(booking_to_delete)
    session.commit()
    return "Deleted booking!"