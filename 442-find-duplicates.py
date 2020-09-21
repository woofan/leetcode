class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        temp = [0]*len(nums)
        for i in nums:
            if temp[i-1] == 0:
                temp[i-1] = i
            elif temp[i-1] == i:
                res.append(i)
        return res