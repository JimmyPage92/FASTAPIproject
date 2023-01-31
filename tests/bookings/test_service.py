import unittest

from src.interfaces.db_interface import DataObject
from src.api.bookings.service import create_booking
from src.api.bookings.schemas import BookingCreateData


class DataInterfaceStub:
    def create(self, booking_data) -> DataObject:
        raise NotImplementedError()


class BookingInterface(DataInterfaceStub):
    def create(self, booking_data: DataObject) -> DataObject:
        new_booking = dict(booking_data)
        new_booking["id"] = 1
        print(new_booking)
        return new_booking


class TestBooking(unittest.TestCase):
    def test_create_booking(self):
        booking_data = create_booking(
            BookingCreateData(
                id=1,
                from_date="2022-01-01",
                to_date="2022-01-20",
                price=100,
                customer_id=1,
                room_id=1,
            ),
            booking_interface=BookingInterface(),
        )
        self.assertEqual(booking_data["price"], 100)


""""""