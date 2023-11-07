import DSAAS01Class_Sorted as DCLL

def display_menu():
    print("Doubly Circular Linked List Menu")
    print("1. Add Item")
    print("2. Delete")
    print("3. Search")
    print("4. Size Checker")
    print("5. Size Limit Checker")
    print("6. Display")
    print("7. Quit")

def add_item(my_list):
    num = int(input("Enter a number to add to the list: "))
    my_list.addToFront(num)
    print(f"Current size of the list: {my_list.getSize()}")

def delete_menu(my_list):
    print("\nDelete Menu")
    print("1. Delete First Specific Item")
    print("2. Delete All Specific Items")
    print("3. Delete by Index")
    print("4. Back")
    num = int(input("Enter your choice: "))
    
    if num == 1:
        num_to_delete = int(input("Enter the number to delete: "))
        my_list.delete(num_to_delete)
    elif num == 2:
        num_to_delete = int(input("Enter the number to delete: "))
        my_list.deleteAll(num_to_delete)
    elif num == 3:
        index_to_delete = int(input("Enter the index to delete: "))
        my_list.deleteByIndex(index_to_delete)

def search_menu(my_list):
    print("\nSearch Menu")
    print("1. Search Item")
    print("2. Search Index") #search index by items
    print("3. Search by Index") #search items by index
    print("4. Back")
    num = int(input("Enter your choice: "))
    
    if num == 1:
        num_to_search = int(input("Enter the number to search: "))
        my_list.search(num_to_search)
    elif num == 2:
        num_to_search = int(input("Enter the number to search: "))
        my_list.searchIndex(num_to_search)
    elif num == 3:
        index_to_search = int(input("Enter the index to search: "))
        my_list.searchByIndex(index_to_search)

my_list = DCLL.DoublyCircularLinkedList()
my_list.addToFront(16)
my_list.addToFront(2)
my_list.addToFront(5)
my_list.addToFront(6)
my_list.addToFront(1)
my_list.addToFront(5)



while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item(my_list)
    elif choice == 2:
        delete_menu(my_list)
    elif choice == 3:
        search_menu(my_list)
    elif choice == 4:
        print(f"Current size of the list: {my_list.getSize()}")
    elif choice == 5:
        print (f"Current size limit: {my_list.limitChecker()}")
    elif choice == 6:
        my_list.display()
        print ('\n')
    elif choice == 7:
        quit()
    else:
        print("Invalid choice. Please try again.")
