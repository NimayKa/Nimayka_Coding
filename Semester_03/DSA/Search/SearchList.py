#For Loop
def  sequential_search (arr_list,search):
    found = False
    for indexpos in arr_list:
        if indexpos == search and not found:
            found = True
    return found

#While Loop
def  sequential_search1 (arr_list,search):
    found = False
    indexpos = 0
    while indexpos < len(arr_list) and not found:
        if arr_list[indexpos] == search :
            found = True
        else:
            indexpos = indexpos+1
    return found


arr = [1,2,3,4,5]
num = int(input("Enter The Number to Search:"))

print (sequential_search(arr, num))
print (sequential_search1(arr, num))



