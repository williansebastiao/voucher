import random
import string
from uuid import UUID

from sqlalchemy.orm import Session

from app.models import VoucherModel
from app.repositories import VoucherRepository
from app.schemas import VoucherRequestSchema


class VoucherService:

    def __init__(self):
        self.repository = VoucherRepository()

    async def create(
        self,
        payload: VoucherRequestSchema,
        session: Session,
    ) -> VoucherModel:
        voucher_code = await self.generate_voucher_code()

        response_schema = VoucherRequestSchema(
            first_name=payload.first_name,
            last_name=payload.last_name,
            email=payload.email,
            voucher_code=voucher_code,
        )

        response = await self.repository.create(
            payload=response_schema,
            session=session,
        )

        return response

    async def find_all(self, session: Session) -> VoucherModel:
        response = await self.repository.find_all(session=session)
        return response

    async def find_by_uuid(
        self,
        uuid: UUID,
        session: Session,
    ) -> VoucherModel:
        response = await self.repository.find_by_uuid(
            uuid=uuid,
            session=session,
        )
        return response

    async def generate_voucher_code(self, length: int = 6) -> str:
        characters = string.ascii_uppercase + string.digits
        return "".join(random.choice(characters) for _ in range(length))
