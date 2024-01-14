class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head
    self.length = 1

  def append(self, data):
    new_node = Node(data)
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1
    return self

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next

  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self.length += 1
    return self

  def insert(self, index, data):
    if index >= self.length:
      return self.append(data)
    else:
      new_node = Node(data)
      count = 0
      for i in self:
        if count == index-1: # traverse likned list until you find index
          temp = i.next
          i.next = new_node
          new_node.next = temp
          self.length += 1
          break
        count +=1
      return self

  def remove(self, index):
    if index >= self.length:
      return self
    else:
      count = 0
      for i in self:
        if count == index-1:
          temp = i.next
          i.next = temp.next
          self.length -= 1
          break
        count +=1
      return self

  def reverse(self):
    if self.length == 1:
      return self
    else:
      first = self.head
      self.tail = self.head # optional if you are not maintaining head and tail throughtout the code
      second = first.next
      while second is not None:
        third = second.next
        second.next = first
        first = second
        second = third
      self.head.next = None
      self.head = first
      return self

mylinkedlist = LinkedList(10)
mylinkedlist.append(20)
mylinkedlist.append(16)
mylinkedlist.prepend(5)
mylinkedlist.insert(2, 99)
print(mylinkedlist.head)
for i in mylinkedlist:
  print(i.data)
print("Length is: ",mylinkedlist.length)
mylinkedlist.reverse()
for i in mylinkedlist:
  print(i.data)
mylinkedlist.remove(2)
print("=========Removed===========")
print("Length is: ",mylinkedlist.length)
for i in mylinkedlist:
  print(i.data)

