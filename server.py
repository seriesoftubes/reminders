
import flask

import handlers


app = flask.Flask(__name__)
app.config['DEBUG'] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# Routes
app.add_url_rule('/', view_func=handlers.Hello)
app.add_url_rule('/create_person', view_func=handlers.CreatePerson)
app.add_url_rule('/get_people', view_func=handlers.GetAllPeople)
