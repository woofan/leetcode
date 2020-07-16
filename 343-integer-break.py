class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        res = 1
        for i in range(n//3):
            res *= 3
        if n%3 == 1:
            res = res//3*4
        if n%3 == 2:
            res = res * 2
        return res