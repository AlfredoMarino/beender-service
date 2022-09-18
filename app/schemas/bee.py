from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, validator


class Interest(str, Enum):
    PYTHON_DEVELOPER = "PYTHON_DEVELOPER"
    DATA_SCIENTIST = "DATA_SCIENTIST"
    DEV_OPS = "DEV_OPS"


class BeeBase(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    interested_in: Interest = Field(..., alias="interestedIn")
    # experience_years: int = Field(..., alias="experienceYears")
    experience_years: int = Field(..., alias="experienceYears", ge=0)
    bio: Optional[str] = Field("")
    picture: str = Field(...)

    # @validator("picture", pre=True, always=True)
    # def check_picture(cls, picture):
    #     assert len(picture.strip()) > 0, "Picture cannot be empty."
    #     return picture

    class Config:
        allow_population_by_field_name = True
        orm_mode = True


class Bee(BeeBase):
    id: int = Field(...)
