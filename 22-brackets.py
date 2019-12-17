def generateParenthesis(n):
    if n == 0 :
        return []
    res = [[''],['()']]
    for i in range(2,n+1):
        tmp = []
        for j in range(i):
            list_left = res[j]
            list_right = res[i-j-1]
            for x in list_left:
                for y in list_right:
                    new_one = '('+x+')'+y
                    tmp.append(new_one)
        res.append(tmp)
    return res[n]

'''
以下为暴力求解所有情况，然后剔除错误情况的方法，速度比较慢
'''
# def generateParenthesis(n):
#     result = []
#     if n == 0:
#         return result
#     s = ['()']
#     for i in range(n-1):
#         s = func1(s)
#     return s
#
#
# def func1(mylist):
#     result = set()
#     for s in mylist:
#         res = set()
#         l  = len(s)
#         for i in range(l+1):
#             for j in range(1,l+2):
#                 tmp = s[:i] + '(' + s[i:]
#                 tmp = tmp[:j]+')'+tmp[j:]
#                 res.add(tmp)
#         for x in filter(res):
#             result.add(x)
#     return result
#
# def filter(l):
#     l = list(l)
#     tmp = l.copy()
#     for i in l:
#         flag_left = 0
#         flag_right = 0
#         for j in i:
#             if j == '(':
#                 flag_left += 1
#             elif j == ')':
#                 flag_right+=1
#             if flag_right > flag_left:
#                 tmp.remove(i)
#                 break
#     return tmp