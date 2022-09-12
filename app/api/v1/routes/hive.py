from typing import List
from fastapi import APIRouter

from app.schemas.hive import Hive
from app.services import hive_service

router = APIRouter()


@router.get(
    path="",
    response_model=List[Hive]
)
def get_hives() -> List[Hive]:
    return hive_service.get_hives()
