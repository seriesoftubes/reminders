"""Manages ppl in the commune."""

from google.appengine.ext import ndb


_US_PHONE_NUMBER_PREFIX = '+1'


class Person(ndb.Model):
  name = ndb.StringProperty(required=True)
  phone_number = ndb.StringProperty(required=True)
  email_address = ndb.StringProperty(required=True)
  sort_order = ndb.IntegerProperty(required=True)

  def __str__(self):
    return '<Person {}>'.format(self.__dict__)


def _GetDigits(string):
  return ''.join(int(s) for s in string.split() if s.isdigit())


def _GetPhoneNumber(raw_phone_number):
  if raw_phone_number.startswith(_US_PHONE_NUMBER_PREFIX):
    raw_phone_number = raw_phone_number[len(_US_PHONE_NUMBER_PREFIX):]
  return _US_PHONE_NUMBER_PREFIX + _GetDigits(raw_phone_number)


def Create(name, phone_number, email_address, sort_order):
  phone_number = _GetPhoneNumber(phone_number)
  person = Person(name, phone_number, email_address, sort_order)
  person.put()
  return person


def GetAll():
  return Person.query().order(Person.sort_order)
