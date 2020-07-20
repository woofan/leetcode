def coinChange(coins, amount) :
    mini = [1e9] * (amount+1)
    mini[0] = 0
    for i in coins:
        for j in range(i,amount+1):
            mini[j] = min(mini[j],mini[j-i]+1)
    return -1 if mini[-1] == 1e9 else mini[-1]

print(coinChange([1,3,5],11))

