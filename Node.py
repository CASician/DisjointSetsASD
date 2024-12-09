class Node:
    def __init__(self, data):
        self.data = data
        self.root = self  # Il capo iniziale è se stesso
        self.next = None  # Puntatore al prossimo elemento nella lista concatenata

class DisjointSets:
    def __init__(self, root):
        self.root = root
        self.tail = root