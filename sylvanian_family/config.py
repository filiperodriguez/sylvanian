# config

#configure our database
class Configuration(object):
    DATABASE = {
        'name': 'sylvanian',
        'engine': 'peewee.MySQLDatabase',
        'user': 'sylvanian',
        'passwd': '68zL7VeS0W',
    }
    DEBUG = True
    SECRET_KEY = 'ssshhhh'
