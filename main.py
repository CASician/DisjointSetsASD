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


N = 1000     # num of vertices
V = 500        # num of edges


def correct(a, b, c):
    mx = max(len(a), len(b), len(c))
    # per il primo
    if mx != len(a):
        dif = mx-len(a)
        for i in range(dif):
            a.append(0)
    # per il secondo
    if mx != len(b):
        dif = mx-len(b)
        for i in range(dif):
            b.append(0)
    # per il terzo
    if mx != len(c):
        dif = mx-len(c)
        for i in range(dif):
            c.append(0)

def plot_times_w_ex(ex_time, ex_time1, ex_time2):
    plt.figure(figsize=(10,10))
    correct(ex_time, ex_time1, ex_time2)
    x = range(1, len(ex_time)+1)
    plt.plot(x, ex_time, marker='o',linestyle='None', color='blue', label="Tempo di esecuzione 1")
    plt.plot(x, ex_time1, marker='o', linestyle='None', color='lightblue', label="Tempo di esecuzione 2")
    plt.plot(x, ex_time2, marker='o', linestyle='None', color='cyan', label="Tempo di esecuzione 3")

    x_values = np.linspace(0, V, len(ex_time))
    scaling_factor = np.max(ex_time)/np.max(x_values**2)
    y_value = (x_values**2)*scaling_factor
    plt.plot(x_values, y_value, color='r', label="y=n^2", linestyle='-', linewidth=2)

    # Titles and labels
    plt.title("Tempo di esecuzione vs Archi", fontsize=12)
    plt.xlabel("Numero di Archi (E)", fontsize=12)
    plt.ylabel("Tempo di esecuzione (s)", fontsize=12)

    # Griglia e legenda
    plt.legend(fontsize=12)

    plt.show()

def plot_times_w_log(ex_time, ex_time1, ex_time2):
    plt.figure(figsize=(10,10))
    correct(ex_time, ex_time1, ex_time2)
    x = range(1, len(ex_time)+1)
    plt.plot(x, ex_time, marker='o',linestyle='None', color='blue', label="Tempo di esecuzione 1")
    plt.plot(x, ex_time1, marker='o', linestyle='None', color='lightblue', label="Tempo di esecuzione 2")
    plt.plot(x, ex_time2, marker='o', linestyle='None', color='cyan', label="Tempo di esecuzione 3")

    # Asymptotic growth
    x_values = np.linspace(1, V, len(ex_time))
    scaling_factor = np.max(ex_time)/np.max(np.log(x_values))
    y_value = (np.log(x_values))*scaling_factor/3
    plt.plot(x_values, y_value, color='r', label="y=log(x)", linestyle='-', linewidth=2)


    # Titles and labels
    plt.title("Tempo di esecuzione vs Archi", fontsize=12)
    plt.xlabel("Numero di Archi (E)", fontsize=12)
    plt.ylabel("Tempo di esecuzione (s)", fontsize=12)

    # Griglia e legenda
    plt.legend(fontsize=12)

    plt.show()

gg = []
gg1 = [None]*3
gg2 = [None]*3
for i in range(3):
    gg.append(Graph())

    for j in range(N):
        gg[i].add_node(j)

    for j in range(V):
        u = random.randint(0,N-1)
        v = random.randint(0,N-1)
        gg[i].add_edge(u, v)

    gg1[i] = copy.deepcopy(gg[i])
    gg2[i] = copy.deepcopy(gg[i])

    ds = DSLinkedList()
    ds_we = DSLinkedListWE()
    ds_wf = DSForest()

    gg[i].findCC(ds)
    gg1[i].findCC(ds_we)
    gg2[i].findCC(ds_wf)


# print(min(g.ex_time), max(g.ex_time))
plot_times_w_ex(gg[0].ex_time, gg[1].ex_time, gg[2].ex_time)
plot_times_w_log(gg1[0].ex_time, gg1[1].ex_time, gg1[2].ex_time)
plot_times_w_log(gg2[0].ex_time, gg2[1].ex_time, gg2[2].ex_time)

#total_time = sum(g.ex_time)
#total_time1 = sum(g1.ex_time)
#total_time2 = sum(g2.ex_time)

#print(f"Tempo totale: {total_time:.3} secondi")
#print(f"Tempo totale 1: {total_time1:.3} secondi")
#print(f"Tempo totale 2: {total_time2:.3} secondi")
