#其它解法，对原数组和set去重后数组求和，原数组-set*3 = -（唯一数字*2）
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = [0] * 32
        k = 0
        for i in nums:
            for j in range(len(res)):
                res[j] += i>>j & 1
        for i in range(len(res)):
            res[i] = res[i]%3
        for i in range(len(res)):
            k += res[i] * (2**i)
        if res[31] == 1:
            k = ~ (k^0xffffffff)
        return k