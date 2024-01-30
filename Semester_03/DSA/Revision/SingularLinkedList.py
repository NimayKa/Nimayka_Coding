class Node:
     def __init__ (self,node):
        self.data = node
        self.next = None

class SingularLinkedList :

    def __init__(self):
        self.head  = None
        self.size = 0
    
    def InsertNode (self, newnode):
        new_node = Node(newnode)
        if self.head == None:
            self.head = new_node
            print ('test')
            self.size +=1
            return
        
        current = self.head
        self.head = new_node
        self.head.next = current
        self.size +=1
        
                
    def RemoveNode (self,item):
        
        current = self.head
        if self.head == None:
            return print ("No Item inside the list")

        if current.data == item :
            self.head = self.head.next
            self.size -=1
            return
            
        while current.data != item:
            print (current.data,"Here")
            prev = self.head
            current = current.next
            print (current.data,"Here1")
        else:
            prev.next = current.next
            self.size -=1
            return
        
    def Search (self,item):
        current = self.head

        while current != None:
            if current.data == item:
                return True
            else:
                current = current.next
        else:
            return False
            
    def is_empty(self):
        if self.head ==None:
            return True
        else:
            return False
    
    def GetSize(self):
        return print(self.size)
            
    #append at end
    def appendend (self, item):
        current = self.head
        while current.next != None:
            current =current.next
        else:
            new_node = Node(item)
            current.next = new_node

    #index - returning position
    def index (self,item):
        position = 0
        current = self.head

        while current != None:
            if current.data == item:
                return position
            
            current = current.next
            position +=1
        else:
            return print ("No item in the list")
        
    #insert using position
    def insertpos(self, pos, item):
        current = self.head
        position = 0
        newnode = Node(item)

        if pos == 0:
            newnode.next = self.head
            self.head = newnode
            return

        while current != None:
            if position == pos - 1:
                newnode.next = current.next
                current.next = newnode
                return
            else:
                current = current.next
                position += 1  
        else:
            return print("Position isnt in the list")  
        
    #pop - remove using index
    def pop (self,pos):
        current = self.head
        position = 0

        if pos == 0:
            self.head = self.head.next
            return

        while current != None:
            if position == pos - 1:
                current.next = current.next.next
                return
            else:
                current = current.next
                position += 1
        else:
            return print("Position isnt in the list")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


SLL = SingularLinkedList()

# Insert
print ('\nInsert Infront')
SLL.InsertNode(9)
SLL.InsertNode(10)
SLL.InsertNode(11)

#Display
print ('\nDisplay')
SLL.display()

#Remove
print ('\n Remove')
SLL.RemoveNode(10)
SLL.display()
SLL.RemoveNode(11)
SLL.display()
SLL.InsertNode(10)
SLL.InsertNode(11)

#Search
print ('\n Search')
SLL.display()
print(SLL.Search(11))
print(SLL.Search(9))
print(SLL.Search(8)) 

#Check Empty or not
print ('\nCheck Empty')
print(SLL.is_empty())

#Check Size
print ('\n Get Size')
SLL.GetSize()      

#Append End
print ('\nAppend at the end')
SLL.appendend(8)
SLL.display()

#Index
print ('\nIndex')
print(f'Index of Item {8}: {SLL.index(8)}')

#Insert using Index
print ('\nInsertPosition')
SLL.insertpos(3,13)
SLL.display()
SLL.insertpos(1,7)
SLL.display()

#POP
print ('\nPOP')
SLL.pop(2)
SLL.display()

#POP
print ('\nPOP')
SLL.pop(10)
SLL.display()