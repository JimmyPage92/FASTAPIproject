from dataclasses import dataclass


@dataclass
class Config:
    db_file_loc: str = "sqlite:///hotel.db"
