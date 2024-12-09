class DSForest:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
           self.parent[rootY] = rootX

# Esempio di utilizzo
ds = DSForest(5)  # Crea 5 insiemi disgiunti (0, 1, 2, 3, 4)
ds.union(0, 1)  # Unisce gli insiemi contenenti 0 e 1
ds.union(1, 2)  # Unisce gli insiemi contenenti 1 e 2
ds.union(3, 4)
ds.union(0, 4)
print(ds.find(0))  # Output: rappresentante dell'insieme contenente 2 (stesso di 0 e 1)
print(ds.find(1))  # Output: rappresentante dell'insieme contenente 0 (stesso di 2 e 1)
print(ds.find(2))
print(ds.find(3))
print(ds.find(4))
