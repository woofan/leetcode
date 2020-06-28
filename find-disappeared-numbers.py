def findDisappearedNumbers1(nums):
    res = [0] * len(nums)
    for i in nums:
        res[i - 1] = i
    for i in range(len(res) - 1, -1, -1):
        if res[i] != 0:
            res.pop(i)
        else:
            res[i] = i+1
    return res

def findDisappearedNumbers(nums):
    for i in nums:
        temp = abs(i)
        nums[temp - 1] = -abs(nums[temp - 1])
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < 0:
            nums.pop(i)
        else:
            nums[i] = i + 1
    return nums
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))