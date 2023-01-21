from sqlalchemy import Column, Integer, String

from src.database import Base

class DBCustomers(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)
    # phone_number = Column(Integer, nullable=False)
    # street = Column(String(100), nullable=False)
    # city = Column(String(100), nullable=False)
    # post_code = Column(Integer, nullable=False)

