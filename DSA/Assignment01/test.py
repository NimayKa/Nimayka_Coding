import DSAAS01Class_Unsorted as DCLL

def Menu(argument):
    match argument:
        case 1:
            num = int(input("Enter Numbers To add into List: "))
            mylist.addToFront(num)
            print(mylist.getSize())
            return
        case 2:
            print ("\nDelete Menu")
            num = int (input ("1. Delete First Specific Item \n2. Delete All Specific Item \n3. Delete by Index \n4. Back"))
            delete(num)
            return
        case 3:
            print ("\nSearch Menu")
            num = int(input("1. Search Item \n2. Search Index \n3. Search by Index \n4. Back"))
            search(num)
            return
        case 4:
            mylist.getSize()
            print('\n')
            return
        case 5:
            mylist.size_limit()
            print('\n')
            return
        case 6:
            mylist.display()
            print('\n')
            return
        case 7:
            quit()
        case default:
            return "Error Output"
        
def delete(argument):
    num = int (input ("Enter number to Delete: \n"))
    
    match argument:
        case 1:
            mylist.delete(num)
            return
        case 2:
            mylist.deleteAll(num)
            return
        case 3:
            mylist.deleteByIndex(num)
            return
        case 4:
            return
        case default:
            return "Error Output"

def search(argument):
    num = int (input ("Enter number to Search: \n"))
    match argument:
        case 1:
            mylist.search(num)
            return
        case 2:
            mylist.searchIndex1(num)
            return
        case 3:
            mylist.searchByIndex(num)
            return
        case 4:
            return
        case default:
            return "Error Output"

     
  
mylist = DCLL.DoublyCircularLinkedList()
mylist.addToFront(2)

while True:
    print ("Doubly Circular Linked List Menu")
    print (("1. Add Item \n2. Delete \n3. Search \n4. Size Checker \n5. Size Limit Checker \n6. Dispaly \n7. Quit \n"))
    num = Menu(int(input("Enter Menu Numbers: ")))
    print(num)