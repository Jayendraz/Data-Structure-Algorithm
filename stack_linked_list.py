class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:

  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def push(self, data):
    new_node = Node(data)
    if self.length == 0:
      self.top = new_node
      self.bottom = new_node
    else:
      holding_node = self.top
      self.top = new_node
      self.top.next = holding_node
    self.length += 1
    return self

  def __iter__(self):
    node = self.top
    while node is not None:
      yield node
      node = node.next

  def pop(self):
    if self.top is None:
      return None
    elif self.top is self.bottom:
      self.boottom = None
    else:
      holding_node = self.top
      self.top = self.top.next
      self.length -= 1
      return holding_node

  def peek(self):
    return self.top


mystack = Stack()
mystack.push('google')
mystack.push('udemy')
mystack.push('youtube')
for i in mystack:
  print(i.data)
print("Length is: ", mystack.length)
print(mystack.peek().data)

popped = mystack.pop()
print(popped.data)

print(mystack.peek().data)