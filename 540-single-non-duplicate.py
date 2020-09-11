class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if i not in res :
                res.append(i)
            else:
                res.remove(i)
        return res[0]