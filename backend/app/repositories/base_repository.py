from typing import Generic, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Repositorio base para todas las entidades.

    Centraliza las operaciones CRUD comunes.
    """

    def __init__(self, model):
        self.model = model

    def get_all(
        self,
        db: Session,
    ):

        return db.query(
            self.model
        ).all()

    def get_by_id(
        self,
        db: Session,
        entity_id: str,
    ):

        return (
            db.query(self.model)
            .filter(
                self.model.id == entity_id
            )
            .first()
        )

    def delete(
        self,
        db: Session,
        entity,
    ):

        db.delete(entity)

        db.commit()