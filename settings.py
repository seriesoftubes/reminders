"""App settings that should never be changed at runtime."""

import json


def _GetAppSecrets():
  with open('secrets.json', 'r') as f:
    return json.loads(f.read())

_SECRETS = _GetAppSecrets()

# All twilio account info, including:
# "phone_number", "api_user", and "api_secret" (the secret key)
TWILIO = _SECRETS['twilio']

# The Google account email address associated with this app.
# Used as the FROM address for reminder emails.
EMAIL_ADDRESS = _SECRETS['email_address']
