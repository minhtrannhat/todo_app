from pydantic import BaseModel


class todoBaseSchema(BaseModel):
    text: str
    completed: bool


class todoSchema(todoBaseSchema):
    owner_id: int

    class Config:
        orm_mode = True


class todoResponseSchema(todoSchema):
    id: int


class todoUpdateSchema(todoBaseSchema):
    id: int
