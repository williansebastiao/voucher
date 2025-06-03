import uuid as puuid

import pendulum
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):

    __abstract__ = True

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        default=lambda: puuid.uuid4(),
        primary_key=True,
        index=True,
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=pendulum.now(),
        nullable=False,
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=pendulum.now(),
        onupdate=pendulum.now(),
        nullable=False,
    )
