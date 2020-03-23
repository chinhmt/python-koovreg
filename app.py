from koovreg import create_app
from multiprocessing.pool import ThreadPool

service_ports = [
  '8000',  # port for testing service 1
  '8080',  # port for testing service 2
]

app = create_app(service_ports)
app.pool = ThreadPool(3)
