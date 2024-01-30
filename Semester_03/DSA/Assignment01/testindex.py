
def binary_search (a_list, its):
    low = 0
    high = len(a_list) - 1

    found = False
    print ("\n")
    while low  <= high  and not found:

        midpoint = (high + low) // 2
        print (midpoint)
        print ("Midpoint",a_list[midpoint])
        if midpoint == its:
            print(f'Index {its}:{a_list[midpoint]}')
            found = True
        else:
            if its < midpoint:
                print("\nLowering")
                high = midpoint - 1
            else:
                print("\nUpper")
                low = midpoint + 1
        
    return found



arr = [3,5,6,8,11]
num = int(input("Enter Number to Search: "))
print(binary_search(arr,num))
