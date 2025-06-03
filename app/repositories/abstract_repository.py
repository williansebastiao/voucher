from abc import abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.orm import Session

T = TypeVar("T", bound=BaseModel)


class AbstractRepository(Generic[T]):

    @abstractmethod
    async def create(
        self,
        payload: T,
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
