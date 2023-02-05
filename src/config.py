from dataclasses import dataclass


@dataclass
class Config:
    db_file_loc: str = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_DATABASE_URI: str = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"