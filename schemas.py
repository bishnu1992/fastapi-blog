# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-21 17:31:13
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-30 20:35:37
from pydantic import BaseModel
from typing import Optional, List

class Blog(BaseModel):
    title: str
    body: str
    created_by: int
    published: Optional[bool]
    class Config:
        orm_mode = True

class ShowUserForBlog(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUserForBlog
    class Config:
        orm_mode = True

class StatusBlog(BaseModel):
    published: Optional[bool]
    class Config:
        orm_mode = True
class UpdateBlog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str
    class Config:
        orm_mode = True

class ShowBlogByUser(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True

class ShowUserBlogs(BaseModel):
    name: str
    email: str
    blogs: List[ShowBlogByUser] = []
    class Config:
        orm_mode = True
