# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-27 10:44:43
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-29 19:56:28
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_context.hash(password)
    def verify(password: str, hashed_password: str):
        return pwd_context.verify(password, hashed_password)
