class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def remove_at_index(self, index):
        if index < len(self.items):
            self.items.pop(index)
    
    def size(self):
        return len(self.items)
    
    def print_queue(self):
        print(self.items)