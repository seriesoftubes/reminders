"""Handler functions."""

import twilio

from google.appengine.api import mail

import settings


_TWILIO = settings.SECRETS['twilio']


def _GetTwilioRestClient():
  return twilio.rest.TwilioRestClient(
    _TWILIO['api_user'], _TWILIO['api_secret'])


def Hello():
  client = _GetTwilioRestClient()
  client.messages.create(
    to='+16313531888', from_=_TWILIO['phone_number'], body='Test')
  from_address = _EMAIL_ADDRESS
  to_address = 'brianweiden@gmail.com'
  subject = 'TEST SUBJECT!'
  body = 'Test body!'
  mail.send_mail(from_address, to_address, subject, body)
  return 'message sent...'
