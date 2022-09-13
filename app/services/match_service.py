from app.schemas.match import Match, MatchBase
from app.models.match import Match as MatchModel


def create_match(match: MatchBase) -> Match:

    # Validations should be here

    match_saved = MatchModel(
        hive_id=match.hive_id,
        bee_id=match.bee_id,
        hive_accept=match.hive_accept,
        bee_accept=match.bee_accept
    )

    match_saved.save()

    return Match(
        id=match_saved.id,
        hive_id=match.hive_id,
        bee_id=match.bee_id,
        hive_accept=match.hive_accept,
        bee_accept=match.bee_accept
    )
