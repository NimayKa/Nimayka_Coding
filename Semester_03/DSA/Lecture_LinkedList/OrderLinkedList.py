class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
class orderedLinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def search(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next
        return False
    
    def add(self, new_data):
        add_node = Node(new_data)
        previous = None
        current = self.head
        
        while current != None and current.data < new_data: 
            previous = current
            current = current.next
        if previous == None:
            add_node.next = self.head
            self.head = add_node
        else:
            previous.next = add_node
            add_node.next = current
        
    def display(self):
        current = self.head
        while current != None:
            print(current.data, end=',')
            current = current.next
        print()
        
    def SearchPosition(self,item):
        current = self.head
        position = 0
        while current != None:
            position += 1
            if current.data == item:
                return position
            if current.data > item:
                break
            current = current.next 
        print(item, 'is not found after', position, 'iterations.')

ordered_list = orderedLinkedList()        
list = [22,23,24,37,40,60]
print('Items in list:', list)

for item in list:
    ordered_list.add(item)
    
print('\nAdding 50 in list:')
ordered_list.add(50)
print('Items in list:')
ordered_list.display()

print('\nSearching for 38 in list:')
print(ordered_list.search(38))

print('\nSearching position of 38 in list:')
ordered_list.SearchPosition(38)

print('\nSearching for 23 in list:')
print(ordered_list.search(23))

print('\nSearching position of 23 in list:')
print(ordered_list.SearchPosition(23))