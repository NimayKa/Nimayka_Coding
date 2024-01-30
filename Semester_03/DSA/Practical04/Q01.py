def  sequential_search (arr_list,search):
    found = False
    for i in range (0,len(arr_list)):
        if search == arr_list[i] and not found: 
            found = True
            text = 'is found at position'
            break
        else:
            text = 'is not found at position'
    return print ("%d %s %d" % (search,text, i))
    
arr_list = [4,5,3,2,1]
num = int(input("Enter the numbers"))
sequential_search(arr_list,num)