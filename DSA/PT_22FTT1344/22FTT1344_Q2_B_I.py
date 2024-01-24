
def iteration (list):
    i = 0
    Total = 1
    while i < len (list):
        Total = Total * list[i]
        i+=1
    return print (Total)

    
list = [1,2,3,4,5]
print (list)
iteration(list)

