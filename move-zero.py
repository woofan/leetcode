class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = []
        for i in range(n-1,-1,-1):
            if nums[i] == 0:
                zero.append(0)
                nums.pop(i)
        for i in zero:
            nums.append(0)