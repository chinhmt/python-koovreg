import iptc
import multiprocessing
from .storage import load_objects
from .storage import save_object_with_lock

lock = multiprocessing.Lock()
storage_file = '/etc/koovreg.pkl'


def save_rule_for_client(client):
  save_object_with_lock(storage_file, client, lock)


def get_allowed_clients():
  # object's format: {'mac': '11:22:33:44:55:66', 'ports': 'port1,port2'}
  clients = load_objects(storage_file)
  for client in clients:
    if ('mac' not in client) or ('ports' not in client):
      clients.remove(client)
      continue

  return clients


def allow_client(client):
  rule = iptc.Rule()
  rule.protocol = "tcp"
  rule.target = iptc.Target(rule, "ACCEPT")

  match = iptc.Match(rule, "mac")
  match.mac_source = client['mac']
  rule.add_match(match)

  match = iptc.Match(rule, "multiport")
  match.dports = client['ports']
  rule.add_match(match)

  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
  chain.insert_rule(rule)
