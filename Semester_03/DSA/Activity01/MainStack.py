import StackOperation as Sk

myStack = Sk.stack()
print (myStack.is_empty())
myStack.push(4)
myStack.push(5)
myStack.push(6)
myStack.push(1)
myStack.push(34)
myStack.push(5)
myStack.push(6)
print ("Show all")
print (myStack.showall())

print (myStack.peek())

print(myStack.size())
print (myStack.is_empty())

print(myStack.pop())
print(myStack.pop())
print(myStack.size())