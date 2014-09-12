# New relic must be initialized before Flask is loaded
import newrelic.agent
import os
newrelic.agent.initialize('dexter/config/newrelic.ini',
                          os.environ.get('FLASK_ENV', 'development'))


from dexter.core import app

if __name__ == '__main__':
    app.debug = True
    app.run()
