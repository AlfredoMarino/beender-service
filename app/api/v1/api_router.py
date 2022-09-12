from fastapi import APIRouter
from .routes.hive import router as hive_router


api_router = APIRouter()

api_router.include_router(hive_router, prefix="/hives", tags=["hives"])
