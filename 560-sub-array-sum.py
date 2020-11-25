class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        mydict = {0:1}
        pre_array_num = 0
        for num in nums:
            pre_array_num += num
            temp = pre_array_num - k
            if temp in mydict:
                result += mydict[temp]
            if pre_array_num in mydict:
                mydict[pre_array_num] += 1
            else:
                mydict[pre_array_num] = 1
        return result