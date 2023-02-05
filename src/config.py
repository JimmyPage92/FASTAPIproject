from dataclasses import dataclass


@dataclass
class Config:
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_DATABASE_URI: str = 'postgresql+psycopg2://postgres:postgres@db:5432/hotel_db'