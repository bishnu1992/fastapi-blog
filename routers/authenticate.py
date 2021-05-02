# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-29 17:12:51
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-30 20:25:04
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from sqlalchemy.orm import Session
import schemas
from repository import user

router = APIRouter(
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm  = Depends(), db: Session = Depends(get_db)):
    return user.login(request, db)
