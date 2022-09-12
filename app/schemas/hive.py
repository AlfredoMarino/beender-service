from pydantic import BaseModel, Field


class Hive(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    queen_bee: str = Field(..., alias="queenBee")
    picture: str = Field(...)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
