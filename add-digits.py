class Solution:
    def addDigits(self, num: int) -> int:
        while num >=10:
            k = 0
            for i in str(num):
                k += int(i)
            num = k
        return num


class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9+1 if num !=0 else 0