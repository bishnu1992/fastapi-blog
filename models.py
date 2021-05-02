# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-21 18:14:05
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-27 19:14:16
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250))
    body = Column(Text)
    created_by = Column(Integer, ForeignKey('users.id'))
    published = Column(Boolean)

    creator = relationship('User', back_populates="blogs")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))

    blogs = relationship('Blog', back_populates="creator")
