class Solution:
    def fib(self, N: int) -> int:
        if N<0:
            return None
        if N == 0:
            return 0
        if N == 1:
            return 1
        else:
            return  self.fib(N-2) + self.fib(N-1)

    def fib2(self, n):
        fiblist = [0,1]
        for i in range(2,30):
            fiblist[i] = fiblist[i-1] + fiblist[i-2]
        return fiblist[n]

    def fib3(self,n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        temp1 = 0
        temp2 = 1
        for i in range(n-1):
            temp = temp1 + temp2
            temp1 = temp2
            temp2 = temp
        return temp