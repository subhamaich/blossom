from linked_list import Node, LinkedList
class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    hashcode = self.hash(key)
    array_index = self.compress(hashcode)
    #self.array[array_index] = [key, value]
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for i in list_at_array:
      if i[0] == key:
        i[1] = value
        return
    list_at_array.insert(payload)


  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    '''payload = self.array[array_index]
    if payload != None and payload[0] == key:
      return payload[1]
    else:
      return None'''
    list_at_index = self.array[array_index]
    for i in list_at_index:
      if i[0] == key:
        return i[1]
      else:
        return None
