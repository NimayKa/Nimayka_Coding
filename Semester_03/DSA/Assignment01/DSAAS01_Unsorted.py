import DSAAS01Class_Unsorted as DCLL

#function for Each Menu

mylist = DCLL.DoublyCircularLinkedList()
num  = int(input("1. Add Item "))
mylist.addToFront(num)
mylist.addToFront(2)
mylist.addToFront(5)
mylist.addToFront(2)
mylist.addToFront(5)
print(mylist.getSize())
print ("Doubly Circular Linked List Menu")
while True:
    ip = int(input("1. Add Item \
                   \n2. Delete \
                   \n3. Search Item\n4. Search Index\
                   \n5. Search by Index\n6. Size Checker\
                   \n7. Size Limit Checker \
                   \n8. Quit \n"))
    if ip == 2:
        print ("\nDelete Menu")
        ip2= int (input ("1. Delete First Specific Item\
                         \n2. Delete All Specific Item\
                         \n3. Delete by Index \
                         \n4. Back"))
    elif ip == 10:
        quit()

