def allKindStep(n):
    res= []
    flag = False
    if n%2 == 1:
        flag = True
    two_number = n//2

    for i in range(two_number+1):
        tmp = []
        one_number = 2*(two_number-i)
        for j in range(one_number):
            tmp.append(1)
        for j in range(i):
            tmp.append(2)
        if flag:
            tmp.append(1)
        res.append(tmp)
    return res

def factorial(n):
    res = 1
    for i in range(n):
        res = res*(i+1)
    return res

def climbStairs(n):
    res = 0
    all_types = allKindStep(n)
    for i in all_types:
        one_number = 0
        two_number = 0
        tmp = 0
        for j in i:
            if j == 1:
                one_number +=1
            else:
                two_number +=1
        tmp = factorial(len(i))/factorial(one_number)/factorial(two_number)
        res += tmp
    return int(res)
print(climbStairs(10))
