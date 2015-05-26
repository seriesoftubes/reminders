
import json

import flask
import twilio


app = flask.Flask(__name__)
app.config['DEBUG'] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


def _GetAppSecrets():
  with open('secrets.json', 'r') as f:
    return json.loads(f.read())


@app.route('/')
def Hello():
  secrets = _GetAppSecrets()
  return 'Hello secrets! {}'.format(secrets)


@app.errorhandler(404)
def NotFound(e):
  return 'Sorry, nothing at this URL.', 404
