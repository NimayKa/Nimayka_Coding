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

    def insert_node(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def remove_node(self, item):
        current = self.head
        while current:
            if current.data == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                    self.head.prev = None
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                    self.tail.next = None
                self.size -= 1
                return
            current = current.next

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def is_empty(self):
        return self.head is None

    def get_size(self):
        return self.size

    def append_end(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def index(self, item):
        current = self.head
        position = 0
        while current:
            if current.data == item:
                return position
            current = current.next
            position += 1
        return None

    def insert_pos(self, pos, item):
        if pos == 0:
            self.insert_node(item)
        else:
            current = self.head
            position = 0
            new_node = Node(item)
            while current:
                if position == pos - 1:
                    new_node.prev = current
                    new_node.next = current.next
                    if current.next:
                        current.next.prev = new_node
                    current.next = new_node
                    self.size += 1
                    return
                current = current.next
                position += 1

    def pop(self, pos):
        if pos == 0:
            if self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                self.size -= 1
        else:
            current = self.head
            position = 0
            while current:
                if position == pos:
                    if current.prev:
                        current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                    self.size -= 1
                    return
                current = current.next
                position += 1

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


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert_node(9)
doubly_linked_list.insert_node(10)
doubly_linked_list.insert_node(11)

print("Forward:")
doubly_linked_list.display_forward()

print("\nBackward:")
doubly_linked_list.display_backward()


print("\nSearch:")
print(doubly_linked_list.search(11))
print(doubly_linked_list.search(8))

print("\nCheck Empty:")
print(doubly_linked_list.is_empty())

print("\nGet Size:")
print(doubly_linked_list.get_size())

print("\nAppend End:")
doubly_linked_list.append_end(8)
doubly_linked_list.display_forward()
doubly_linked_list.display_backward()

print("\nIndex:")
print(f'Index of Item 8: {doubly_linked_list.index(8)}')

print("\nInsert Position:3")
doubly_linked_list.insert_pos(3, 13)
doubly_linked_list.display_forward()
doubly_linked_list.display_backward()
print("\nInsert Position:1")
doubly_linked_list.insert_pos(1, 7)
doubly_linked_list.display_forward()
doubly_linked_list.display_backward()

print("\nPop:")
doubly_linked_list.pop(2)
doubly_linked_list.display_forward()
doubly_linked_list.display_backward()

print("\nPop:")
doubly_linked_list.pop(10)
doubly_linked_list.display_forward()
doubly_linked_list.display_backward()
