from Node import Node, DisjointSets

class DSLinkedList:
    def __init__(self):
        self.nodes = {}
        self.sets = {}

    def make_set(self, data):
        node = Node(data)
        self.nodes[data] = node
        self.sets[data] = DisjointSets(node)

    def find(self, data):
        if data not in self.nodes:
            return None
        node = self.nodes[data]
        return node.root

    def union(self, data1, data2):
        # Roots & Sets
        root1 = self.find(data1)
        root2 = self.find(data2)

        set1 = self.sets[root1.data]
        set2 = self.sets[root2.data]

        # Same set
        if root1 == root2 or not root1 or not root2:
            return

        # Link the sets
        set1.tail.next = root2

        # Update the second set
        current = root2
        while current:
            current.root = root1
            if current.next is None:
                set1.tail = current
            current = current.next

        # Delete second set
        del self.sets[root2.data]

    def print_sets(self):
        for key, disjoint_set in self.sets.items():
            print(f"Set Root: {disjoint_set.root.data}, Tail: {disjoint_set.tail.data}")
            current = disjoint_set.root
            members = []
            while current:
                members.append(current.data)
                current = current.next
            print("Members:", ", ".join(map(str, members)))
            print("---")

# Debug
"""
ds = DSLinkedList()
for i in range(10):
    ds.make_set(i)

ds.union(0, 1)
ds.union(2, 3)
ds.union(1, 3)
ds.union(9, 8)
ds.union(4, 5)
ds.union(7, 6)
ds.union(5, 2)

ds.print_sets()
"""