class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class orderedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next
        return False
    
    def add(self, item):
        new_node = Node(item)
        previous = None
        current = self.head
        while current is not None and current.data < item:
            previous = current
            current = current.next
        if previous is None:
            new_node.next = self.head
            self.head = new_node
        else:
            previous.next = new_node
            new_node.next = current
    
    def search_position(self, item):
        current = self.head
        position = 0
        while current is not None:
            position += 1
            if current.data == item:
                return position
            if current.data > item:
                break
            current = current.next
        return f"{item} is not found after {position} iterations"
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=", ")
            current = current.next
        print()

ordered_list = orderedList()
items = [22, 23, 24, 37, 40, 60]

for item in items:
    ordered_list.add(item)

print("Items in list:", end=" ")
ordered_list.display()

print("Add(50)")
ordered_list.add(50)

print("New List:", end=" ")
ordered_list.display()

print("Search(38)")
print(ordered_list.search(38))

print("SearchPosition(38)")
print(ordered_list.search_position(38))

print("Search(23)")
print(ordered_list.search(23))

print("SearchPosition(23)")
print(ordered_list.search_position(23))


