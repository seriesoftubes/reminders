"""Manages ppl in the commune."""

from google.appengine.ext import ndb


ACTION_CREATE = 'create'
ACTION_UPDATE = 'update'

_US_PHONE_NUMBER_PREFIX = '+1'


class Person(ndb.Model):
  full_name = ndb.StringProperty(required=True)
  phone_number = ndb.StringProperty(required=True)
  email_address = ndb.StringProperty(required=True)
  sort_order = ndb.IntegerProperty(required=True)

  def __str__(self):
    return '<Person {}>'.format(self.to_dict())

  __repr__ = __str__

  @classmethod
  def GetByFullName(cls, full_name):
    return cls.query().filter(cls.full_name == full_name).get()


def _LowerStrip(string):
  return string.lower().strip()


def _GetDigits(string):
  return ''.join(s for s in string if s.isdigit())


def _GetPhoneNumber(raw_phone_number):
  if raw_phone_number.startswith(_US_PHONE_NUMBER_PREFIX):
    raw_phone_number = raw_phone_number[len(_US_PHONE_NUMBER_PREFIX):]
  return _US_PHONE_NUMBER_PREFIX + _GetDigits(raw_phone_number)


def Upsert(full_name, phone_number, email_address, sort_order):
  full_name = _LowerStrip(full_name)
  email_address = _LowerStrip(email_address)
  phone_number = _GetPhoneNumber(phone_number)
  sort_order = int(sort_order)

  person = Person.GetByFullName(full_name)
  if person:
    action = ACTION_UPDATE
    person.phone_number = phone_number
    person.email_address = email_address
    person.sort_order = sort_order
  else:
    action = ACTION_CREATE
    person = Person(
      full_name=full_name, phone_number=phone_number, email_address=email_address,
      sort_order=sort_order)

  person.put()
  return person, action


def Delete(full_name):
  full_name = _LowerStrip(full_name)
  person = Person.GetByFullName(full_name)
  person.key.delete()
  return person


def GetAll():
  return Person.query().order(Person.sort_order).fetch()
