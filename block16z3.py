from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
# create dict
users = {'1': 'Имя: Example, Возраст: 18'}


@app.get('/user')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=3, max_length=30, description='Enter username', example='Mike')]
        , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=30)]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f'User {user_id} is registered;'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=0, le=300, description='Enter user_id', example='1')]
        , username: Annotated[str, Path(min_length=3, max_length=30, description='Enter username', example='Mike')]
        , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=30)]) -> str:
    users[str(user_id)] = f'Имя: {username}, Возраст: {age}'
    return f"User {user_id} has been updated"

# not work
# @app.delete('/user/{user_id}')
# async def delete_user(user_id: int = Path(ge=0, le=300, description='Enter user_id', example='1')) -> str:
#     users.pop(str(user_id))
#     return f"User {user_id} has been deleted"



@app.delete('/user/{user_id}')
async def delete_user_id(
        user_id: Annotated[str, Path(description='Enter user ID', example='2')]) -> str:
    del users[user_id]
    return f'User {user_id} has been deleted'