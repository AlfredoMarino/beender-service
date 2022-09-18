from typing import List

from fastapi import APIRouter

from app.schemas.bee import Bee, BeeBase
from app.services import bee_service

router = APIRouter()


@router.get(
    path="",
    response_model=List[Bee]
)
def get_bees() -> List[Bee]:
    return bee_service.get_bees()


@router.get(
    path="/{bee_id}",
    response_model=Bee
)
def get_bee(bee_id) -> Bee:
    return bee_service.get_bee(bee_id)


@router.post(
    path="",
    response_model=Bee
)
def create_bee(bee: BeeBase) -> Bee:
    return bee_service.create_bee(bee)


@router.patch(
    path="/{bee_id}",
    response_model=Bee
)
def update_bee(bee_id: int, bee: BeeBase) -> Bee:
    pass


@router.delete(
    path="/{bee_id}",
    response_model=None
)
def delete_bee(bee_id: int) -> None:
    pass
