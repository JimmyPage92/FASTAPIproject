from sqlalchemy import Column, Integer, DATE, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base

class DBBookings(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_date = Column(DATE, nullable=False)
    to_date = Column(DATE, nullable=False)
    price = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    room_id = Column(Integer, ForeignKey("room.id"))
