class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self  # Il capo iniziale è se stesso
        self.next = None  # Puntatore al prossimo elemento nella lista concatenata
        self.tail = self  # Puntatore alla coda della lista

class DisjointSetLinkedList:
    def __init__(self):
        self.sets = {}

    def make_set(self, data):
        if data not in self.sets:
            node = Node(data)
            self.sets[data] = node

    def find(self, data):
        node = self.sets[data]
        return node.parent.data  # Restituisce il "capo" della lista

    def union(self, data1, data2):
        node1 = self.sets[data1]
        node2 = self.sets[data2]

        # Trova i rappresentanti di ciascun insieme
        root1 = node1.parent
        root2 = node2.parent

        # Se appartengono già allo stesso insieme, non fare nulla
        if root1 == root2:
            return

        # Unisce l'insieme di root2 alla coda dell'insieme di root1
        root1.tail.next = root2  # Collegamento della lista
        root1.tail = root2.tail  # Aggiorna la coda

        # Imposta il parent di tutti gli elementi in root2 per puntare a root1
        current = root2
        while current is not None:
            current.parent = root1
            current = current.next

# Esempio di utilizzo
ds = DisjointSetLinkedList()
ds.make_set(1)
ds.make_set(2)
ds.make_set(3)
ds.make_set(4)

ds.union(1, 2)  # Unisce gli insiemi contenenti 1 e 2
ds.union(3, 4)  # Unisce gli insiemi contenenti 3 e 4
ds.union(2, 3)  # Unisce gli insiemi contenenti 2 (che include anche 1) e 3 (che include anche 4)

print(ds.find(4))  # Output: il rappresentante dell'insieme (sarà 1 dopo le unioni)
