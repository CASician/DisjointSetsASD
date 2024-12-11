class Node:
    def __init__(self, data):
        self.data = data
        self.root = self
        self.next = None

class DisjointSets:
    def __init__(self, root):
        self.root = root
        self.tail = root
        self.length = 1
