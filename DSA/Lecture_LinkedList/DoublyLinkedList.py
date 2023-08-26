class Node:
    def __self__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToFront(self,data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.prev = None

        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            newNode.prev = None

    def removeNodeAtFront(self):
        currentHead = self.head
        currentHead.next.prev = None

        self.head = currentHead.next