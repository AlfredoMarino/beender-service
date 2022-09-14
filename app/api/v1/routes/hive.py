from typing import List, Optional
from fastapi import APIRouter, HTTPException, status, Path, Query

from app.schemas.hive import Hive
from app.services import hive_service

router = APIRouter()


@router.get(
    path="",
    response_model=List[Hive],
    response_model_exclude_none=True
)
def get_hives(bee_id: Optional[int] = Query(default=None, alias="bee")) -> List[Hive]:
    if bee_id is None:
        return hive_service.get_hives()
    else:
        return hive_service.get_hives_extended(bee_id)


@router.get(
    path="/{hive_id}",
    response_model=Hive,
    response_model_exclude_none=True
)
def get_hive(
        hive_id: int = Path(..., example=1, gt=0, description="Hive identifier")
) -> Hive:
    try:
        return hive_service.get_hive(hive_id)

    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hive not found")
