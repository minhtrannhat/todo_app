from pydantic import BaseModel
from pydantic import EmailStr

from fastapi_todo.schemas.todoSchemas import todoSchema


class UserBase(BaseModel):
    email: EmailStr


class UserSchema(UserBase):
    first_name: str
    last_name: str

    class Config:
        org_mode = True


class UserCreateSchema(UserSchema):
    password: str

    class Config:
        org_mode = False


class UserFullSchema(UserSchema):
    todos: list[todoSchema]
