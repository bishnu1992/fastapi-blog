# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-29 20:23:46
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-30 20:32:17
from jose import JWTError, jwt
from datetime import datetime, timedelta
import schemas

SECRET_KEY = "b7747f5c082bff276dbb62844119c2ef2c606325ceb1e83bb021af35c3ef04e5"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verif_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        user_id: int = payload.get("user_id")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return {"email":email, "user_id":user_id}
