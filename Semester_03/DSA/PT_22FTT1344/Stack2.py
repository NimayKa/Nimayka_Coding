class Stack2:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


newStack = Stack2()
#add 4,5,6,1,34,5,6
#how do you produce the list using stack (6 should be at the bottom)
newStack.push(4)
newStack.push(5)
print(newStack.is_empty())
print(newStack.peek())
print(newStack.size())
print(newStack.pop())
print(newStack.size())
