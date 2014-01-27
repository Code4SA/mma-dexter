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

### nginx

Install nginx:

`sudo apt-get install nginx`

Link in the dexter config:

`sudo ln -s /home/mma/mma-dexter/resources/nginx/dexter.conf /etc/nginx/sites-enabled/`

And restart nginx:

`sudo service nginx restart`

### upstart

Tell upstart about the dexter gunicorn server:

```
sudo ln -s /home/mma/mma-dexter/resources/upstart/dexter.conf /etc/init/`
sudo initctl reload-configuration
```

And start it:

``sudo start dexter``

### Logging

nginx's production logs are in ``~mma/log/access.log``

The dexter application logs are in ``~mma/log/dexter.log``

### Deploying changes

To deploy changes to the service,

* make the changes elsewhere and commit to git
* `git pull` on the production server
* tell upstart to restart marley: `sudo restart dexter`

If you have made changes to the nginx config, you'll need to restart nginx too:

`sudo service nginx restart`

## Database

The server expects MySQL 5.6 because it uses the CURRENT_TIMESTAMP default value
on a DATETIME column, [as described here](http://shankargopal.blogspot.com/2013/03/mysql-566-timestamp-columns-and-default.html).
This means on some systems you'll need to upgrade from 5.5 to 5.6.
