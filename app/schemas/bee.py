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
        schema_extra = {
            "example": {
                "firstname": "Freddie",
                "lastname": "Mercury",
                "interestedIn": "PYTHON_DEVELOPER",
                "experienceYears": 15,
                "bio": "Programador python",
                "picture": "photo.jpg"
            }
        }


class Bee(BeeBase):
    id: int = Field(...)


class BeeOptional(BaseModel):
    firstname: Optional[str] = Field(default=None)
    lastname: Optional[str] = Field(default=None)
    interested_in: Optional[Interest] = Field(default=None, alias="interestedIn")
    experience_years: Optional[int] = Field(default=None, alias="experienceYears")
    bio: Optional[str] = Field(default=None)
    picture: Optional[str] = Field(default=None)
