
import flask

import handlers


def _ConfigureRoutes(app):
  app.add_url_rule('/', view_func=handlers.Hello)


def main():
  app = flask.Flask(__name__)
  app.config['DEBUG'] = True
  # Note: We don't need to call run() since our application is embedded within
  # the App Engine WSGI application server.
  _ConfigureRoutes(app)

if __name__ == '__main__':
  main()
