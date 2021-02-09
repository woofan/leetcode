class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        temp = 0
        for i in nums:
            temp = temp + i
            result.append(temp)
        return result