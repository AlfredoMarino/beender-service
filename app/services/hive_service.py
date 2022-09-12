from typing import List

from fastapi import HTTPException, status

from app.schemas.hive import Hive
from app.models.hive import Hive as HiveModel


def get_hives() -> List[Hive]:
    return [Hive.from_orm(hive) for hive in list(HiveModel.select())]


def get_hive(hive_id: int) -> Hive:
    hive = HiveModel.select().where(HiveModel.id == hive_id).get_or_none()
    if hive is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hive not found")
    return Hive.from_orm(hive) if hive is not None else []
