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
                print("Item not found in the list.")
                break

    #Deletes all the specified item inside the list.
    def deleteAll(self, item):
        if self.head is None:
            print("Empty list. Cannot delete items.")
            return

        current = self.head

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
            if current == self.head:
                break

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
                return True

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
                return index

            current = current.next
            index += 1
            if current == self.head:
                break
        return None
    
    def binary_search (a_list, its):
        low = 0
        high = len(a_list) - 1

        found = False
        print ("\n")
        while low  <= high  and not found:

            midpoint = (high + low) // 2
            print (midpoint)
            print ("Midpoint",a_list[midpoint])
            if a_list[midpoint] == its:
                found = True
            else:
                if its < a_list[midpoint]:
                    print("\nLowering")
                    high = midpoint - 1
                else:
                    print("\nUpper")
                    low = midpoint + 1
        return found

    
    #Returns the value at the specific index.
    def searchByIndex(self, index):
        
        if self.head is None:
            print("Empty list. Invalid index.")
            return None

        if index < 0 or index >= self.size:
            print("Invalid index.")
            return None

        current = self.head
        count = 0

        while True:
            if count == index:
                return current.data

            current = current.next
            count += 1
            if current == self.head:
                break

        return None
    
    #Returns the current size of the list.
    def getSize(self):
        return self.size
    
    def display(self):
        if not self.head:
            return
        
        current = self.head
        while True:
            print (current.data, end= "->")
            current= current.next
            if current ==self.head:
                break
            print ("->",end ="")
