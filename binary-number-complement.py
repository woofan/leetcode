def findComplement(num):
    mynum = num
    binary = []
    res = 0
    while mynum > 0:
        temp = mynum%2
        binary.insert(0,(1 if temp == 0 else 0))
        mynum = mynum//2
    for i in range(len(binary)):
        res += binary[i] * (2**(len(binary)-1-i))
    return res

print(findComplement(1))