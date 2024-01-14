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
      while(current_node.left != new_node) and (current_node.right != new_node):
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

  def DFS_in_order(self):
    return self.traverse_in_order(self.root, [])

  def traverse_in_order(self, current_node, list):
    if current_node.left is not None:
      self.traverse_in_order(current_node.left, list)
    list.append(current_node.data)
    if(current_node.right is not None):
      self.traverse_in_order(current_node.right, list)
    return list

  def DFS_pre_order(self):
    return self.traverse_pre_order(self.root, [])

  def traverse_pre_order(self, current_node, list):
    list.append(current_node.data)
    if current_node.left is not None:
      self.traverse_pre_order(current_node.left, list)
    if(current_node.right is not None):
      self.traverse_pre_order(current_node.right, list)
    return list

  def DFS_post_order(self):
    return self.traverse_post_order(self.root, [])

  def traverse_post_order(self, current_node, list):
    if current_node.left is not None:
      self.traverse_post_order(current_node.left, list)
    if(current_node.right is not None):
      self.traverse_post_order(current_node.right, list)
    list.append(current_node.data)
    return list

my_bst = BST()
my_bst.insert(9)
my_bst.insert(4)
my_bst.insert(20)
my_bst.insert(1)
my_bst.insert(6)
my_bst.insert(15)
my_bst.insert(170)
print()
print("In Order", my_bst.DFS_in_order())
print()
print("Pre Order", my_bst.DFS_pre_order())
print()
print("Post Order",my_bst.DFS_post_order())