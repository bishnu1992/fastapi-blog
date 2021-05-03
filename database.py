# -*- coding: utf-8 -*-
# @Author: bishnu
# @Date:   2021-04-21 18:00:41
# @Last Modified by:   Bishnu
# @Last Modified time: 2021-05-03 19:31:12
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@192.168.1.8:3306/fastapi_blog"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
