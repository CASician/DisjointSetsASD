class NodeLS:
    def __init__(self, value):
        self.value = value
        self.parent = self  # Il capo iniziale è se stesso
        self.next = None  # Puntatore al prossimo elemento nella lista concatenata
        self.tail = self  # Puntatore alla coda della lista
