from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy import text

Base = declarative_base()
DBSession = sessionmaker()


def init_db(db_path: str) -> None:
    # Bind elements
    engine: Engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession.bind = engine

    # Create models & apply changes
    # add_column_stmt = text('SELECT CAST(post_code AS INT) FROM customer;')
    # connection = engine.connect()
    # connection.execute(add_column_stmt)
    Base.metadata.create_all(engine)

    # add_column_stmt = text('ALTER TABLE customer ADD COLUMN city varchar(255);')
    # connection = engine.connect()
    # connection.execute(add_column_stmt)