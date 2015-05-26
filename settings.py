"""App settings that should not ever be changed at runtime."""


EMAIL_ADDRESS = 'reminders.commune2.0@gmail.com'


def _GetAppSecrets():
  with open('secrets.json', 'r') as f:
    return json.loads(f.read())

SECRETS = _GetAppSecrets()
