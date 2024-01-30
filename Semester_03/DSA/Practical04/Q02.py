def  sequential_search (arr_list,search):
    found = False
    iterations = 1
    for i in range (0,len(arr_list)):
        while search == arr_list[i] and not found: 
            found = True
        iterations = iterations + 1  
        break      
    if found == True:
        print ('%d is found after %d iterations' %(search,iterations))
    else:
        print ('%d is not found after %d iterations' %( search,iterations))
    return

    
arr_list = [1, 2, 3, 4, 5, 7]
num = int(input("Enter the numbers"))
print(sequential_search(arr_list,num))
