from app import app
from app import db
from flask import render_template
from app.models import PyUser

# import sqlalchemy



@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/pyuser')
@app.route('/pyuser/<name>')
def pyuser(name=None):
    pyusers = PyUser.query.all()
    return render_template('pyuser.html', name=name, pyusers=pyusers)




