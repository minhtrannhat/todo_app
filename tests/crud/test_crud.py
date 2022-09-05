from fastapi.security import OAuth2PasswordRequestForm
import pytest

from sqlalchemy.orm import Session
from fastapi_todo.crud.user_crud import get_current_user
from fastapi_todo.schemas.todo_schemas import TodoBaseSchema


from fastapi_todo.views.user_views import sign_up, login_for_access_token
from fastapi_todo.views.todo_views import add_todo_view, delete_todo_view
from fastapi_todo.schemas.user_schemas import UserCreateSchema, UserSchema
from fastapi_todo.db import get_db

email = "johndoe@gmail.com"
f_name = "John"
l_name = "Doe"
password = "johndoe123"

user_data = UserCreateSchema(
    email=email, f_name=f_name, l_name=l_name, password=password  # type: ignore
)

login_form = OAuth2PasswordRequestForm(
    grant_type="",
    username="johndoe@gmail.com",
    password="johndoe123",
    scope="",
    client_id="",
    client_secret="",
)

todo_data = TodoBaseSchema(text="walk my dog", completed=False)


with next(get_db()) as db:

    @pytest.mark.asyncio
    async def test_signup():
        new_user: UserSchema = sign_up(user_data, db)
        assert new_user.f_name == user_data.f_name
        assert new_user.l_name == user_data.l_name

    @pytest.mark.asyncio
    async def test_signin_and_add_todo():
        jwt = login_for_access_token(db, login_form)
        assert jwt != None
        todos = add_todo_view(todo_data, db, get_current_user(jwt["access_token"]))
        assert todos[0].text == "walk my dog"
        assert todos[0].completed == False
