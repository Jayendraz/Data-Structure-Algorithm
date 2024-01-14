class Graph:

  def __init__(self):
    self.number_of_nodes = 0
    self.adjacency_list = {}

  def add_node(self, node):
    if node not in self.adjacency_list:
      self.adjacency_list[node] = []
      self.number_of_nodes += 1
      return
    return "Node already exists"

  def add_edge(self, node1, node2):
    if node2 not in self.adjacency_list[node1]:
      self.adjacency_list[node1].append(node2)
      self.adjacency_list[node2].append(node1)
      return
    return "Nodes are already connected"


  def show_connections(self):
    print(self.adjacency_list)
    for node, edges in enumerate(self.adjacency_list):
      print(node, "-->", self.adjacency_list[edges])



mygraph = Graph()
mygraph.add_node(0)
mygraph.add_node(1)
mygraph.add_node(2)
mygraph.add_node(3)
mygraph.add_node(4)
mygraph.add_node(5)
mygraph.add_node(6) 

mygraph.add_edge(0, 1)
mygraph.add_edge(0, 2)
mygraph.add_edge(1, 3)
mygraph.add_edge(2, 4)
mygraph.add_edge(3, 4)
mygraph.add_edge(4, 5)
mygraph.add_edge(5, 6)


mygraph.show_connections()


