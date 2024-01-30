
def binary_search (a_list, its):
    low = 0
    high = len(a_list) - 1

    found = False
    print ("\n")
    while low  <= high  and not found:

        midpoint = (high + low) // 2
        print (midpoint)
        print ("Midpoint",a_list[midpoint])
        if a_list[midpoint] == its:
            found = True
        else:
            if its < a_list[midpoint]:
                print("\nLowering")
                high = midpoint - 1
            else:
                print("\nUpper")
                low = midpoint + 1
        
    return found



arr = [3,5,6,8,11,12,14,15,17,18]
num = int(input("Enter Number to Search: "))
print(binary_search(arr,num))
