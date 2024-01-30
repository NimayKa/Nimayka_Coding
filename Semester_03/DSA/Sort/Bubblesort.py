def bubblesort(nums):

    for i in range (len(nums)-1,0,-1):
        for j in range (i):
            if nums[j] >= nums[j+1]:
                temp = nums[j]
                nums [j] = nums[j+1]
                nums[j+1] = temp
            print (nums)
    return nums


nums = [54,26,93,17,77,31,44,56,20]
print(bubblesort(nums))