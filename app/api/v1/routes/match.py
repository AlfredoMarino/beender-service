from fastapi import APIRouter

from app.schemas.match import Match, MatchBase
from app.services import match_service

router = APIRouter()


@router.post(
    path="",
    response_model=Match
)
def create_match(match: MatchBase) -> Match:
    return match_service.create_match(match)

