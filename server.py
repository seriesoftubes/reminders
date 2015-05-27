"""The Flask server + routes."""

import flask

import handlers


app = flask.Flask(__name__)
app.config['DEBUG'] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# Routes
app.add_url_rule('/cron/send_personal_reminder', view_func=handlers.SendPersonalReminder)
app.add_url_rule('/cron/send_group_reminder', view_func=handlers.SendGroupReminder)
app.add_url_rule('/cron/rotate_trash_person', view_func=handlers.RotateTrashPerson)

app.add_url_rule('/people/create', view_func=handlers.CreatePerson)
app.add_url_rule('/people/list', view_func=handlers.GetAllPeople)
app.add_url_rule('/people/delete', view_func=handlers.DeletePerson)
app.add_url_rule('/people/toggle_is_in_commune', view_func=handlers.ToggleIsInCommune)
app.add_url_rule('/people/toggle_can_do_trash', view_func=handlers.ToggleCanDoTrash)
