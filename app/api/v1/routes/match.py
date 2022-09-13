from fastapi import APIRouter, Body

from app.schemas.match import Match, MatchBase
from app.services import match_service

router = APIRouter()

MATCH_EXAMPLE = MatchBase(hive_id=1, bee_id=1, bee_accept=True, hive_accept=None)


@router.post(
    path="",
    response_model=Match,
    summary="Save a Match"
)
def create_match(
        match: MatchBase = Body(example=MATCH_EXAMPLE)
) -> Match:
    return match_service.create_match(match)
