from datetime import date

from fastapi import APIRouter

from src.database import DBSession
from .models import DBRoom
from .schemas import RoomCreateData, RoomUpdateData
from src.interfaces.db_interface import DataObject, DBInterface
from .service import read_all_rooms, read_room, create_room, update_room, delete_room, check_room_availability, \
    find_available_rooms

router: APIRouter = APIRouter()


@router.get("/rooms")
def api_read_all_rooms() -> list[DataObject]:
    return read_all_rooms(DBInterface(DBSession(), DBRoom))


@router.get("/room/{room_id}")
def api_read_room(room_id: int) -> DataObject:
    return read_room(room_id, DBInterface(DBSession(), DBRoom))


@router.post("/room")
def api_create_room(new_room: RoomCreateData) -> DataObject:
    return create_room(new_room, DBInterface(DBSession(), DBRoom))


@router.put("/room/{room_id}")
def api_update_room(room_id: int, data_to_update: RoomUpdateData) -> DataObject:
    return update_room(room_id, data_to_update, DBInterface(DBSession(), DBRoom))


@router.delete("/room")
def api_delete_room(room_id: int) -> DataObject:
    return delete_room(room_id, DBInterface(DBSession(), DBRoom))


@router.get('/is_room_available/{room_id}')
def api_is_room_available(room_id: int, from_date: date, to_date: date) -> str:
    session: DBSession = DBSession()

    is_room_available: bool = check_room_availability(session, room_id, from_date, to_date)

    return f"{is_room_available}"


@router.get('/find_available_rooms')
def api_find_available_rooms(from_date: date, to_date: date):
    return find_available_rooms(DBSession(), from_date, to_date)
