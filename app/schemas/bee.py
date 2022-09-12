from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Interest(Enum):
    PYTHON_DEVELOPER = "PYTHON_DEVELOPER"
    DATA_SCIENTIST = "DATA_SCIENTIST"
    DEV_OPS = "DEV_OPS"


class Bee(BaseModel):
    id: int = Field(...)
    firstname: str = Field(...)
    lastname: str = Field(...)
    interested_in: Interest = Field(..., alias="interestedIn")
    experience_years: int = Field(..., alias="experienceYears")
    bio: Optional[str] = Field("")
    picture: str = Field(...)
    