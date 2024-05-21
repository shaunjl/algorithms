"""
Graphs

https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38

The easiest way to represent a graph is just by a list of the edges but searching this list is O(E) where E is the number of edges

Instead, use an adjacency matrix. An adjacency matrix is a 2d array with indicies for all the nodes and 1s where the nodes have an edge and 0s where they don't (or other values if it's weighted). This can be a problem, though, when the graph is sparse. In that case you end up taking up a lot of space for nothing.

To solve the problem with adjacency matricies, make an adjacency list. This is a list where each of the indicies represents a node and holds a linked list or list representing it's immediate neighbors

https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.attributes = {}  # Dictionary to store additional attributes

    def __repr__(self):
        return f"Node({self.value})"


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)  # For undirected graph

    def display(self):
        for node, neighbors in self.adjacency_list.items():
            neighbor_values = [neighbor.value for neighbor in neighbors]
            print(f"{node.value}: {neighbor_values}")

# Example usage:
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')

graph = Graph()
graph.add_node(node_a)
graph.add_node(node_b)
graph.add_edge(node_a, node_b)
graph.add_edge(node_a, node_c)
graph.add_edge(node_b, node_c)
graph.add_edge(node_c, node_d)
graph.display()
