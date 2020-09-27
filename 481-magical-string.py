def magicalString(n):
    magical_list = [1, 2, 2]
    index = 2
    res = 0
    while len(magical_list) <= n:
        temp = 1 if magical_list[-1] == 2 else 2
        for i in range(magical_list[index]):
            magical_list.append(temp)
        index += 1
    for i in magical_list[:n]:
        if i == 1:
            res += 1
    return magical_list

print(magicalString(10))