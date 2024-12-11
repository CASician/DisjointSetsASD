class DSForest:
    def __init__(self):
        self.parent = {}

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
           self.parent[rootY] = rootX

    def print_sets(self):
        sets = {}
        for x in self.parent:
            root = self.find(x)
            if root not in sets:
                sets[root] = []
            sets[root].append(x)

        for root, members in sets.items():
            print(f"Rappresentante: {root} -> Membri: {members}")

# Esempio di utilizzo
ds = DSForest()
for i in range(10):
    ds.make_set(i)

ds.union(0, 1)
ds.union(2, 3)
ds.union(1, 3)
ds.union(9, 8)
ds.union(4, 5)
ds.union(7, 6)
ds.union(5, 2)
ds.union(9,6)

ds.print_sets()

