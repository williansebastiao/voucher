from abc import ABC, abstractmethod
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.orm import Session


class AbstractRepository(ABC):

    @abstractmethod
    async def create(
        self,
        payload: BaseModel,
        session: Session,
    ): ...

    @abstractmethod
    async def find_all(
        self,
        session: Session,
    ): ...

    @abstractmethod
    async def find_by_uuid(
        self,
        uuid: UUID,
        session: Session,
    ): ...
