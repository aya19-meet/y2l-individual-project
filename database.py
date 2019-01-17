from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_recipe(name, description, time, keyword):
	recipe_object = Recipe(
		name=nam,
		description=description,
		time=time,
		keyword=keyword)
	print(recipe_object)
	session.add(recipe_object)
	session.commit()
   
