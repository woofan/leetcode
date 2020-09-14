class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s[::-1]
        res = ''
        amount = len(s) // k
        for i in range(amount):
            temp = ''
            counter = i + 1 #if odd number,reversal;if even number,be the same
            if counter%2 == 0:
                temp = s[i*k:i*k+k]
            if counter%2 == 1:
                temp = s[i*k:i*k+k]
                temp = temp[::-1]
            res += temp
        if (counter+1)%2 == 0:#add the rest
            res += s[amount*k:]
        else:
            temp = s[amount*k:]
            temp = temp[::-1]
            res += temp
        return res

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        temp = list(s)
        for i in range(0,len(s),2*k):
            temp[i:i+k] = reversed(temp[i:i+k])
        res = ''.join(temp)
        return res