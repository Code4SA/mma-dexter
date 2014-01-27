# mma-dexter

Dexter web app for MMA.

The app is a [Pyramid web app](http://www.pylonsproject.org/) that uses [SQLAlchemy](http://www.sqlalchemy.org/) to talk to a MySQL database.

## Development

* clone the repo
* install a virtual env and activate it: `virtualenv --no-site-packages env; source env/bin/activate`
* install egg in dev mode: `python setup.py develop`
* setup the database: `initialize_dexter_db development.ini`
* run the server: `pserve development.ini --reload`

## Production

TODO
