class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1
            else:
                res.append(temp)
                temp = 0
        res.append(temp)
        return max(res)