def insertionsort (arr_list):

    for i in range (1,len(arr_list)):
        print(arr_list)
        exchangeChecker = 0
        itemToSort = arr_list[i]

        while arr_list[i-1] > itemToSort and i > 0 :
            exchangeChecker = 1
            print ('Exchange require cos item (%d)is smaller than (%d)'% (itemToSort,arr_list[i-1]))
            arr_list[i], arr_list[i-1] = arr_list[i-1] , arr_list[i]
            i -= 1

        if exchangeChecker == 0:
            print('No Exchanged required. \n')
        else:
            print('Exchanged completed. \n')
            exchangeChecker = 0
    return arr_list

print (insertionsort([7,8,3,5,1,3,5]))