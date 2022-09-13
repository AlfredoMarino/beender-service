from typing import List

from fastapi import APIRouter

from app.schemas.bee import Bee, BaseBee

router = APIRouter()


@router.get(
    path="",
    response_model=List[Bee]
)
def get_bees() -> List[Bee]:
    pass


@router.post(
    path="",
    response_model=Bee
)
def create_bee(bee: Bee) -> Bee:
    pass


@router.patch(
    path="/{bee_id}",
    response_model=Bee
)
def update_bee(bee_id: int, bee: BaseBee) -> Bee:
    pass


@router.delete(
    path="/{bee_id}",
    response_model=None
)
def delete_bee(bee_id: int) -> None:
    pass
