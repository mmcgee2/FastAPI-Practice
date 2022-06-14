from pydantic import BaseModel

# from .Model import User


class UserBase(BaseModel):
    au_fname: str
    phone: str | None = None
    age: int


class UserCreate(UserBase):
    name: str


class author(UserBase):
    au_id: str

    class Config:
        orm_mode = True
