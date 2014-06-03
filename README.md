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

## Production

Deploy the code using Fabric:

```
fab prod deploy
```

### Database

* setup the database by [installing mysql 5.6](https://rtcamp.com/tutorials/mysql/mysql-5-6-ubuntu-12-04/)
* Add the DB user: 

```
CREATE DATABASE mma;
GRANT ALL ON mma.* TO 'mma'@'localhost' identified by 'PASSWORD';
GRANT SELECT ON *.* TO 'reports'@'%' identified by 'PASSWORD' require ssl;
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
```

**Note:** DO NOT commit `production-settings.sh` into source control!

### Database backups

* Install s3cmd: `sudo apt-get install s3cmd`
* Setup the s3 creds: `s3cmd --configure`
* Install the crontab: `crontab -i resources/cron/backups.crontab`

#### Restoring from backups

* download the latest backup:

```
s3cmd get `s3cmd ls --recursive s3://mma-dexter-backups/mysql- | tail -1 | awk '{print $4}'`
```

* extract and restore

```
gunzip -c BACKUP-FILE | mysql -u mma -p mma
```

### Logging

nginx's production logs are in ``~mma/log/access.log``

The dexter application logs are in ``~mma/log/dexter.log``


### Deploying changes

To deploy changes to the service,

* make the changes elsewhere, commit to git and push to github
* `fab prod deploy`

## Database

The server expects MySQL 5.6 because it uses the CURRENT_TIMESTAMP default value
on a DATETIME column, [as described here](http://shankargopal.blogspot.com/2013/03/mysql-566-timestamp-columns-and-default.html).
This means on some systems you'll need to [upgrade from 5.5 to 5.6](https://rtcamp.com/tutorials/mysql/mysql-5-6-ubuntu-12-04/).
