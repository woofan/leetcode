#coding:utf-8
def foo(arr):
    if len(arr) <= 1:
        return [arr]
    ans = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for j in foo(rest):
            ans.append([arr[i]] + j)
    return ans


print(foo([1,2,3]))