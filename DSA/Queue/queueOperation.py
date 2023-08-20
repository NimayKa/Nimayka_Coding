class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        return self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def remmoveAtIndex(self, index):
        self.items.remove(index)
    
    def size(self):
        
        return len(self.items)
    
    def printQueue(self):
        print(self.items)