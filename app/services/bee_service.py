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
        new_bee = Bee(
            id=bee.id,
            firstname=bee.firstname,
            lastname=bee.lastname,
            interested_in=bee.interested_in,
            experience_years=bee.experience_years,
            bio=bee.bio,
            picture=bee.picture
        )
        result.append(new_bee)

    return result

