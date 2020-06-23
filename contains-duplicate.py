class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = (len(nums) == len(set(nums)))
        return not flag