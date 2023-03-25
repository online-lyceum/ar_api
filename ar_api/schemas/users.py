from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
    name: str
    coordinates: str
    job_title: str = ''


class UserCreate(BaseUser):
    pass


class User(BaseUser):
    user_id: int

    class Config:
        orm_mode = True


class UsersList(BaseModel):
    users: list[User]


class UserFilter(BaseModel):
    name: Optional[str]
    job_title: Optional[str]

