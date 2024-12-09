class NodeLS:
    def __init__(self, data):
        self.data = data
        self.root = self  # Il capo iniziale è se stesso
        self.next = None  # Puntatore al prossimo elemento nella lista concatenata
        self.tail = self  # Puntatore alla coda della lista
