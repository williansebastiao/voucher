from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import db_session
from app.exceptions import IntegrityErrorException, NotFoundException
from app.schemas import VoucherRequestSchema, VoucherResponseSchema
from app.services import VoucherService

router = APIRouter(
    prefix="/voucher",
    tags=["Voucher"],
)


@router.get(
    "",
    response_model=List[VoucherResponseSchema],
    status_code=status.HTTP_200_OK,
)
async def find_all(
    session: Session = Depends(db_session),
):
    service = VoucherService()
    response = await service.find_all(
        session=session,
    )

    return response


@router.get(
    "/{uuid}",
    response_model=VoucherResponseSchema,
    status_code=status.HTTP_200_OK,
)
async def find_by_uuid(
    uuid: UUID,
    session: Session = Depends(db_session),
):
    try:
        service = VoucherService()
        response = await service.find_by_uuid(
            uuid=uuid,
            session=session,
        )

        return response
    except NotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        ) from e


@router.post(
    "",
    response_model=VoucherResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    payload: VoucherRequestSchema,
    session: Session = Depends(db_session),
):

    try:
        service = VoucherService()
        response = await service.create(
            payload=payload,
            session=session,
        )

        return response
    except IntegrityErrorException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e
