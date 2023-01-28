import unittest

from src.api.bookings.schemas import BookingCreateData
from src.interfaces.db_interface import DataObject
from src.api.bookings.service import create_booking

class DataInterfaceStub:
    def create(self, booking_data) -> DataObject:
        raise NotImplementedError()


class BookingInterface(DataInterfaceStub):
    def create(self, booking_data) -> DataObject:
        new_booking = dict(booking_data)
        new_booking['id'] = 1
        print(new_booking)
        return new_booking

class TestBooking(unittest.TestCase):
    def test_create_booking(self):
        booking_data = create_booking(
            BookingCreateData(



            )
        )
        self.assertEqual(booking_data)