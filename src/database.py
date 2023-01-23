from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
DBSession = sessionmaker()


def init_db(db_path: str) -> None:
    # Bind elements
    engine: Engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession.bind = engine

    # Create models & apply changes
    Base.metadata.create_all(engine)


