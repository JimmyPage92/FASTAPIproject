from src.interfaces.db_interface import DataObject, DBInterface
from .schemas import RoomCreateData, RoomUpdateData


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
