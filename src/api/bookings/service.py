from src.interfaces.db_interface import DataObject, DBInterface
from .schemas import BookingCreateData, BookingUpdateData


def read_all_bookings(booking_interface: DBInterface) -> list[DataObject]:
    return booking_interface.read_all()


def read_booking(booking_id: int, booking_interface: DBInterface) -> DataObject:
    return booking_interface.read_by_id(booking_id)


def create_booking(new_booking: BookingCreateData, booking_interface: DBInterface) -> DataObject:
    return booking_interface.create(new_booking.dict())


def update_booking(booking_id: int, booking_to_update: BookingUpdateData, booking_interface: DBInterface) -> DataObject:
    return booking_interface.update(booking_id, booking_to_update)


def delete_booking(booking_id: int, booking_interface: DBInterface) -> DataObject:
    return booking_interface.delete(booking_id)