"""Rotating the current trash person."""

from google.appengine.ext import ndb


class RotationIndex(ndb.Model):
  index = ndb.IntegerProperty(required=True, default=0)


def _GetRotation():
  return RotationIndex.query().get()


def GetIndex():
  return _GetRotation().index


def ResetIndex():
  """At read time, if it's > len(people), run this function."""
  rotation = _GetRotation()
  rotation.index = 0
  rotation.put()
  return rotation


def IncrementIndex():
  rotation = _GetRotation()
  rotation.index += 1
  rotation.put()
  return rotation


if not _GetRotation():
  RotationIndex(index=0).put()
