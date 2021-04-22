from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask('__name__')

EVN = 'con'
if EVN == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xuboyang:xby1999726@localhost/music'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes
