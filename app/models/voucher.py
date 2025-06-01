from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import BaseModel


class VoucherModel(BaseModel):

    __tablename__ = "vouchers"

    first_name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
    )
    voucher_code: Mapped[str] = mapped_column(
        String(6),
        unique=True,
        nullable=False,
    )
