from fastapi import FastAPI

from .config import Config
from .database import init_db
from src.api.rooms import rooms_router
from src.api.customers import customer_router
from src.api.bookings import bookings_router

app: FastAPI = FastAPI()


@app.on_event("startup")
def startup_event() -> None:
    init_db(Config.SQLALCHEMY_DATABASE_URI)


@app.get("/")
def read_root() -> str:
    return "The server is running."


app.include_router(rooms_router)
app.include_router(customer_router)
app.include_router(bookings_router)

