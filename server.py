
import flask

import handlers


app = flask.Flask(__name__)
app.config['DEBUG'] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# Routes
app.add_url_rule('/', view_func=handlers.Hello)
