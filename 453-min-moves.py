class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_nums = min(nums)
        res = sum(nums) - len(nums) * min_nums
        return res