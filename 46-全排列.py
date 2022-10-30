#coding:utf-8
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i,num in enumerate(nums):
            rest = nums[:i] + nums[i+1:]
            for tmp_num in self.permute(rest):
                ans.append([num] + tmp_num)
        return ans

