from typing import List

from peewee import JOIN

from app.schemas.hive import Hive
from app.models.hive import Hive as HiveModel
from app.models.match import Match as MatchModel


def get_hives() -> List[Hive]:
    return [Hive.from_orm(hive) for hive in list(HiveModel.select())]


def get_hives_extended(bee_id: int) -> List[Hive]:
    query = (
        HiveModel.select(
            HiveModel.id,
            HiveModel.name,
            HiveModel.description,
            HiveModel.queen_bee,
            HiveModel.picture,
            MatchModel.hive_accept,
            MatchModel.bee_accept
        )
        .join(MatchModel, JOIN.LEFT_OUTER, on=((HiveModel.id == MatchModel.hive_id) & (MatchModel.bee_id == bee_id)))
    )

    return [_map_hive_extended(hive) for hive in query.namedtuples()]


def get_hive(hive_id: int) -> Hive:
    hive = HiveModel.get_by_id(hive_id)

    return Hive.from_orm(hive)


def _map_hive_extended(hive) -> Hive:
    return Hive(
        id=hive.id,
        name=hive.name,
        description=hive.description,
        queen_bee=hive.queen_bee,
        picture=hive.picture,
        bee_accept=hive.bee_accept,
        hive_accept=hive.hive_accept
    )
