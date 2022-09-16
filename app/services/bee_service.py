from typing import List

from app.schemas.bee import Bee
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


def get_bee(bee_id) -> Bee:
    # bee = BeeModel.get_by_id(bee_id)
    # bee_saved = Bee(
    #     id=bee.id,
    #     firstname=bee.firstname,
    #     lastname=bee.lastname,
    #     interested_in=bee.interested_in,
    #     experience_years=bee.experience_years,
    #     bio=bee.bio,
    #     picture=bee.picture
    # )

    # return bee_saved
    return Bee.from_orm(BeeModel.get_by_id(bee_id))
