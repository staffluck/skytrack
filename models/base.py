from sqlalchemy import Column, Integer

from db.base import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)