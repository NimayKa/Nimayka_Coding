class todo():
    def __init__(self):
        self.list = []
        self.size = 0
    
    def insert (self,item):
        self.list.append(item)
        self.size +=1
        
    def display(self):
        print("Todo List:")
        for i in self.list:
            print (i)
            
    def recursive(self, index=0):
        if index == len(self.list) - 1:
            return self.list[index]
        else:
            return self.list[index] + ", " + self.recursive(index + 1)

list= todo()
list.insert("Nasi Katok")
list.insert("Maggi")
list.insert("Ice lemon Tea")
list.insert("Sembahyang")
list.insert("Revision")  
list.display()   
print(list.recursive())