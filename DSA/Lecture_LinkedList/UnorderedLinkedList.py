class Node:
    def __init__(self,data):
        self.data = data # the data of the node
        self.next = None #Reference to next node  

    #method to get the data held by the node
    def get_data(self):
        return self.data
    
    #method to get the node located next to the current node
    def get_next(self):
        return self.next
    
    #method to set the data for this current node
    def set_data (self, new_data):
        self.data = new_data

    #method to set the next node for this current node
    def set_next(self, next_node):
        self.next = next_node

class unorderedLL:
    #constructor to create new linked list
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self,item):
        #temporary node
        temp = Node(item)
        #Set current head as next node
        temp.set_next(self.head)

        #Set temp as new head
        self.head = temp

    #method to print all data in every note in the linkedlisted
    def showall(self):

        if self.head is None:
            print ("Linked List is empty")
        
        currentnode = self.head

        dataStr  = ""

        while currentnode is not None:
            data = currentnode.get_data()
            dataStr += str(data) + "-"
            currentnode = currentnode.get_next() # or currentnode.next

        dataStr += "Null"
        return dataStr
    
    def removeNodeBasedOnData(self,dataToRemove):

        currentNode = self.head
        previousNode = None
        found = False

        while not found:
            if currentNode.get_data() == dataToRemove:
                found = True
            else:
                previousNode = currentNode
                currentNode = currentNode.get_next()

        if previousNode is None:
            self.head = currentNode.get_next()
        else:
            previousNode.set_next(currentNode.get_next())

    #method to remove a node based on its index location

    def removeNodeByIndex(self,idx):
        #if user want to remove node at index 0
        if idx == 0:
            self.head = self.head.next
        else:
            currentNode = self.head
            currIdx = 0
            while currentNode is not None:
                if currIdx  == idx - 1:
                    currentNode.next = currentNode.next.next
                currentNode = currentNode.get_next()
                currIdx += 1



ull = unorderedLL()
print(ull.is_empty()) #False
ull.add("Y")
ull.add("u")
ull.add("h")
ull.add("m")
ull.add("e")
ull.add("e")
ull.add("n")
print(ull.is_empty()) #True
print(ull.showall())
ull.removeNodeBasedOnData("e")
print(ull.showall())
