from fastapi import APIRouter, Depends, status, HTTPException
from block17.app4.backend.db import Base
from sqlalchemy.orm import Session
from typing import Annotated
from block17.app4.models import *
from block17.app4.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from block17.app4.backend.db_depends import get_db

router = APIRouter(prefix="/user", tags=["user"])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    user = db.scalars(select(User).where(User.id)).all()
    return user


@router.get('/user_id')
async def all_users(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(user_id == User.id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    return user


@router.post('/create')
async  def create_user(session: SessionDep, username: str, firstname: str, lastname: str, age: int):
    users_name = session.scalars(select(User.slug)).all()
    if slugify(username) in users_name:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User with that username already exists'
        )
    session.execute(insert(User).values(username=username,
                                      firstname=firstname,
                                      lastname=lastname,
                                      age=age,
                                      slug=slugify(username)))
    session.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: CreateUser):
    category = db.scalars(select(User).where(User.id == user_id))
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            datail='User was not found'
        )

    db.execute(update(User).where(User.id == user_id).values(
        firstname=create_user.firstname,
        lastname=create_user.lastname,
        age=create_user.age))

    db.commit()
    return {
        'status_code': status.HTTP_202_OK,
        'transaction': 'User update is successful!'
    }


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(user_id == User.id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(delete(User).where(User.id).values(is_active=False))
    db.commit
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User delete is successful!'
    }
