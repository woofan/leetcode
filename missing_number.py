class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k = 0
        p = 0
        for i in nums:
            k += i
        for i in range(len(nums)+1):
            p += i
        return p-k