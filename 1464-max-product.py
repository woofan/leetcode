class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num_1 = max(nums)
        nums.remove(max_num_1)
        max_num_2 = max(nums)
        return (max_num_1 - 1) * (max_num_2 - 1)
