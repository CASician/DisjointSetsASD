from Node import Node, DisjointSets


class DSLinkedList:
    def __init__(self):
        self.nodes = {}
        self.sets = {}

    def make_set(self, data):
        node = Node(data)
        self.nodes[data] = node
        a_set = DisjointSets(node)
        self.sets[data] = a_set

    def find(self, data):
        if data not in self.nodes:
            return None
        node = self.nodes[data]
        return node.root

    def union(self, data1, data2):
        # Trova i rappresentanti di ciascun insieme
        root1 = self.find(data1)
        root2 = self.find(data2)

        set1 = self.sets[root1.data]
        set2 = self.sets[root2.data]

        # Se appartengono già allo stesso insieme, non fare nulla
        if root1 == root2 or not root1 or not root2:
            return

        # Collegamento delle liste
        set1.tail.next = root2

        # Aggiustiamo prima lista


        # Aggiustiamo seconda lista
        current = set2.root
        while current:
            current.root = root1
            if current.next is None:
                set1.tail = current
            current = current.next

        # Delete second list
        del self.sets[root2.data]


# Esempio di utilizzo
ds = DSLinkedList()
for i in range(10):
    ds.make_set(i)

ds.union(0, 1)
ds.union(2, 3)
ds.union(1, 3)
#ds.union(9, 8)
#ds.union(4, 5)
#ds.union(7, 6)
#ds.union(5, 2)

for i in range(10):
    if i in ds.sets:
        x = ds.sets[i].root
        print("r: " + str(ds.sets[i].root.data) + " t:" + str(ds.sets[i].tail.data))
        while x is not None:
            print(x.data)
            x = x.next
        print("---")
    else:
        print("Deleted")
        print("---")