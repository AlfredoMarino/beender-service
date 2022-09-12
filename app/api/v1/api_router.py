from fastapi import APIRouter
from .routes.hive import router as hive_router
from .routes.match import router as match_router


api_router = APIRouter()

api_router.include_router(hive_router, prefix="/hives", tags=["hives"])
api_router.include_router(match_router, prefix="/matches", tags=["matches"])
