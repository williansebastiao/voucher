from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, ConfigDict


class VoucherRequestSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    voucher_code: Optional[str] = None


class VoucherResponseSchema(VoucherRequestSchema):
    uuid: UUID

    model_config = ConfigDict(
        from_attributes=True,
    )
