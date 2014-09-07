from flask_peewee.admin import Admin

from app import app
from auth import auth
from models import *

admin = Admin(app, auth)
admin.register(Note)
admin.register(Sylvanians)
