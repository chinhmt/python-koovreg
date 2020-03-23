import json
from koovreg.utils import allow_client
from koovreg.utils import get_allowed_clients
from koovreg.utils import save_rule_for_client
from flask import (
  Blueprint,
  abort,
  request,
)


def allow_authenticated_clients():
  for client in allowed_clients:
    allow_client(client)


module = Blueprint('register', __name__, url_prefix='/register')
service_ports = ''

allowed_clients = get_allowed_clients()
allow_authenticated_clients()


@module.route('', methods=['POST'])
def register():
  remote_mac_addr = request.get_json().get('mac')
  for client in allowed_clients:
    if client['mac'] == remote_mac_addr:
      return '', 200

  # will raise a popup windows!
  # allow_client({'mac': remote_mac_addr, 'ports': service_ports})
  # save_rule_for_client({'mac': remote_mac_addr, 'ports': service_ports})

  abort(404)


@module.before_request
def before_register_req():
  if not request.is_json or not request.get_json().get('mac'):
    abort(404)
