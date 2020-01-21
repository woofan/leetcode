#约瑟夫环问题求解的两种方法

#非递归方法
def f1(n,m,k):
    for i in range(n):
        k = (k + m - 1) % (i+1) + 1
    return k

#递归方法
def f2(n,m):
    if n == 1:
        return 0
    return (f2(n-1,m)+m)%n


print(f1(15,3,0))
print(f2(15,3))