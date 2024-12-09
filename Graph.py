class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if (node1 in self.graph and node2 in self.graph
                and
                node1 not in self.graph[node2] and node2 not in self.graph[node1]
                and node1 != node2
        ):
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def print(self):
        for node, neighbours in self.graph.items():
            print(f"{node} : {neighbours}")


g = Graph()
for i in range(5):
    g.add_node(i)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print()
