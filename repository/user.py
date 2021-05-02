# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-29 17:12:51
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-30 20:29:50
from fastapi import Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
import models, JWTtoken
from hashing import Hash

def create(request, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'data': {'message': 'User created', 'respose': new_user}}

def show(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'No user found')
    return user

def login(request, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Invalid Credentials')

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Invalid Password')

    access_token = JWTtoken.create_access_token(data={"email": user.email, "user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
