from flask import Flask


def create_app(service_ports):
  app = Flask(__name__)

  import koovreg.general.controllers as general
  import koovreg.register.controllers as register

  register.service_ports = ','.join(service_ports)

  app.register_blueprint(general.module)
  app.register_blueprint(register.module)

  return app
