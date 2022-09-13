from typing import List
from fastapi import APIRouter, HTTPException, status, Path

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
def get_hive(
        hive_id: int = Path(..., example=1, gt=0, description="Hive identifier")
) -> Hive:
    try:
        return hive_service.get_hive(hive_id)

    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hive not found")
