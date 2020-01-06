def maxSubArray(nums):
    max_sum_list = nums.copy()
    for i in range(len(nums)):
        if i == 0:
            max_sum_list[i] = nums[i]
        else:
            max_sum = nums[i]+max_sum_list[i-1]
            max_sum_list[i] = max(max_sum_list[i],max_sum)
    max_index_right = 0
    for i in range(len(max_sum_list)):
        if max_sum_list[i] >= max_sum_list[max_index_right]:
            max_index_right = i
    return max_sum_list[max_index_right]

a = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(a))