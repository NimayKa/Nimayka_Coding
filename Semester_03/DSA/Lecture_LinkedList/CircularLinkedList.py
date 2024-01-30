class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToFront(self,data):
        if self.last == None: 
            newNode = Node(data)
            self.last=newNode
            self.last.next = self.last
            return self.last
        else: 
            newNode = Node(data)
            newNode.next = self.last.next
            self.last.next =newNode

    def traverse(self):
        if self.last == None:
            print ("Empty")
        else:
            current = self.last.next

            while current is not None:
                print (current.data,end='->')
                current = current.next
                if current == self.last.next:
                    break

mylist = CircularLinkedList()
mylist.addToFront(2)
mylist.addToFront(4)
mylist.addToFront(6)
mylist.addToFront(8)
mylist.addToFront(10)
mylist.traverse()