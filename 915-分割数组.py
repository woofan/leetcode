#coding:utf-8
#!python3
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        min_list = [0]*len(nums)
        min_list[-1] = nums[-1]
        max_num = nums[0]
        for i in range(len(nums)-2,0,-1):
            min_list[i] = min(nums[i],min_list[i+1])
        for i in range(1,len(nums)):
            if max_num <= min_list[i]:
                return i
            else:
                max_num = max(max_num,nums[i])

