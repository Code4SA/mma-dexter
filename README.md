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

* clone the repo
* install a virtual env and activate it: `virtualenv --system-site-packages env; source env/bin/activate`
* install egg in dev mode: `python setup.py develop`

Setup the database. Set the database URL as an environment variable:

```bash
export SQLALCHEMY_URL=mysql://mma:PASSWORD@localhost/mma
```

To create the db from scratch, run

```
initialize_dexter_db development.ini
```

or restore it from a backup.

To start the server,

```bash
pserve production.ini
```

## Database

The server expects MySQL 5.6 because it uses the CURRENT_TIMESTAMP default value
on a DATETIME column, [as described here](http://shankargopal.blogspot.com/2013/03/mysql-566-timestamp-columns-and-default.html).
This means on some systems you'll need to upgrade from 5.5 to 5.6.
