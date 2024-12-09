class Node:
    def __init__(self, data):
        self.data = data
        self.root = self
        self.next = None

class DisjointSets:
    def __init__(self, root):
        self.root = root
        self.tail = root

    def length(self):
        current = self.root
        c = 1
        while current != self.tail:
            c += 1
            current = current.next
        return c