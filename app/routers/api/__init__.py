from fastapi import APIRouter

from . import health, voucher

router = APIRouter()

router.include_router(health.router)
router.include_router(voucher.router)
