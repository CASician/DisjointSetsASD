import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

from DSLinkedList import DSLinkedList
from DSLinkedListWE import DSLinkedListWE
from Forest import DSForest
from Graph import Graph


N = 100000     # num of vertices
V = 70000       # num of edges

def plot_times(ex_time):
    plt.figure(figsize=(10,10))
    x = range(1, len(ex_time)+1)
    plt.plot(x, ex_time, marker='o',linestyle='None', color='blue', label="Tempo di esecuzione")

    sf = N/V
    x_values = np.linspace(0, V, 500)
    scaling_factor = np.max(ex_time)/np.max(x_values**2)
    y_value = (x_values**2)*scaling_factor
    plt.plot(x_values, y_value, color='r', label="y=n^2", linestyle='-', linewidth=2)

    # Titles and labels
    plt.title("Tempo di esecuzione vs Archi", fontsize=12)
    plt.xlabel("Numero di Archi (E)", fontsize=12)
    plt.ylabel("Tempo di esecuzione (s)", fontsize=12)

    # Griglia e legenda
    #plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=12)

    plt.show()

g = Graph()

for i in range(N):
    g.add_node(i)

for i in range(V):
    u = random.randint(0,N-1)
    v = random.randint(0,N-1)
    g.add_edge(u, v)

#ds = DSForest()
ds = DSLinkedList()
#ds = DSLinkedListWE()

g.findCC(ds)


# print(min(g.ex_time), max(g.ex_time))
plot_times(g.ex_time)