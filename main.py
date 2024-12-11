import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

from DSLinkedList import DSLinkedList
from DSLinkedListWE import DSLinkedListWE
from Forest import DSForest
from Graph import Graph


N = 20       # num of vertices
V = 10       # num of edges

g = Graph()

for i in range(N):
    g.add_node(i)

for i in range(V):
    u = random.randint(0,N-1)
    v = random.randint(0,N-1)
    g.add_edge(u, v)

#ds = DSForest()
#ds = DSLinkedList()
ds = DSLinkedListWE()

g.findCC(ds)
print("---")
for edge in g.edges():
    print(edge)