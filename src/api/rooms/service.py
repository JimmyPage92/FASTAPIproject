from datetime import date

from sqlalchemy import and_

from src.interfaces.db_interface import DataObject, DBInterface
from src.api.bookings.models import DBBookings
from .models import DBRoom
from .schemas import RoomCreateData, RoomUpdateData
from ...database import DBSession


def read_all_rooms(room_interface: DBInterface) -> list[DataObject]:
    return room_interface.read_all()


def read_room(room_id: int, room_interface: DBInterface) -> DataObject:
    return room_interface.read_by_id(room_id)


def create_room(new_room: RoomCreateData, room_interface: DBInterface) -> DataObject:
    return room_interface.create(new_room.dict())


def update_room(room_id: int, room_to_update: RoomUpdateData, room_interface: DBInterface) -> DataObject:
    return room_interface.update(room_id, room_to_update)


def delete_room(room_id: int, room_interface: DBInterface) -> DataObject:
    return room_interface.delete(room_id)


def check_room_availability(session: DBSession, room_id: int, from_date: date, to_date: date) -> bool:
    overlapping_bookings = session.query(DBBookings).filter(
        and_(DBBookings.room_id == room_id, DBBookings.from_date <= to_date, DBBookings.to_date >= from_date)
    ).all()
    return len(overlapping_bookings) == 0


def find_available_rooms(session: DBSession, from_date: date, to_date: date) -> list[DBRoom]:
    all_rooms: list[DBRoom] = session.query(DBRoom).all()
    return [room for room in all_rooms if check_room_availability(session, room.id, from_date, to_date)]

