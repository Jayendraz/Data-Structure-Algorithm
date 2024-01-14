# Dijkstra's algo is useful to find shortest path in weighted graph. 
# Time Complexity: O(E log V) where, E -> edges and V -> nodes (Using priority queue for optimum run time efficiency)
# Space Complexity: O(V+E)

from typing import DefaultDict
import sys
import heapq

class Graph():
  def __init__(self):
    self.nodes = []
    self.edges = DefaultDict(dict)
    self.distances = {}

  def add_node(self, value):
    self.nodes.append(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node][to_node] = distance
    self.edges[to_node][from_node] = distance

  def dijkstra(self, graph, src, dest):
    infinite = sys.maxsize
    node_data = DefaultDict(dict)

    for node in graph.nodes:
      node_data[node]['cost'] = infinite
      node_data[node]['path'] = []

    node_data[src]['cost'] = 0
    visited = []
    current_node = src

    while graph.edges:
      if current_node is dest:
        return (node_data[current_node]['cost'], node_data[current_node]['path'] + list(dest))
      if current_node not in visited:
        visited.append(current_node)
        min_heap = []
        for neighbour in graph.edges[current_node]:
          if neighbour not in visited:
            #calculate cost
            new_cost = node_data[current_node]['cost'] + graph.edges[current_node][neighbour]
            if new_cost < node_data[neighbour]['cost']:
              node_data[neighbour]['cost'] = new_cost
              node_data[neighbour]['path'] = node_data[current_node]['path'] + list(current_node)
            heapq.heappush(min_heap, (node_data[neighbour]['cost'], neighbour))
        heapq.heapify(min_heap)
        current_node = min_heap[0][1]

graph2 = {
  'A':{'B':2, 'C':4},
  'B':{'A':2, 'C':3, 'D':8},
  'C':{'A':4, 'B':3, 'E':5, 'D':2},
  'D':{'B':8, 'C':2, 'E':11, 'F': 12},
  'E':{'C':5, 'D':11, 'F':1},
  'F':{'D':22, 'E':1}
}

graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')

graph.add_edge('A', 'B', 2)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'D', 8)
graph.add_edge('C', 'D', 2)
graph.add_edge('C', 'E', 5)
graph.add_edge('D', 'E', 11)
graph.add_edge('E', 'F', 1)
graph.add_edge('D', 'F', 22)

src = 'A'
dest = 'F'
print(graph.dijkstra(graph, src, dest))

