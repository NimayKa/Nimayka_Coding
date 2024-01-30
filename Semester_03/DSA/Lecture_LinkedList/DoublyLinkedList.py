class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size +=1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size +=1

    def removeNode (self,item):
        current = self.head
        if self.head == item:
            self.head.next = current.next.next
            self.head = current
            return
        
        while current.data != item:
            current = current.next
        else: 
            current.prev = current.prev.prev
            current.next = current.next.next
            print (current.data,item)

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

    
DLL = DoublyLinkedList()
DLL.append(10)
DLL.append(11)
DLL.append(13)
DLL.display_forward()
DLL.display_backward()
DLL.removeNode(11)
DLL.display_forward()
DLL.display_backward()