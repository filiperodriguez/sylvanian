from flask import Flask
from flask_peewee.db import Database


app = Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)

def create_tables():
    Sylvanians.create_table()
    Note.create_table()


#instantiate the DB wrapper
#db = Database(app)



#admin.setup()

#if __name__ == '__main__':
    #app.run()