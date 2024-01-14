class Node:

  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

  def __repr__(self):
    return str(self.data)


class BinaryTree:

  def __init__(self):
    self.root = None

  def insert(self, data):
    new_node = Node(data)
    if self.root == None:
      self.root = new_node
    else:
      current_node = self.root
      while True:
        if data < current_node.data:
          if current_node.left == None:
            current_node.left = new_node
            return self
          current_node = current_node.left
        if data > current_node.data:
          if current_node.right == None:
            current_node.right = new_node
            return self
          current_node = current_node.right

  def lookup(self, data):
    if self.root == None:
      return "No Tree"
    else:
      current_node = self.root
      while(current_node is not None):
        if (current_node.data == data):
          return "Found"
        elif (data < current_node.data):
          current_node = current_node.left
        elif (data > current_node.data):
          current_node = current_node.right
      return "Not Found"

  # def remove():

mytree = BinaryTree()
mytree.insert(50)
mytree.insert(60)
mytree.insert(30)
mytree.insert(20)
print(mytree.lookup(70))

print(mytree.root)
print(mytree.root.right)
print(mytree.root.left)
print(mytree.root.left.left)