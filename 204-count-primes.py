def countPrimes(n):
    res = [1 for i in range(n+1)]
    res[0],res[1] = 0,0
    for i in range(n+1):
        if res[i] == 1:
            for j in range(i+1,n+1):
                if j%i == 0:
                    res[j] = 0
    return sum(res)

def judge(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5+1)):
        if n%i == 0:
            return False
    return True


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        res = [1 for i in range(n)]
        res[0], res[1] = 0, 0
        for i in range(1, int(n ** 0.5) + 1):
            if res[i] == 1:
                for j in range(i * i, n, i):
                    res[j] = 0

        return sum(res)