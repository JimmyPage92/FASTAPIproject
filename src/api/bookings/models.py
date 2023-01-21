from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base
from src.api.customers.models import DBCustomers
from src.api.rooms.models import DBRoom


class DBBookings(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)

    customer = relationship(DBCustomers)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    room = relationship(DBRoom)
    room_id = Column(Integer, ForeignKey("room.id"))
