from pydantic import BaseModel, Field


class Match(BaseModel):
    id: int = Field(...)
    hive_id: int = Field(..., alias="hiveId")
    bee_id: int = Field(..., alias="beeId")
    hive_accept: bool = Field(..., alias="hiveAccept")
    bee_accept: bool = Field(..., alias="beeAccept")
