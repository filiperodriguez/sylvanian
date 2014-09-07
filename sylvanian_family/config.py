# config

#configure our database
class Configuration(object):
    DATABASE = {
        'name': 'sylvanian',
        'engine': 'peewee.MySQLDatabase',
        #'user': 'db_user',
        #'passwd': 'secret password',
    }
    DEBUG = True
    SECRET_KEY = 'ssshhhh'
