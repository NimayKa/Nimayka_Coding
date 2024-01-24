
def recursive(list, index=0, Total=1):
    if index == len(list):
        return print (Total)
    else:
        Total = Total * list[index]
        return recursive(list, index + 1, Total)

    
list = [1,2,3,4,5]
print (list)

recursive(list)
