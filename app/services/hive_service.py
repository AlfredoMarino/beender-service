from typing import List

from app.schemas.hive import Hive
from app.models.hive import Hive as HiveModel


def get_hives() -> List[Hive]:
    return [Hive.from_orm(hive) for hive in list(HiveModel.select())]


def get_hive(hive_id: int) -> Hive:
    hive = HiveModel.get_by_id(hive_id)

    return Hive.from_orm(hive)
