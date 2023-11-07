class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.size_limit = 10

    #Adds a new node to the front of the list.
    def addToFront(self, data):
        if self.size >= self.size_limit:
            print("Size limit reached. Cannot add more items.")
            return 

        newNode = Node(data)

        if self.head is None:   
            self.head = newNode
            self.tail = newNode
            self.head.next = self.head
            self.head.prev = self.head 
        else:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode
        self.size += 1

    #Deletes the first item of the specified item from the list.
    def delete(self, item):
        if self.head is None:
            print("Empty list. Cannot delete item.")
            return

        current = self.head
        if self.size == 1 and current.data == item:
            self.head = None
            self.tail = None
            self.size = 0
            return

        while True:

            if current.data == item:
                current.prev.next = current.next
                current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.size -= 1
                break

            current = current.next
            if current == self.head:
                return print("Item not found in the list.")

    #Deletes all the specified item inside the list.
    def deleteAll(self, item):
        if self.head is None:
            print("Empty list. Cannot delete items.")
            return

        current = self.head
        orihead = self.head

        while True:
            if current.data == item:
                current.prev.next = current.next
                current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.size -= 1
            current = current.next
            if current.data != item and current == orihead:
                return print("Item inda ada lagi")

                
                
    #Deletes the item at the specified index position.     
    def deleteByIndex(self, index):
        if self.head is None:
            print("Empty list. Cannot delete item.")
            return

        if index < 0 or index >= self.size:
            print("Invalid index.")
            return

        current = self.head
        count = 0

        while True:
            if count == index:
                current.prev.next = current.next
                current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.size -= 1
                break

            current = current.next
            count += 1
            if current == self.head:
                break

    #Returns a boolean result indicating whether the item is found within the list.
    def search(self, item):
        if self.head is None:
            print("Empty list. Item not found.")
            return False

        current = self.head

        while True:
            if current.data == item:
                return print('Search Items is Found')

            current = current.next
            if current == self.head:
                break

        return False

    #Returns the index of the first of the specified item in the list.
    def searchIndex(self, item): 
        if self.head is None:
            print("Empty list. Item not found.")
            return None

        current = self.head
        index = 0

        while True:
            if current.data == item:
                return print(f'Search Item in Index : {index}')
            current = current.next
            index += 1
            if current == self.head:
                return print('Item you try to search is not in the list')
            

    #Returns the value at the specific index.
    def searchByIndex(self, item):
        if self.head is None:
            print("Empty list. Item not found.")
            return None
        
        current = self.head
        index = 0
        list = []
        
        while True:
            list.append(current.data)
            current = current.next
            index+=1
            if current == self.head:
                break
        
        low = 0
        high = len(list)-1
        
        while low <= high and True:
            midpoint = (low + high) // 2
            if midpoint == item:
                print (f'Item in Index :{item} is {list[midpoint]}')
                break
            else:
                if item < midpoint:
                    high = midpoint -1 
                else:
                    low = midpoint + 1
        return 
    
    def limitChecker(self):
        return self.size_limit
    
    #Returns the current size of the list.
    def getSize(self):
        return self.size
    
    def display(self):
        if not self.head:
            return
        
        current = self.head
        while True:
            print (current.data, end="->")
            current= current.next
            if current ==self.head:
                break
