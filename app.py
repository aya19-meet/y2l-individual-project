from flask import Flask, render_template, url_for, redirect, request, session
from flask import session as login_session
from database import *

app = Flask(__name__)

app.secret_key = "secret_key"


@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe_route():
    print(request.method)
    if(request.method == 'GET'):
        return render_template("addrecipe.html")
    else: 
        name = request.form['name']
        description = request.form['description'] 
        time = request.form['time']
        ingredients = request.form['ingredients']
        print(request)
        if 'vegan' in request.form:
            vegan = True
        else:
            vegan = False
        if 'breakfast' in request.form:
            breakfast = True
        else: 
            breakfast = False
        if 'quicksnacks' in request.form:
            quicksnacks = True
        else:
            quicksnacks = False

        if 'glutenfree' in request.form:
            glutenfree = True
        else: 
            glutenfree = False
        if 'dessert' in request.form:
            dessert = True
        else: 
            dessert = False
        if 'keto' in request.form:
            keto = True
        else: 
            keto = False
        add_recipe(name, description, time, ingredients, vegan, breakfast, dessert, glutenfree, quicksnacks, keto)
        return render_template("home.html")

@app.route('/vegan')
def vegan():
    recipes=recipe_query_vegan(vegan)
    return render_template('vegan.html', recipes=recipes)

@app.route('/breakfast')
def breakfast():
    recipes=recipe_query_breakfast(breakfast)
    return render_template('breakfast.html', recipes=recipes)

@app.route('/dessert')
def dessert():
    recipes=recipe_query_dessert(dessert)
    return render_template('dessert.html', recipes=recipes)

@app.route('/glutenfree')
def glutenfree():
    recipes=recipe_query_glutenfree(glutenfree)
    return render_template('glutenfree.html', recipes=recipes)

@app.route('/quicksnacks')
def quicksnacks():
    recipes=recipe_query_quicksnacks(quicksnacks)
    return render_template('quicksnacks.html', recipes=recipes)

@app.route('/discover')
def discover():
    recipes=recipe_query()
    return render_template('discover.html', recipes=recipes)




if __name__ == '__main__':
    app.run(debug=True)

