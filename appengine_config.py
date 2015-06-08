"""This file runs when a new AppEngine instance is started."""

import os

from google.appengine.ext import vendor


# Third-party libraries are stored in "lib", vendoring will make
# sure that they are importable by the application.
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
