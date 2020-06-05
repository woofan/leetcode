def findMaxLength(nums):
    mydict = {}
    res = 0
    k = 0
    for i in range(len(nums)):
        temp = 1 if nums[i] == 1 else -1
        k += temp
        if k==0:
            res = max(res, i+1)
        else:
            if k not in mydict:
                mydict[k] = i
            else:
                res = max(res, i - mydict[k])
    return res

a = [0,1,0,1,0,0,0,1,1,1,1,1,1,0]
print(findMaxLength(a))

