class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertNode(self,item):
        newNode = Node(item)
        
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
            self.size +=1
            return 

        current = self.head

        if current.next != self.head:
            current= current.next
        current.next = newNode
        newNode.next = self.head

    def display(self):
        if not self.head:
            print("Empty Circular Linked List")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(" (Head)")

CLL = CircularLinkedList()
CLL.insertNode(5)
CLL.insertNode(5)
CLL.display()

