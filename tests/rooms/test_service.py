import unittest

import pytest

# from src.api.rooms.schemas import RoomCreateData
# from src.api.rooms.service import create_room
# from src.interfaces.db_interface import DataObject
# from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
import fastapi


# class DataInterfaceStub:
#     def create(self, room_data) -> DataObject:
#         raise NotImplementedError()

#
# class RoomInterface(DataInterfaceStub):
#     def create(self, room_data: DataObject) -> DataObject:
#         new_room = dict(room_data)
#         new_room["id"] = 1
#         print(new_room)
#         return new_room


# class TestRoom(unittest.TestCase):
#     def test_create_room(self):
#         room_data = create_room(
#             RoomCreateData(
#                 id=1,
#                 price=100,
#                 number=100,
#                 size=100
#             ),
#             room_interface=RoomInterface(),
#         )
#         self.assertEqual(room_data["price"], 100)


"""reading room --> mockowanie pokoju/endpointa??? """


@pytest.mark.parametrize("room_id, expected_results", [
    (1, {"id": 1, "price": 100, "number": 100, "size": 100})
])
def test_api_read_room(room_id: int, expected_results: dict):
    app = fastapi.FastAPI()
    from src.main import rooms_router
    app.include_router(rooms_router)
    client = TestClient(app)
    response = client.get("/room/{room_id}")
    assert response.status_code == 200
    assert response.json() == expected_results

