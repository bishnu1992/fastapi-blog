# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-28 13:30:06
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-30 20:39:30
from typing import Optional, List, Dict
from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy.orm import Session
import models, schemas, OAuth2
from repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(get_token_header)],
)

@router.post('', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

@router.get('', response_model = List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog.all(db)

@router.get('/{id}', response_model = schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.show(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.UpdateBlog, db: Session = Depends(get_db)):
    return blog.update_blog(id, request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)

