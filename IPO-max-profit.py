def findMaximizedCapital( k, W, Profits, Capital):
    mylist = []
    for i in range(len(Profits)):
        mylist.append([Profits[i],Capital[i]])
    mylist.sort(reverse=True)
    for i in range(k):
        j = 0
        while j < len(mylist):
            if mylist[j][1] <= W:
                W += mylist[j][0]
                mylist.pop(j)
                break
            j += 1
    return W


print(findMaximizedCapital(2,0,[1,2,3],[0,1,1]))
