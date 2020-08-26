class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] - nums[i] == k:
                    if nums[i] not in res:
                        res.append(nums[i])
                if nums[j] - nums[i] > k:
                    break
        return len(res)