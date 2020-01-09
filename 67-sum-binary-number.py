def addBinary(a,b):
    l = max(len(a),len(b))
    res = ''
    flag = 0
    if len(a) < l:
        for i in range(l-len(a)):
            a = '0' + a
    if len(b) < l:
        for i in range(l - len(b)):
            b = '0' + b
    for i in range(l-1,-1,-1):
        tmp = int(a[i]) + int(b[i]) + flag
        if tmp <2:
            res = str(tmp) + res
        else:
            res = str(tmp%2) + res
        flag = tmp//2
    if flag == 1:
        res = str(flag) + res
    return res


print(addBinary('1010','1011'))