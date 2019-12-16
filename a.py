def generateParenthesis(n):
    if n == 0:
        return []
    s = '()'
    for i in range(n-1):
        s = func1(s)
    return s


def func1(s):
    res = set()
    l  = len(s)
    for i in range(l+1):
        for j in range(1,l+2):
            tmp = s[:i] + '(' + s[i:]
            tmp = tmp[:j]+')'+tmp[j:]
            res.add(tmp)
    return filter(res)

def filter(l):
    l = list(l)
    tmp = l
    for i in l:
        flag_left = 0
        flag_right = 0
        for j in i:
            if j == '(':
                flag_left += 1
            elif j == ')':
                flag_right+=1
            if flag_right > flag_left:
                tmp.remove(i)
                break
    return tmp
print(generateParenthesis(3))