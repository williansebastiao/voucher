from unittest.mock import AsyncMock, patch

import pytest

from app.services import VoucherService
from sqlalchemy.exc import IntegrityError


@pytest.fixture
def payload():
    return {
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa5",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "voucher_code": "ABC123",
    }


@pytest.fixture
def session():
    return AsyncMock()


@pytest.mark.asyncio
async def test_create_voucher_success(payload, session):
    with patch.object(
        VoucherService, "create", new_callable=AsyncMock
    ) as mock_create:
        mock_create.return_value = {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa5",
            **payload,
        }
        service = VoucherService()
        response = await service.create(payload=payload, session=session)
        mock_create.assert_awaited_once_with(payload=payload, session=session)


@pytest.mark.asyncio
async def test_find_all_vouchers(session):
    vouchers = [
        {
            "uuid": "1fa85f64-5717-4562-b3fc-2c963f66afa1",
            "first_name": "Joe",
            "last_name": "Doe",
            "email": "joe@example.com",
            "voucher_code": "XYZ789",
        },
        {
            "uuid": "2fa85f64-5717-4562-b3fc-2c963f66afa2",
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane@example.com",
            "voucher_code": "LMN456",
        },
    ]
    with patch.object(
        VoucherService, "find_all", new_callable=AsyncMock
    ) as mock_find_all:
        mock_find_all.return_value = vouchers
        service = VoucherService()
        response = await service.find_all(session=session)
        mock_find_all.assert_awaited_once_with(session=session)
        assert response == vouchers


@pytest.mark.asyncio
async def test_find_by_uuid_success(session):
    voucher = {
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa5",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "voucher_code": "ABC123",
    }
    with patch.object(
        VoucherService, "find_by_uuid", new_callable=AsyncMock
    ) as mock_find_by_uuid:
        mock_find_by_uuid.return_value = voucher
        service = VoucherService()
        response = await service.find_by_uuid(
            uuid="3fa85f64-5717-4562-b3fc-2c963f66afa5", session=session
        )
        mock_find_by_uuid.assert_awaited_once_with(
            uuid="3fa85f64-5717-4562-b3fc-2c963f66afa5", session=session
        )
        assert response == voucher


@pytest.mark.asyncio
async def test_create_voucher_duplicate_code(payload, session):

    with patch.object(
        VoucherService, "create", new_callable=AsyncMock
    ) as mock_create:
        mock_create.side_effect = IntegrityError(
            "Erro de integridade.", {}, None
        )
        service = VoucherService()
        with pytest.raises(IntegrityError):
            await service.create(payload=payload, session=session)
        mock_create.assert_awaited_once_with(payload=payload, session=session)
