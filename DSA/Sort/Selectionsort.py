def selectionsort(nums):
    for i in range (0,len(nums)-1):
        curr_num = i
        
        for j in range (i+1,len(nums)):

            if num[j] < num [curr_num]:
                curr_num = j

        if curr_num != i:
            nums[curr_num],nums[i] = nums [i],nums[curr_num]
    return nums

num=[54,36,93,17,77,31,44,55,20]

print(selectionsort(num))
