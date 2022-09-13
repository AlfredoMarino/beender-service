from pydantic import BaseModel, Field


class Hive(BaseModel):
    id: int = Field(..., description="Hive identifier")
    name: str = Field(..., description="Hive name")
    description: str = Field(..., description="Hive description")
    queen_bee: str = Field(..., alias="queenBee", description="Hive manager")
    picture: str = Field(..., description="Hive Picture")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
