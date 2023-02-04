from typing import Optional

from datetime import date

from pydantic import BaseModel


class BookingCreateData(BaseModel):
    from_date: date
    to_date: date
    price: int
    customer_id: int
    room_id: int


class BookingUpdateData(BaseModel):
    from_date: Optional[date]
    to_date: Optional[date]
    price: Optional[int]
    customer_id: Optional[int]
    room_id: Optional[int]
