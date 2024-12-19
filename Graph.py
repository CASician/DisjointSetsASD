from DSLinkedList import DSLinkedList
from DSLinkedListWE import DSLinkedListWE
from Forest import DSForest
from timeit import default_timer as timer


class Graph:
    def __init__(self):
        self.graph = {}
        self.edges_list = set()  # Usare un set per evitare duplicati
        self.ex_time = []

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if (node1 in self.graph and node2 in self.graph
                and node1 != node2):
            edge = tuple(sorted((node1, node2)))  # Gli archi sono non orientati
            if edge not in self.edges_list:
                self.edges_list.add(edge)
                self.graph[node1].append(node2)
                self.graph[node2].append(node1)

    def edges(self):
        return self.edges_list

    def findCC(self, ds):
        for node in self.graph:
            ds.make_set(node)
        for edge in self.edges():
            start = timer()
            node1, node2 = edge
            ds.union(node1, node2)
            end = timer()
            self.ex_time.append(round(end - start, 9))


    def print(self):
        for node, neighbours in self.graph.items():
            print(f"{node} : {neighbours}")


"""
g = Graph()
for i in range(5):
    g.add_node(i)
g.add_edge(0, 1)
#g.add_edge(0, 2)
#g.add_edge(1, 2)
#g.add_edge(2, 0)
g.add_edge(2, 3)
#g.add_edge(3, 4)
#g.print()

#for edge in g.edges():
 #   print(edge)

ds = DSLinkedListWE()
g.findCC(ds)
"""