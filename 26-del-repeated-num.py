def removeDuplicates( nums):
    i = 0
    while i < len(nums):
        temp = []
        for j in range(i + 1, len(nums)):
            if nums[j] == nums[i]:
                temp.append(j)
            else:
                break
        for n in range(len(temp)-1,-1,-1):
            del (nums[temp[n]])
        i += 1
    return nums

print (removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
