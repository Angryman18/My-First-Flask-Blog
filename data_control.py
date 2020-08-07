from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

with open('config.json', mode='r') as c:
    params = json.load(c)['params']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = params["local_url"]
db = SQLAlchemy(app)

class Data_control(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    no_of_post = db.Column(db.Integer, nullable=False)
    about = db.Column(db.String(), nullable=True)
    service = db.Column(db.String(), nullable=True)

class Admin(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)




