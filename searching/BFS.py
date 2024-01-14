class Node():

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BST():

  def __init__(self):
    self.root = None
    self.number_of_nodes = 0

  def insert(self, data):
    new_node = Node(data)
    if self.root == None:
      self.root = new_node
      self.number_of_nodes += 1
      return
    else:
      current_node = self.root
      while (current_node.left != new_node) and (current_node.right !=
                                                 new_node):
        if new_node.data > current_node.data:
          if current_node.right == None:
            current_node.right = new_node
          else:
            current_node = current_node.right
        elif new_node.data < current_node.data:
          if current_node.left == None:
            current_node.left = new_node
          else:
            current_node = current_node.left
      self.number_of_nodes += 1
      return

  def BFS(self):
    current_node = self.root
    list = []
    queue = []
    queue.append(current_node)
    while(len(queue) > 0):
      current_node = queue.pop(0)
      list.append(current_node.data)
      if current_node.left is not None:
        queue.append(current_node.left)
      elif current_node.right is not None:
        queue.append(current_node.right)
    return list


my_bst = BST()
my_bst.insert(9)
my_bst.insert(4)
my_bst.insert(20)
my_bst.insert(1)
my_bst.insert(6)
my_bst.insert(15)
my_bst.insert(170)
