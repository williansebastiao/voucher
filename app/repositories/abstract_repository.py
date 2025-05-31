from abc import ABC, abstractmethod
from uuid import UUID

from pydantic import BaseModel


class AbstractRepository(ABC):

    @abstractmethod
    def create(self, payload: BaseModel): ...

    @abstractmethod
    def find_all(self): ...

    @abstractmethod
    def find_by_uuid(self, uuid: UUID): ...
