import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        res = 0
        temp = math.ceil(math.sqrt(num))
        for i in range(1,temp):
            if (num / i) - (num // i) == 0:
                res += i
                res += num//i
        return (res//2) == num