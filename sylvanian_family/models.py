import datetime
from peewee import *
from app import db


class Sylvanians(db.Model):
    name = TextField()
    description = TextField()
    category = TextField()
    maker = IntegerField(choices=((1, 'Flair'), (2, 'Epoch UK'), (3, 'Epoch JP'), (4, 'Tomy'), (5, 'Calico Critters')))
    date_purchased = DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.description)