from typing import Optional

from pydantic import BaseModel


class RoomCreateData(BaseModel):
    size: int
    price: int
    number: int


class RoomUpdateData(BaseModel):
    size: Optional[int]
    price: Optional[int]
    number: Optional[int]
