def foo(s):
    temp = []
    temp_dict = {}
    temp_list = []
    res = ''
    for i in s:
        temp.append(i)
    temp = sorted(temp)
    for i in temp:
        if i not in temp_dict:
            counter = temp.count(i)
            temp_dict[i] = counter
    temp_list = sorted(temp_dict.items(),key=lambda x:x[1],reverse=True)
    for i in temp_list:
        for j in range(i[1]):
            res = '{}{}'.format(res,i[0])
    return res

print(foo('tree'))