from typing import List

from fastapi import HTTPException, status

from app.schemas.bee import Bee, BeeBase
from app.models.bee import Bee as BeeModel


def get_bees() -> List[Bee]:
    bees = list(BeeModel.select().namedtuples())

    # result = []
    # for n in range(0, 10):
    #     result.append(n)

    result = []
    for bee in bees:
        bee_saved = Bee(
            id=bee.id,
            firstname=bee.firstname,
            lastname=bee.lastname,
            interested_in=bee.interested_in,
            experience_years=bee.experience_years,
            bio=bee.bio,
            picture=bee.picture
        )
        result.append(bee_saved)

    return result
    # return [Bee.from_orm(bee) for bee in list(BeeModel.select().namedtuples())]


def get_bee(bee_id: int) -> Bee:
    bee = BeeModel.get_by_id(bee_id)
    bee_saved = Bee(
        id=bee.id,
        firstname=bee.firstname,
        lastname=bee.lastname,
        interested_in=bee.interested_in,
        experience_years=bee.experience_years,
        bio=bee.bio,
        picture=bee.picture
    )
    #
    return bee_saved
    # return Bee.from_orm(BeeModel.get_by_id(bee_id))


def create_bee(bee: BeeBase) -> Bee:
    # if bee.picture is None or len(bee.picture.strip()) == 0:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Picture is required")

    new_bee = BeeModel.create(
        firstname=bee.firstname,
        lastname=bee.lastname,
        interested_in=bee.interested_in.name,
        experience_years=bee.experience_years,
        picture=bee.picture,
        bio=bee.bio
    )

    return Bee.from_orm(new_bee)
