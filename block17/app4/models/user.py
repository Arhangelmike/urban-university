from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import relationship
from block17.app4.backend.db import Base
from block17.app4.models.task import Task
# возможно надо но не факт   ---    from block17.app4.models import *


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user', cascade='all')

# from sqlalchemy.schema import CreateTable
# print(CreateTable(User.__table__))
