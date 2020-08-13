class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        temp = sorted(nums)
        median = temp[len(temp)//2]
        res = 0
        for i in nums:
            res += abs(i - median)
        return res