from Node import Node, DisjointSets

class DSLinkedListWE:
    def __init__(self):
        self.nodes = {}
        self.sets = {}

    def make_set(self, data):
        if data not in self.nodes:
            node = Node(data)
            self.nodes[data] = node
            self.sets[data] = DisjointSets(node)

    def find (self, data):
        if data in self.nodes:
            return self.nodes[data].root

    def union(self, data1, data2):
        # Roots & Sets
        root1 = self.find(data1)
        root2 = self.find(data2)

        set1 = self.sets[root1.data]
        set2 = self.sets[root2.data]

        # Same set
        if root1 == root2 or not root1 or not root2:
            return

        # Heuristic: the smallest list gets updated
        if set1.length() >= set2.length():
            s_root = root2
            largest = set1
            l_root = root1
        else:
            s_root = root1
            largest = set2
            l_root = root2

        # Link the lists
        largest.tail.next = s_root

        # Update the smallest list
        current = s_root
        while current:
            current.root = l_root
            if current.next is None:
                largest.tail = current
            current = current.next

        # Delete the smallest list
        del self.sets[s_root.data]


# Debug
ds = DSLinkedListWE()
for i in range(10):
    ds.make_set(i)

ds.union(0, 1)
ds.union(2, 3)
ds.union(1, 3)
ds.union(9, 8)
ds.union(4, 5)
ds.union(7, 6)
ds.union(5, 2)
ds.union(6, 2)

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