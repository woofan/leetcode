class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        temp = 0
        res = ''
        l = max(len(num1),len(num2))
        for i in range(l-len(num1)):
            num1 = f'{0}{num1}'
        for i in range(l-len(num2)):
            num2 = f'{0}{num2}'
        for i in range(l-1,-1,-1):
            p = int(num1[i]) + int(num2[i]) + temp
            temp = p//10
            res = f'{p%10}{res}'
        if temp >0:
            res = f'{temp}{res}'
        return res