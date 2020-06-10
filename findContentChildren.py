def findContentChildren(g,s):
    g = sorted(g)
    s = sorted(s)
    flag = [0] * len(g)
    res = 0
    for i in s:
        for j in range(len(g)):
            if flag[j] == 0 and i >= g[j]:
                flag[j] = 1
                break
            if i < g[j]:
                break
    for i in flag:
        res += i
    return res

def doubleFlag(g,s):
    g = sorted(g)
    s = sorted(s)
    flag_g = 0
    flag_s = 0
    res = 0
    while flag_g < len(g) and flag_s < len(s):
        if g[flag_g] <= s[flag_s]:
            res += 1
            flag_s += 1
            flag_g += 1
        else:
            flag_s += 1
    return res


#print(findContentChildren([1,2,3],[3]))
print(doubleFlag([1,2,3],[3]))