class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        l = len(nums)
        res = [0] * l
        temp = []
        for i in range(l):
            temp.append([nums[i],i])
        temp = sorted(temp,reverse = True)
        for i in range(l):
            if i == 0:
                res[temp[i][1]] = 'Gold Medal'
            if i == 1:
                res[temp[i][1]] = 'Silver Medal'
            if i == 2:
                res[temp[i][1]] = 'Bronze Medal'
            if i > 2:
                res[temp[i][1]] = str(i+1)
        return res