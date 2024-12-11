from fastapi import FastAPI, HTTPException, Path, Request, Form
from fastapi.responses import HTMLResponse
from typing import List, Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/users/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, 'user': users[user_id-1]})


@app.post('/users/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=3, max_length=30, description='Enter username', example='username')]
        , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=30)]) -> User:
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=0, le=300, description='Enter user_id', example='1')]
        , username: Annotated[str, Path(min_length=3, max_length=30, description='Enter username', example='username')]
        , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=30)]) -> User:
    try:
        user = next((u for u in users if u.id == user_id))
        users[user_id-1] = User(id=user.id, username=username, age=age)
        return users[user_id]
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/users/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=0, le=300, description='Enter user_id', example='1')]) -> User:
    try:
        user = next((u for u in users if u.id == user_id))
        users.remove(user)
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")