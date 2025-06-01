from typing import List
from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.exceptions import IntegrityErrorException, NotFoundException
from app.models import VoucherModel
from app.repositories import AbstractRepository
from app.schemas import VoucherRequestSchema


class VoucherRepository(AbstractRepository):
    def __init__(self): ...

    async def create(
        self,
        payload: VoucherRequestSchema,
        session: Session,
    ) -> VoucherModel:

        try:
            response = VoucherModel(**payload.model_dump())

            session.add(response)
            session.commit()
            session.refresh(response)

            return response
        except IntegrityError as e:
            raise IntegrityErrorException() from e

    async def find_all(self, session: Session) -> List[VoucherModel]:
        response = (
            session.query(VoucherModel)
            .order_by(VoucherModel.created_at.desc())
            .all()
        )

        return response

    async def find_by_uuid(
        self,
        uuid: UUID,
        session: Session,
    ):
        response = (
            session.query(VoucherModel)
            .filter(VoucherModel.uuid == uuid)
            .first()
        )

        if not response:
            raise NotFoundException()

        return response
