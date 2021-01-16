from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vladislavbiryukov:@localhost/postgres'
db = SQLAlchemy(app)

from app.models import PyUser

db.drop_all()
db.create_all()

admin = PyUser(username='admin', email='admin@example.com')
guest = PyUser(username='guest', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()

from app import routes