"""Handler functions."""

from flask import request
import twilio

from google.appengine.api import mail

import people
import settings


_TWILIO = settings.SECRETS['twilio']


def _GetTwilioRestClient():
  return twilio.rest.TwilioRestClient(
    _TWILIO['api_user'], _TWILIO['api_secret'])


def Hello():
  client = _GetTwilioRestClient()
  client.messages.create(
    to='+16313531888', from_=_TWILIO['phone_number'], body='Test')
  from_address = settings.EMAIL_ADDRESS
  to_address = 'brianweiden@gmail.com'
  subject = 'TEST SUBJECT!'
  body = 'Test body!'
  mail.send_mail(from_address, to_address, subject, body)
  return 'message sent...'


def CreatePerson():
  name = request.args['name']
  phone_number = request.args['phone_number']
  email_address = request.args['email_address']
  sort_order = int(request.args['sort_order'])
  person = people.Create(name, phone_number, email_address, sort_order)
  return str(person)


def GetAllPeople():
  return str(people.GetAll())
