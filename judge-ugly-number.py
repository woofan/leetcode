'''
to judge if one number has factors which only include 2 、3 and 5
'''
def isugly(num):
    factors = [2,3,5]
    num = abs(num)
    temp = num
    l = []
    while num > 1:
        for i in factors:
            if temp % i == 0:
                l.append(i)
                temp = temp//i
        if num == temp:
            return False
        num = temp
    if num == 1:
        print(l)
        return True

print(isugly(-2147483648))
print(2**31)