class Node:

    data = None
    nxt = None

    def __init__(self, data, nxt):
        self.data = data
        self.nxt = nxt

class List:

    head = None

    def __init__(self):
        self.head = None

    def addToFront(self, n):
        n = Node(n, None)

        if self.head:
            n.nxt = self.head

        self.head = n

    def printNodes(self):
        current = self.head
        while current:
            if current.nxt:
                print(current.data, end=',')
            else:
                print(current.data, end='.')
            current = current.nxt

                
