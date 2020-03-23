import pickle


def load_objects(file):
  with open(file, 'rb') as f:
    objs = []
    while True:
      try:
        objs.append(pickle.load(f))
      except EOFError:
        break

  return objs


def save_object_with_lock(file, obj, lock):
  with lock:
    with open(file, 'wb') as f:
      pickle.dump(obj, f)
