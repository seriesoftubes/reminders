"""Handler functions."""

from flask import jsonify
from flask import request
import twilio

from google.appengine.ext import deferred
from google.appengine.api import mail

import people
import rotation
import settings


_TWILIO = settings.TWILIO


def CreatePerson():
  full_name = request.args['full_name']
  phone_number = request.args['phone_number']
  email_address = request.args['email_address']
  sort_order = request.args['sort_order']
  person, action = people.Upsert(
    full_name=full_name, phone_number=phone_number, email_address=email_address,
    sort_order=sort_order)
  return jsonify(action=action, person=person.to_dict())


def GetAllPeople():
  all_people = [person.to_dict() for person in people.GetAll()]
  return jsonify(people=all_people)


def DeletePerson():
  full_name = request.args['full_name']
  deleted_person = people.Delete(full_name)
  return jsonify(deleted=deleted_person.to_dict())


def ToggleIsInHouse():
  full_name = request.args['full_name']
  person = people.ToggleProperty(full_name, 'is_in_house')
  return jsonify(updated=person.to_dict())


def ToggleCanDoTrash():
  full_name = request.args['full_name']
  person = people.ToggleProperty(full_name, 'can_do_trash')
  return jsonify(updated=person.to_dict())


def _GetTrashPerson():
  trash_people = people.GetTrashPeople()
  index = rotation.GetIndex()
  if index >= len(trash_people):
    rotation.ResetIndex()
    index = 0
  return trash_people[index]


def RotateTrashPerson():
  new_rotation = rotation.IncrementIndex()
  return jsonify(new_index=new_rotation.index)


def _GetTwilioRestClient():
  return twilio.rest.TwilioRestClient(
    _TWILIO['api_user'], _TWILIO['api_secret'])


def _SendPersonalReminder():
  trash_person = _GetTrashPerson()
  sms = _GetTwilioRestClient()

  sms.messages.create(
    to=trash_person.phone_number, from_=_TWILIO['phone_number'],
    body='Please take out the trash tonight!')

  from_address = settings.EMAIL_ADDRESS
  to_address = trash_person.email_address
  subject = 'Please take out the trash tonight'
  body = 'Thanks!'
  mail.send_mail(from_address, to_address, subject, body)


def SendPersonalReminder():
  deferred.defer(_SendPersonalReminder)
  return 'Sending messages...'


def _SendGroupReminder():
  trash_person = _GetTrashPerson()
  sms = _GetTwilioRestClient()

  message = '{} was supposed to take out the trash tonight'.format(
    trash_person.full_name)

  cc_addresses = []
  for person in people.GetHouseDwellers():
    sms.messages.create(
      to=person.phone_number, from_=_TWILIO['phone_number'],
      body=message)
    if person != trash_person:
      cc_addresses.append(person.email_address)

  from_address = settings.EMAIL_ADDRESS
  to_address = trash_person.email_address
  body = 'Please make sure they did it'
  mail.send_mail(
    from_address, to_address, message, body, cc=cc_addresses)


def SendGroupReminder():
  deferred.defer(_SendGroupReminder)
  return 'Sending messages...'
