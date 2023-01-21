from typing import Any

from src.database import Base, DBSession

DataObject = dict[str, Any]


def model_to_dict(base_model: Base) -> dict[str, Any]:
    return {col.name: getattr(base_model, col.name) for col in base_model.__table__.columns}


class DBInterface:

    def __init__(self, session: DBSession, db_model: type[Base]) -> None:
        self.session = session
        self.db_model = db_model

    def read_all(self) -> list[DataObject]:
        return [model_to_dict(result) for result in self.session.query(self.db_model).all()]

    def read_by_id(self, id_: int) -> DataObject:
        return model_to_dict(self.session.query(self.db_model).get(id_))

    def create(self, new_data: DataObject) -> DataObject:
        data_to_insert = self.db_model(**new_data)
        self.session.add(data_to_insert)
        self.session.commit()

        return model_to_dict(data_to_insert)

    def update(self, id_: int, data: DataObject) -> DataObject:
        data_to_update = self.session.query(self.db_model).get(id_)

        for key, value in data.dict(exclude_none=True).items():
            setattr(data_to_update, key, value)

        self.session.commit()

        return model_to_dict(data_to_update)

    def delete(self, id_: int) -> DataObject:
        deleted_data = self.session.query(self.db_model).get(id_)
        self.session.delete(deleted_data)
        self.session.commit()
        return model_to_dict(deleted_data)
