
import json

import flask
import twilio

from google.appengine.api import mail


# TODO: try to put this stuff into if __name__ == '__main__'
app = flask.Flask(__name__)
app.config['DEBUG'] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

def _GetAppSecrets():
  with open('secrets.json', 'r') as f:
    return json.loads(f.read())
_SECRETS = _GetAppSecrets()['twilio']

_EMAIL_ADDRESS = 'reminders@commune-2-0.com'


def _GetTwilioRestClient():
  return twilio.rest.TwilioRestClient(
    _SECRETS['api_user'], _SECRETS['api_secret'])


@app.route('/')
def Hello():
  client = _GetTwilioRestClient()
  client.messages.create(
    to='+16313531888', from_=_SECRETS['phone_number'], body='Test')
  from_address = _EMAIL_ADDRESS
  to_address = 'brianweiden@gmail.com'
  subject = 'TEST SUBJECT!'
  body = 'Test body!'
  mail.send_mail(from_address, to_address, subject, body)
  return 'message sent...'


@app.errorhandler(404)
def NotFound(e):
  return 'Sorry, nothing at this URL.', 404
