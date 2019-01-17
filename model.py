from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Recipe(Base):
    __tablename__ = 'recipes'
    _id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    time = Column(String)
    keyword = Column(String)