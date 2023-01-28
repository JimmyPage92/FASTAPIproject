import unittest

from src.api.rooms.schemas import RoomCreateData
from src.api.rooms.service import create_room
from src.interfaces.db_interface import DataObject


class DataInterfaceStub:
    def create(self, room_data) -> DataObject:
        raise NotImplementedError()


class RoomInterface(DataInterfaceStub):
    def create(self, room_data: DataObject) -> DataObject:
        new_room = dict(room_data)
        new_room["id"] = 1
        print(new_room)
        return new_room


class TestRoom(unittest.TestCase):
    def test_create_room(self):
        room_data = create_room(
            RoomCreateData(
                id=1,
                price=100,
                number=100,
                size=100
            ),
            room_interface=RoomInterface(),
        )
        self.assertEqual(room_data["price"], 100)


