from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import Field
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID]  = Field(default_factory=uuid4) #Using uuid4() directly as a default value will generate the same UUID for all users. Use default_factory instead.    first_name: str
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]
