from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath

app.config['SECRET_KEY'] = 'donttellanyone'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hayde:haz@localhost/hazraps'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)