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


@router.get(
    path="/{hive_id}",
    response_model=Hive
)
def get_hives(hive_id: int) -> Hive:
    return hive_service.get_hive(hive_id)
