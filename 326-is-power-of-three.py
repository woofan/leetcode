class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        temp = []
        for i in range(100):
            temp.append(3**i)
        if n in temp:
            return True
        else:
            return False

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n%3 == 0:
            n /= 3
        return n == 1