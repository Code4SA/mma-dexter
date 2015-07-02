# mma-dexter

Dexter web app for MMA.

The app is a [Flask web app](http://flask.pocoo.org/) that uses [SQLAlchemy](http://www.sqlalchemy.org/) to talk to a MySQL database.

Please read the wiki for a [full overview of how Dexter works](https://github.com/Code4SA/mma-dexter/wiki).

## Development

* clone the repo
* install a virtual env and activate it: `virtualenv --no-site-packages env; source env/bin/activate`
* install requirements: `pip install -r requirements.txt`
* setup the database:

```bash
mysql -u root
mysql> CREATE DATABASE mma;
mysql> GRANT ALL ON mma.* TO 'mma'@'localhost';
mysql> exit;
```

```python
from dexter.models.support import db
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

Use [nose](https://nose.readthedocs.org/en/latest/):

    nosetests

## Production

Note: if you're on Ubuntu 12.04 you will need to manually [install mysql 5.6](https://rtcamp.com/tutorials/mysql/mysql-5-6-ubuntu-12-04/)

Deploy the code using Fabric:

```
fab prod provision deploy
```

### Database

* Add the DB user: 

```
CREATE DATABASE mma;
GRANT ALL ON mma.* TO 'mma'@'localhost' identified by 'PASSWORD';
GRANT SELECT ON *.* TO 'reports'@'%' identified by 'PASSWORD' require ssl;
GRANT SELECT, LOCK TABLES, SHOW VIEW ON `mma`.* TO 'backup'@'localhost' IDENTIFIED BY 'X2aVljzBeDDm';
```

* restore the database from a backup, if available.
* copy the ssl cert key into /home/mma/mma-dexter/resources/mysql/server-key.pem
* edit my.cnf:

```
default_time_zone = +02:00
...
ssl-ca=/home/mma/mma-dexter/resources/mysql/ca-cert.pem
ssl-cert=/home/mma/mma-dexter/resources/mysql/server-cert.pem
ssl-key=/home/mma/mma-dexter/resources/mysql/server-key.pem
```

### Configuration

Create a file for sensitive configuration settings called `production-settings.sh` and the appropriate
configuration entries.

```bash
export SQLALCHEMY_DATABASE_URI=mysql://mma:PASSWORD@localhost/mma
export ALCHEMY_API_KEY=thekey
export CALAIS_API_KEY=anotherkey
export AWS_ACCESS_KEY_ID=access-key
export AWS_SECRET_ACCESS_KEY=secret
export NEWSTOOLS_FEED_PASSWORD=password
```

**Note:** DO NOT commit `production-settings.sh` into source control!

### Logging

nginx's production logs are in ``~mma/log/access.log``

The dexter application logs are in ``~mma/log/dexter.log``


### Deploying changes

To deploy changes to the service,

* make the changes elsewhere, commit to git and push to github
* `fab prod deploy`

### Deploying database changes

Dexter uses [Flask-Migrate](https://flask-migrate.readthedocs.org/en/latest/) (which uses Alembic) to handle database migrations.

To add a new model or make changes, update the SQLAlchemy definitions in `dexter/models/`. Then run

    python app.py db migrate --message "a description of your change"

This will autogenerate a change. Double check that it make sense. To apply it on your machine, run

    python app.py db upgrade head

To deploy it remotely, ensure it is committeed and pushed, then run:

    fab production deploy migrate restart

## Database

The server expects MySQL 5.6 because it uses the CURRENT_TIMESTAMP default value
on a DATETIME column, [as described here](http://shankargopal.blogspot.com/2013/03/mysql-566-timestamp-columns-and-default.html).
This means on some systems you'll need to [upgrade from 5.5 to 5.6](https://rtcamp.com/tutorials/mysql/mysql-5-6-ubuntu-12-04/).
