class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 0:
            return []
        if l == 1:
            return [-1]
        res = [0] * l
        for i in range(l):
            temp = nums[i+1:l] + nums[0:i]
            for j in temp:
                if nums[i] < j:
                    res[i] = j
                    break
                res[i] = -1
        return res
