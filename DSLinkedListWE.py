from Node import Node

class DisjointSetLinkedListWE:
    def __init__(self):
        self.sets = {}

    def make_set(self, data):
        if data not in self.sets:
            self.sets[data] = Node(data)

    def find (self, data):
        if data in self.sets:
            return self.sets[data].root

    def union(self, data1, data2):
        node1 = self.sets[data1]
        node2 = self.sets[data2]

        # Roots
        root1 = node1.root
        root2 = node2.root
        if root1 != root2:
            return

        # Connect lists
        root1.tail.next = root2

        # Correct second List
        current = root2
        while current is not None:
            current.root = root1
            current = current.next

        # Correct first List
        current1 = root1
        newTail = root2.tail
        while current1 is not root2:
            current1.tail = newTail
            current1 = current1.next