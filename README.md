# mma-dexter

[![Build Status](https://travis-ci.org/Code4SA/mma-dexter.svg)](http://travis-ci.org/Code4SA/mma-dexter)

Dexter web app for MMA.

The app is a [Flask web app](http://flask.pocoo.org/) that uses [SQLAlchemy](http://www.sqlalchemy.org/) to talk to a MySQL database.

Please read the wiki for a [full overview of how Dexter works](https://github.com/Code4SA/mma-dexter/wiki).

## Development

* clone the repo
* install a virtual env and activate it: `virtualenv --no-site-packages env; source env/bin/activate`
* install requirements: `pip install -r requirements.txt`
* setup the MySQL database (minimum version 5.6.21)

```bash
mysql -u root
mysql> CREATE DATABASE mma;
mysql> GRANT ALL ON mma.* TO 'mma'@'localhost';
mysql> exit;
```

```python
from dexter.models import db
from dexter.models.seeds import seed_db
db.create_all()
seed_db(db)
```

* setup the AlchemyAPI and OpenCalais API keys:

```bash
export ALCHEMY_API_KEY=thekey
export CALAIS_API_KEY=anotherkey
```

* run the server: `python app.py`
* log in as `admin@code4sa.org` with password `admin`
* to add a new article to the database, visit [http://localhost:5000/articles/new] and enter a Mail and Guardian URL.

### Topic Clustering

Dexter needs NumPy, SciPy and scikit-learn to run clustering.

On Mac OS X, we recommend this:

```bash
brew install gcc
pip install scipy
```

## Running Tests

You will need to setup a test database:

```bash
mysql -u root
mysql> CREATE DATABASE mma_test;
mysql> GRANT ALL ON mma.* TO 'mma'@'localhost';
mysql> exit;
```

Then use [nose](https://nose.readthedocs.org/en/latest/) to run tests:

    nosetests

## Production

Dexter runs using [Dokku](http://dokku.viewdocs.io/dokku/), a Docker-based container infrastructure very similar to [Heroku](https://www.heroku.com/)

To deploy your changes, simply `git push dokku` to push to your dokku remote.

To setup a new dokku container:

* Create the app: `dokku app create mma-dexter`
* Configure the app: 

    dokku config:set mma-dexter \
        SQLALCHEMY_DATABASE_URI="mysql://user:pass@host/database?charset=utf8&use_unicode=0" \
        FLASK_ENV=production
        NEW_RELIC_CONFIG_FILE='/app/dexter/config/newrelic.ini'
        NEWSTOOLS_FEED_PASSWORD=newstools-password \
        SENDGRID_API_KEY=sendgrid-api-key \
        ALCHEMY_API_KEY=api-key \
        AWS_ACCESS_KEY_ID=aws-access-key \
        AWS_SECRET_ACCESS_KEY=aws-secret-access-key \
        CALAIS_API_KEY2=calais-api-key-1 \
        CALAIS_API_KEY=calais-api-key-2

* Deploy your code: `git push dokku`

### Database

* Add the DB user: 

```
CREATE DATABASE mma;
GRANT ALL ON mma.* TO 'mma'@'localhost' identified by 'PASSWORD';
```

* restore the database from a backup, if available.

### Deploying database changes

Dexter uses [Flask-Migrate](https://flask-migrate.readthedocs.org/en/latest/) (which uses Alembic) to handle database migrations.

To add a new model or make changes, update the SQLAlchemy definitions in `dexter/models/`. Then run

    python app.py db migrate --message "a description of your change"

This will autogenerate a change. Double check that it make sense. To apply it on your machine, run

    python app.py db upgrade head

## Database

The server expects MySQL 5.6 because it uses the CURRENT_TIMESTAMP default value
on a DATETIME column, [as described here](http://shankargopal.blogspot.com/2013/03/mysql-566-timestamp-columns-and-default.html).
This means on some systems you'll need to [upgrade from 5.5 to 5.6](https://rtcamp.com/tutorials/mysql/mysql-5-6-ubuntu-12-04/).
