from flask import Flask, render_template, url_for, redirect, request, session
from flask import session as login_session
from database import *

app = Flask(__name__)

app.secret_key = "secret_key"


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe_route():
    if(request.method == 'GET'):
        return render_template("addrecipe.html")
    else:                                                          
        name = request.form['name']
        description = request.form['description'] 
        time = request.form['time']
        add_event(name, description, time, keywords, ingredients)

if __name__ == '__main__':
    app.run(debug=True)

