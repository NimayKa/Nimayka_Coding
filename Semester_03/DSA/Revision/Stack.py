class stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        self.size+=1
    
    def pop(self):
        self.size-=1
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def get_size(self):
        return self.size
    
    def showall(self):
        i = self.size-1
        print ('\n')
        while i>-1 :
          print (f'Index: {i} = {self.items[i]}')
          i -=1
        
Stack=stack()
print(Stack.is_empty())
Stack.push(1)
Stack.push(8)
Stack.push(5)
Stack.push(4)
Stack.push(3)
print(Stack.is_empty())
Stack.showall()
Stack.pop()
Stack.showall()
print ('\n stack size')
print(Stack.get_size())
print ('\n stack peek')
print(Stack.peek())

