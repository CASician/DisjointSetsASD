from Node import NodeLS as Node

class DSLinkedList:
    def __init__(self):
        self.sets = {}

    def make_set(self, data):
        if data not in self.sets:
            node = Node(data)
            self.sets[data] = node

    def find(self, data):
        node = self.sets[data]
        return node.root.data  # Restituisce il "capo" della lista

    def union(self, data1, data2):
        node1 = self.sets[data1]
        node2 = self.sets[data2]

        # Trova i rappresentanti di ciascun insieme
        root1 = node1.root
        root2 = node2.root

        # Se appartengono già allo stesso insieme, non fare nulla
        if root1 == root2:
            return

        root1.tail.next = root2  # Collegamento della lista

        # Aggiustiamo seconda lista
        current = root2
        while current is not None:
            current.root = root1
            current = current.next

        # Aggiustiamo la prima lista
        newTail = root2.tail
        current1 = root1
        while current1 is not root2:
            current1.tail = newTail
            current1 = current1.next

# Esempio di utilizzo
ds = DSLinkedList()
for i in range(10):
    ds.make_set(i)

ds.union(0, 1)  # Unisce gli insiemi contenenti 1 e 2
# ds.union(2, 3)  # Unisce gli insiemi contenenti 3 e 4
ds.union(1, 3)  # Unisce gli insiemi contenenti 2 (che include anche 1) e 3 (che include anche 4)
ds.union(2, 5)
ds.union(4, 6)
ds.union(7, 8)

x = ds.sets

for i in range(10):
    if x[i].next is None:
        print(x[i].data, x[i].root.data, "-", x[i].tail.data)
    else:
        print(x[i].data, x[i].root.data, x[i].next.data, x[i].tail.data)
