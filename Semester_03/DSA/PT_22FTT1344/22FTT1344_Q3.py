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
    
    def checker(self,string):
        count=0
        for i in string:
            if i == '*':
                print()
            elif  i.isdigit():
                count+=1
            else:
                Stack2.push(self,i)
        return print (self.items,'\nNumbers in The Sequences is:',count)

    
newStack = Stack2()
string  = '2POL2*L*TEK3***NIK***BRU*NEI***'
newStack.checker(string)
print ('Top of the stack is',newStack.pop())
