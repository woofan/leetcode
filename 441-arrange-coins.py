def arrangeCoins( n):
    if n == 0:
        return 0
    i = 1
    while i <= n+1:
        if (1+i)*i//2 > n :
            return i-1
        i += 1

print(arrangeCoins(1))