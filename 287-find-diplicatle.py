import collections
def findDuplicate1( nums):
    temp = collections.Counter(nums).most_common()
    return temp[0][0]

def findDuplicate(nums):
    left = 1
    right = len(nums)-1
    while left < right:
        count = 0
        mid = (right + left)//2
        for i in nums:
            if i <= mid:
                count += 1
        if count > mid:
            right = mid
        else:
            left = mid + 1
    return left

print(findDuplicate([1,2,2,3,4]))