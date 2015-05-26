
from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def Hello():
  """Return a friendly HTTP greeting."""
  return 'Hello World!'


@app.errorhandler(404)
def NotFound(e):
  return 'Sorry, nothing at this URL.', 404

