from typing import Optional

from pydantic import BaseModel, Field


class MatchBase(BaseModel):
    hive_id: int = Field(..., alias="hiveId", gt=0, example=1)
    bee_id: int = Field(..., alias="beeId", gt=0, example=1)
    bee_accept: Optional[bool] = Field(default=False, alias="beeAccept", example=True)
    hive_accept: Optional[bool] = Field(default=False, alias="hiveAccept")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Match(MatchBase):
    id: int = Field(...)
