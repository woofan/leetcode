#coding:utf-8
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        hashmap = {}
        hashmap[0] = -1
        tmp = 0
        for i,num in enumerate(nums):
            tmp += 1 if num == 1 else -1
            if tmp not in hashmap:
                hashmap[tmp] = i
            else:
                ans = max(ans, abs(hashmap[tmp]-i))
        return ans

s = Solution()
nums = [0,1,0]
print(s.findMaxLength(nums))