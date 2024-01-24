class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:

    def __init__(self):
        self.head = None    

    def is_empty(self):
        return self.head == None

    def add(self, item): #addtofront
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:

            if previous != None:
                print("Previous")
                print(previous.get_data())
            else:
                print("Previous")
                print("None")

            print("Current")
            print(current.get_data())
            print("Next of a current")
            print(current.next.get_data())

            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
                
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def removeAll(self, item):
        current = self.head
        found = None
        while current != None:
            if current.data == item:
                found = True
                previous.next = current.next   
                current = current.next               

            previous = current
            current = current.next
        else:
            if not found:
                return print ('No Item is removed.')
        return

    def searchAll(self, item):
        current = self.head
        i = 0
        found=[]
        while current != None:
            if current.data == item:
                found.append(i)

            i +=1
            current = current.next
        
        if len(found) != 0:
            return print (f'Item(s) found at Position :{found}')
        else:
            return print ('No item is found')
        
    def sum (self):
        current = self.head
        sumoflist = 0

        while current != None:
            sumoflist += current.data
            current = current.next
        return print (f'Sum :{sumoflist}')
        

    def printAll(self):
        current = self.head

        while current != None:
            print(current.get_data(), end=" ")
            current = current.next



mylist = LinkedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.add(6)  
mylist.add(7)
mylist.add(6)
mylist.add(6)
mylist.add(8)
mylist.add(8)  
print(mylist.search(17)) 
mylist.printAll()
mylist.removeAll(6)
mylist.printAll()
mylist.removeAll(9) 
mylist.searchAll(8)
mylist.searchAll(9)
mylist.sum()