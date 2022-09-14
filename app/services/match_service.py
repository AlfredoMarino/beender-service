from app.schemas.match import Match, MatchBase
from app.models.match import Match as MatchModel


def create_or_update_match(match: MatchBase) -> Match:
    # Validations should be here

    match_saved, is_created = MatchModel.get_or_create(
        hive_id=match.hive_id,
        bee_id=match.bee_id,
        defaults={'hive_accept': match.hive_accept, 'bee_accept': match.bee_accept}
    )

    if not is_created:
        match_saved.hive_accept = match.hive_accept
        match_saved.bee_accept = match.bee_accept

    match_saved.save()

    return Match(
        id=match_saved.id,
        hive_id=match.hive_id,
        bee_id=match.bee_id,
        hive_accept=match.hive_accept,
        bee_accept=match.bee_accept
    )
