# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-30 19:41:07
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-30 19:59:19
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
import JWTtoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return JWTtoken.verif_token(token, credentials_exception)

