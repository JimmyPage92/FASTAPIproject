from sqlalchemy import Column, String, Integer, Boolean
from src.database import Base


class DBCustomers(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)
    phone_number = Column(Integer, nullable=False)
    street = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    post_code = Column(Integer, nullable=False)
    want_email = Column(Boolean, nullable=False)