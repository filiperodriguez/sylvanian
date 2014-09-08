from flask import Flask
from flask_peewee.db import Database


app = Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)

def create_tables():
    Sylvanians.create_table()