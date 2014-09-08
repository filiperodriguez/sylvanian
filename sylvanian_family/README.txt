Sylvanian personal stock control
================================

An application to maintain stock control of Sylvanina's dolls collection

batteries included:

* admin
* auth
* rest api

requirements:

* `flask <https://github.com/mitsuhiko/flask>`_
* `peewee <https://github.com/coleifer/peewee>`_
* `wtforms <https://github.com/wtforms/wtforms>`_
* `wtf-peewee <https://github.com/coleifer/wtf-peewee>`_
* python 2.5 or greater

Admin interface using peewee, more documentation here: <http://flask-peewee.readthedocs.org/>

Initial setup:

python setup.py install
python setup.py test

Create user for admin:

from app(or main in this case) import auth
auth.User.create_table(fail_silently=True)  # make sure table created.
admin = auth.User(username='admin', email='', admin=True, active=True)
admin.set_password('admin')
admin.save()