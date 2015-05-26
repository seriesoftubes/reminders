
import flask
import twilio


app = flask.Flask(__name__)
app.config['DEBUG'] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def Hello():
  return 'Hello Twilio version {0}!'.format(twilio.__version__)


@app.errorhandler(404)
def NotFound(e):
  return 'Sorry, nothing at this URL.', 404
