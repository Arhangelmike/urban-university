from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from block17.app2.backend.db import Base
from block17.app2.models.user import User


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    slug = Column(String, unique=True, index=True)
    user = relationship('User', back_populates='tasks')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))