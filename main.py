# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-15 19:21:15
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-29 19:58:24
from typing import Optional
from fastapi import FastAPI
from database import engine
import models
from routers import blog, user, authenticate

# from routers import blogs

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authenticate.router)
app.include_router(blog.router)
app.include_router(user.router)

@app.get('/')
def idex():
    return {"Hello": "Welcome to Project1"}

@app.get('/blogs')
def blogs(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    return {'data': {'blog': {'limit': limit, 'published': published, 'sort': sort}}}

@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10):
    return {'data': {'blog': id, 'comments': {'limit': limit}}}
