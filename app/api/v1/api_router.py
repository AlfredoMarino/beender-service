from fastapi import APIRouter, Depends
from .routes.hive import router as hive_router
from .routes.match import router as match_router
from ...core.db import get_db
from .routes.bee import router as bee_router


api_router = APIRouter()

api_router.include_router(hive_router, prefix="/hives", tags=["hives"], dependencies=[Depends(get_db)])
api_router.include_router(match_router, prefix="/matches", tags=["matches"], dependencies=[Depends(get_db)])
api_router.include_router(bee_router, prefix="/bees", tags=["bees"], dependencies=[Depends(get_db)])
