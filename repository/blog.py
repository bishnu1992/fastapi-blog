# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-29 17:36:52
# @Last Modified by:   bishnu
# @Last Modified time: 2021-04-29 19:03:00
from fastapi import Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
import models

def create(request, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body, published = request.published, created_by = request.created_by)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'No blog found')
    return blog

# def show(id: int, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         response.status_code = status.HTTP_404_NOT_FOUND
#     return {'data': {'blog': blog}}

# def update_blog(id: int, request: schemas.UpdateBlog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if blog.first():
#         # blog.update(request)
#         blog.update({'title': request.title})
#         db.commit()
#         db.refresh(blog.first())
#         return blog.first()
#     else:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'No blog found')

#     return {'data': {'message': 'Blog Updated'}}

def update_blog(id: int, request, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog.first():
        blog.update({'title':request.title, 'body':request.body})
        db.commit()
        db.refresh(blog.first())
        return blog.first()
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'No blog found')

def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog.count():
        blog.delete(synchronize_session = False)
        db.commit()
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'No blog found')

