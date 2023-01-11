from sqlalchemy import Column, Integer, String

from src.database import Base


class DBRoom(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    size = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    number = Column(String(250), nullable=False)
