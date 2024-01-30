def factorial(num):

    if num ==  1:
        return num
    else:
        return num * factorial(num-1)

inum = int(input("Enter the number: "))
fact = factorial(inum)
print (fact)