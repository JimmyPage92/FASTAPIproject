from fastapi import FastAPI

from .config import Config
from .database import init_db
from src.api.rooms import rooms_router

app: FastAPI = FastAPI()


@app.on_event("startup")
def startup_event() -> None:
    init_db(Config.db_file_loc)


@app.get("/")
def read_root() -> str:
    return "The server is running."


app.include_router(rooms_router)
