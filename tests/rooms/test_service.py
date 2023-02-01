import unittest

from src.api.rooms.schemas import RoomCreateData
from src.api.rooms.service import create_room
from src.interfaces.db_interface import DataObject
from unittest.mock import MagicMock, patch

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


"""reading room --> mockowanie pokoju/endpointa??? """

# class TestReadAnyRoom(unittest.TestCase):
#
#     def test_read_room(self, user):
#         data = {
#                 "id": 1,
#                 "size": 10,
#                 "price": 15000,
#                 "number": "10",
#     }
#         mocked_response = MagicMock()
#         mocked_response.json.return_value = data
#         user.get.return_value = mocked_response
#
#
#         with patch("requests.get", user.get):
#             result = test_read_room()
#             self.assertEqual(result, data)

