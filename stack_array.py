class Stack:

  def __init__(self):
    self.array = []

  def push(self, data):
    self.array.append(data)
    return self

  def pop(self):
    return self.array.pop()

  def peek(self):
    return self.array[len(self.array)-1]


mystack = Stack()
mystack.push('google')
mystack.push('udemy')
mystack.push('youtube')
print(mystack.array)
print("Length is: ", len(mystack.array))
print(mystack.peek())

mystack.pop()
print(mystack.array)

print(mystack.peek())