from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from block17.app2.backend.db import Base
from block17.app2.models import Task
'''Нет в лекции!!!!! 
при импорте файлов учесть, что корнем является ближайшая папка с виртуальным окружением .venv
поэтому путь до файла db.py
не такой    ----    C:\Users\user\PycharmProjects\pythonProject1\block17\app2\backend\db.py
и не такой   ----    app2.backend.db 
а выглядит вот так, в моем случае   ------  block17.app2.backend.db'''
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)


    tasks = relationship('Task', back_populates='user')