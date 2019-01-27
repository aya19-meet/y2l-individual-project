from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///game.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_recipe(name, description, time, ingredients, vegan=False, breakfast=False, dessert=False, glutenfree=False, quicksnacks=False, keto=False):
	recipe_object = Recipe(
		name=name,
		description=description,
		time=time,
		ingredients=ingredients,
		vegan=vegan,
		breakfast=breakfast,
		dessert=dessert,
		glutenfree=glutenfree,
		quicksnacks=quicksnacks,
		keto=keto)
	print(ingredients)
	print(recipe_object.ingredients)
	session.add(recipe_object)
	session.commit()

#add_recipe("ab","a","a","ab",True,True,True,True,True,True)

def recipe_query_vegan(vegan):

	recipes = session.query(Recipe).filter_by(vegan=True).all()
	return recipes

def recipe_query_breakfast(breakfast):

	recipes = session.query(Recipe).filter_by(breakfast=True).all()
	return recipes

def recipe_query_quicksnacks(quicksnacks):

	recipes = session.query(Recipe).filter_by(quicksnacks=True).all()
	return recipes
   
def recipe_query_keto(keto):

	recipes = session.query(Recipe).filter_by(keto=True).all()
	return recipes

def recipe_query_dessert(dessert):

	recipes = session.query(Recipe).filter_by(dessert=True).all()
	return recipes

def recipe_query_glutenfree(glutenfree):

	recipes = session.query(Recipe).filter_by(glutenfree=True).all()
	return recipes

def recipe_query():
	recipes = session.query(Recipe).all()
	return recipes
