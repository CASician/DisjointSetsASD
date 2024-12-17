import random
import copy
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

def plot_times_w_ex(ex_time):
    plt.figure(figsize=(10,10))
    x = range(1, len(ex_time)+1)
    plt.plot(x, ex_time, marker='o',linestyle='None', color='blue', label="Tempo di esecuzione")

    x_values = np.linspace(0, V, 500)
    scaling_factor = np.max(ex_time)/np.max(x_values**9)
    y_value = (x_values**9)*scaling_factor
    plt.plot(x_values, y_value, color='r', label="y=n^9", linestyle='-', linewidth=2)

    # Titles and labels
    plt.title("Tempo di esecuzione vs Archi", fontsize=12)
    plt.xlabel("Numero di Archi (E)", fontsize=12)
    plt.ylabel("Tempo di esecuzione (s)", fontsize=12)

    # Griglia e legenda
    #plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=12)

    plt.show()

def plot_times_w_log(ex_time):
    plt.figure(figsize=(10,10))
    x = range(1, len(ex_time)+1)
    plt.plot(x, ex_time, marker='o',linestyle='None', color='blue', label="Tempo di esecuzione")

    x_values = np.linspace(1, V, 500)
    scaling_factor = np.max(ex_time)/np.max(np.log(x_values))
    y_value = (np.log(x_values))*scaling_factor
    plt.plot(x_values, y_value, color='r', label="y=log(x)", linestyle='-', linewidth=2)

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

g1 = copy.deepcopy(g)
g2 = copy.deepcopy(g)

ds = DSLinkedList()
ds_we = DSLinkedListWE()
ds_wf = DSForest()

g.findCC(ds)
g1.findCC(ds_we)
g2.findCC(ds_wf)


# print(min(g.ex_time), max(g.ex_time))
plot_times_w_ex(g.ex_time)
plot_times_w_log(g1.ex_time)
plot_times_w_log(g2.ex_time)

total_time = sum(g.ex_time)
total_time1 = sum(g1.ex_time)
total_time2 = sum(g2.ex_time)

print(f"Tempo totale: {total_time:.3} secondi")
print(f"Tempo totale 1: {total_time1:.3} secondi")
print(f"Tempo totale 2: {total_time2:.3} secondi")
