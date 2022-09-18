from typing import List

from fastapi import APIRouter, Path, Body

from app.schemas.bee import Bee, BeeBase, BeeOptional
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
def get_bee(bee_id: int = Path(..., example=1, gt=0, description="Bee identifier")) -> Bee:
    return bee_service.get_bee(bee_id)


@router.post(
    path="",
    response_model=Bee
)
def create_bee(bee: BeeBase) -> Bee:
    return bee_service.create_bee(bee)


@router.put(
    path="/{bee_id}",
    response_model=Bee
)
def update_bee(
        bee_id: int = Path(..., example=1, gt=0, description="Bee identifier"),
        bee: BeeBase = Body(..., description="Entire bee to update")
) -> Bee:
    return bee_service.update_bee(bee_id, bee)


@router.patch(
    path="/{bee_id}",
    response_model=Bee
)
def partial_update_bee(
        bee_id: int = Path(..., example=1, gt=0, description="Bee identifier"),
        bee: BeeOptional = Body(..., description="Bee to update")
) -> Bee:
    return bee_service.update_bee(bee_id, bee, True)


@router.delete(
    path="/{bee_id}",
    response_model=None,
    status_code=204
)
def delete_bee(bee_id: int = Path(..., example=1, gt=0, description="Bee identifier")) -> None:
    bee_service.delete_bee(bee_id)
