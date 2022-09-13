from typing import Optional

from pydantic import BaseModel, Field


class MatchBase(BaseModel):
    hive_id: int = Field(..., alias="hiveId", gt=0, example=1, description="Hive identifier")
    bee_id: int = Field(..., alias="beeId", gt=0, example=1, description="Bee identifier")
    bee_accept: Optional[bool] = Field(default=False, alias="beeAccept", example=True, description="Bee match response")
    hive_accept: Optional[bool] = Field(default=False, alias="hiveAccept", description="Hive match response")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Match(MatchBase):
    id: int = Field(..., description="Match identifier")
