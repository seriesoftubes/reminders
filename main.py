
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
_SECRETS = _GetAppSecrets()['twilio']


def _GetTwilioRestClient():
  return twilio.rest.TwilioRestClient(
    _SECRETS['api_user'], _SECRETS['api_secret'])


@app.route('/')
def Hello():
  client = _GetTwilioRestClient()
  client.messages.create(
    to='+16313531888', from_=_SECRETS['phone_number'], body='Test')
  return 'message sent...'


@app.errorhandler(404)
def NotFound(e):
  return 'Sorry, nothing at this URL.', 404
