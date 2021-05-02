# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-29 17:12:51
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-30 20:20:38
from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
import models, schemas
from repository import user

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

@router.post('', status_code = status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model = schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.get('/{id}/blogs', response_model = schemas.ShowUserBlogs)
def show(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
