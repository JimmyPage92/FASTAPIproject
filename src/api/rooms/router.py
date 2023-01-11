from fastapi import APIRouter

from src.database import DBSession
from .models import DBRoom
from .schemas import RoomCreateData, RoomUpdateData

router: APIRouter = APIRouter()


@router.get("/rooms")
def api_read_all_rooms():
    session: DBSession = DBSession()

    all_rooms = session.query(DBRoom).all()
    return all_rooms


@router.get("/room/{room_id}")
def api_read_room(room_id: int):
    session: DBSession = DBSession()

    room = session.query(DBRoom).get(room_id)
    return room


@router.post("/room")
def api_create_room(new_room: RoomCreateData):
    session: DBSession = DBSession()

    new_room_obj = DBRoom(**new_room.dict())
    session.add(new_room_obj)
    session.commit()
    return "Created!"


@router.put("/room/{room_id}")
def api_update_room(room_id: int, data_to_update: RoomUpdateData):
    session: DBSession = DBSession()

    room_to_update = session.query(DBRoom).get(room_id)

    for key, value in data_to_update.dict(exclude_none=True).items():
        setattr(room_to_update, key, value)

    session.commit()
    return "Updated!"


@router.delete("/room")
def api_delete_room(room_id: int):
    session = DBSession()
    room_to_delete = session.query(DBRoom).get(room_id)
    session.delete(room_to_delete)
    session.commit()
    return "Deleted!"
