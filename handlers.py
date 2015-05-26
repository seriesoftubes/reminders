"""Handler functions."""

import logging

from flask import jsonify
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
  full_name = request.args['full_name']
  phone_number = request.args['phone_number']
  logging.info('RAW phone number: {}'.format(phone_number))
  email_address = request.args['email_address']
  sort_order = request.args['sort_order']
  person, action = people.Upsert(
    full_name=full_name, phone_number=phone_number, email_address=email_address,
    sort_order=sort_order)
  return jsonify(action=action, person=person.to_dict())


def GetAllPeople():
  all_people = [person.to_dict() for person in people.GetAll()]
  logging.info('person0: {}'.format(all_people[0]))
  logging.info('got %d people', len(all_people))
  return jsonify(people=all_people)


def DeletePerson():
  full_name = request.args['full_name']
  deleted_person = people.Delete(full_name)
  return jsonify(deleted=deleted_person.to_dict())
