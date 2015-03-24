# New relic must be initialized before Flask is loaded
import newrelic.agent
import os
newrelic.agent.initialize('dexter/config/newrelic.ini',
                          os.environ.get('FLASK_ENV', 'development'))

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from dexter.core import app
from dexter.models import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
