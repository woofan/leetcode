class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 0:
            return False
        while num%4 == 0:
            num /= 4
        return num == 1

import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and math.log(num,2)%2 ==0