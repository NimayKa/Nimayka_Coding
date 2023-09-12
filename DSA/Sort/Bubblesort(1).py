def bubblesort(nums):
    sorted= False

    while not sorted:
        sorted = True
        for i in range (0,len(nums) -1):
            if nums[i] > nums[i+1]:
                sorted = False
                nums[i] ,nums [i+1] = nums[i+1], nums[i] 
                print (nums)
    return nums

num = [54,26,93,17,77,31,44,56,20]
print(bubblesort(num))