class DisjointSetForest:
    def __init__(self, size):
        # Inizializzazione: ogni elemento è il proprio genitore (capo) e il rango è zero
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        # Trova il rappresentante dell'insieme a cui appartiene x con compressione del cammino
        if self.parent[x] != x:
            # Comprimi il percorso puntando il genitore al rappresentante
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Unisce gli insiemi contenenti x e y
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Unione basata sul rango (o altezza dell'albero)
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                # Se hanno lo stesso rango, scegli uno come nuovo capo e incrementa il suo rango
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Esempio di utilizzo
ds = DisjointSetForest(5)  # Crea 5 insiemi disgiunti (0, 1, 2, 3, 4)
ds.union(0, 1)  # Unisce gli insiemi contenenti 0 e 1
ds.union(1, 2)  # Unisce gli insiemi contenenti 1 e 2
print(ds.find(2))  # Output: rappresentante dell'insieme contenente 2 (stesso di 0 e 1)
print(ds.find(0))  # Output: rappresentante dell'insieme contenente 0 (stesso di 2 e 1)
